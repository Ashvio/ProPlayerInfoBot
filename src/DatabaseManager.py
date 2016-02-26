from lxml import etree
from src.Player import Player, Video
import praw
import re
import pickle

r = praw.Reddit("filling the database")


def contains_video_link(text):
    return "oddshot" in text or "youtu.be" in text or "twitch.tv" in text or "youtube" in text


def get_url(submission):
    text = submission.selftext.lower()

    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                      text)
    for url in urls:
        if contains_video_link(url):
            return url
        else:
            curr_url = submission.url
            # print(curr_url)
            return curr_url


def is_video(submission):
    if not submission.is_self:
        return contains_video_link(submission.domain)
    else:
        text = submission.selftext.lower()
        return contains_video_link(text)


class DatabaseManager:
    def __init__(self):
        self.database = {}
        self.videos_dict = {}
        self.CURRENT_VERSION = "1.0"
        self.build()
        self.done_submissions = []

    def build(self):
        self.database = self.build_database("../Player_Info/NALCS.html", "NA")
        self.database = self.build_database("../Player_Info/EULCS.html", "EU")
        self.database = self.build_database("../Player_Info/LCK.html", "LCK")
        self.database = self.build_database("../Player_Info/LPL.html", "LPL")

    def find_videos(self):

        for player in self.database.keys():
            player = player.lower()
            submissions = r.search("title:" + player, subreddit="leagueoflegends", sort="top", period="all", limit=50)
            for submission in submissions:
                if submission.score < 50:
                    continue

                if submission.is_self:
                    curr_url = get_url(submission)
                else:
                    curr_url = submission.url

                if is_video(submission):
                    if submission.permalink in self.videos_dict:
                        video = self.videos_dict.get(submission.permalink)
                        self.database[player].add_video(video)
                        video.add_player(self.database[player])
                        print(video.to_table_row(self.database[player]))
                    else:
                        video = Video(title=submission.title, link=curr_url, players_list=[self.database[player]],
                                      upvotes=submission.score)
                        self.database[player].add_video(video)
                        self.videos_dict[submission.permalink] = video
                        print(video.to_table_row(self.database[player]))
        return self.database

    def save_db(self, filename):
        with open(filename, 'wb') as save_file:
            pickle.dump(self, save_file, pickle.HIGHEST_PROTOCOL)

    def add_submission(self, submission):
        self.done_submissions.append(submission.id)

    def is_done(self, submission):
        return submission.id in self.done_submissions

    def build_database(self, filename, region):

        with open(filename, "r", encoding="UTF-8") as html_file:
            table_string = html_file.read()

        parser = etree.XMLParser(recover=True)

        # Turn the string into an actual table
        table = etree.XML(table_string, parser=parser)
        table.xpath('//tr/td//text()')

        rows = iter(table)

        for row in rows:
            element = row[0].find("a")
            if element is not None:
                name = element.get("href")
                # print(name[1:])
                player = Player(name[1:])
                element = row[2].find("a")
                if element is not None:
                    team_name = element.get("href")
                    team_name = team_name[1:].replace('_', " ")
                    player.team_name = team_name

                player.position = row[4].text
                # print(player.position)

                element = row[5].find("a")
                if element is not None:
                    player.stream_link = element.get("href")
                    if "azubu" in player.stream_link.lower():
                        player.stream_site = "Azubu"
                    elif "twitch" in player.stream_link.lower():
                        player.stream_site = "Twitch"

                # put the player in the dictionary
                player.region = region
                self.database[name[1:].lower()] = player
        return self.database


def load_db(filename):
    with open(filename, 'rb') as load_file:
        return pickle.load(load_file)
