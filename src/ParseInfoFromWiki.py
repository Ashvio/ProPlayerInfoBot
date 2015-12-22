from lxml import etree

from xml.etree import ElementTree as ET

# Open the table and put it in a string
from src.Player import Player


# Returns a list of dictionary mapping player names to players, found in the file


def build_database(filename, region):
    html_file = open(filename, "r", encoding="UTF-8")
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


player_list = build_database("../NALCS.html", "NA")
