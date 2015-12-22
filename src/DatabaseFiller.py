class Player:
    def __init__(self, playername, teamname, region, position, streamlink):
        self.name = playername
        self.teamname = teamname
        self.region = region
        self.position = position
        self.streamlink = streamlink
        self.list_of_videos = set()
    def add_video(self, new_video):
        self.list_of_videos.add(new_video)

import praw
r = praw.Reddit("fill the database")
#for every player in the parsed list
#replace bjergson
p = Player("a", "b", "c", "d", "e", "f")
submissions = r.search(p.name, subreddit="leagueoflegends")
for submission in submissions:
    #check if video
    domain = submission.domain
    is_title = ((domain == "youtube.com") or (domain == "youtu.be") or (domain == "twitch.tv") or (domain == "oddshot.tv"))
    word = submission.selftext.lower()
    if word.__contains__("oddshot") or word.__contains__("youtu.be") or word.__contains__("twitch.tv") or word.__contains__("youtube"):
            is_title = True
    if is_title:
        #add the submission to the database


