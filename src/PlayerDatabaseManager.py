from lxml import etree
from src.Player import Player, Video
import pickle
import sys

# Returns a list of dictionary mapping player names to players, found in the file


def build_database(filename, region):

    with open(filename, "r", encoding="UTF-8") as html_file:
        table_string = html_file.read()

    parser = etree.XMLParser(recover=True)

    # Turn the string into an actual table
    table = etree.XML(table_string, parser=parser)
    table.xpath('//tr/td//text()')

    rows = iter(table)

    player_dict = {}
    for row in rows:
        element = row[0].find("a")
        if element is not None:
            name = element.get("href")
            print(name[1:])
            player = Player(name[1:])
            element = row[2].find("a")
            if element is not None:
                team_name = element.get("href")
                team_name = team_name[1:].replace('_', " ")
                player.team_name = team_name

            player.position = row[4].text
            print(player.position)

            element = row[5].find("a")
            if element is not None:
                player.stream_link = element.get("href")
                if "azubu" in player.stream_link.lower():
                    player.stream_site = "Azubu"
                elif "twitch" in player.stream_link.lower():
                    player.stream_site = "Twitch"

            # put the player in the dictionary
            player.region = region
            player_dict[name[1:]] = player

    return player_dict


def save_to_file(player, filename):
    with open(filename, 'wb') as save_file:
        pickle.dump(player, save_file, pickle.HIGHEST_PROTOCOL)


def load_from_file(filename):
    with open(filename, 'rb') as load_file:
        return pickle.load(load_file)


player_list = build_database(sys.argv[1], "NA")
for player in player_list.values():
    player.add_video(Video("video", "http://example.com", [player], 1))
    player.add_video(Video("video2", "http://example.com", [player_list.get("Doublelift"), player], 2))
    print(player.to_comment())
