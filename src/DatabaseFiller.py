from src.Player import Player
from src.PlayerDatabaseManager import build_database
import praw

r = praw.Reddit("fill the database")
#for every player in the parsed list

for player in build_database("../NALCS.html", "NA"):
    submissions = r.search(player.name, subreddit="leagueoflegends", sort="top", period="all")
    for submission in submissions:
        domain = submission.domain
        is_title = ((domain == "youtube.com") or (domain == "youtu.be") or (domain == "twitch.tv") or (domain == "oddshot.tv"))
        word = submission.selftext.lower()
        if "oddshot" in word or "youtu.be" in word or "twitch.tv" in word or "youtube" in word:
            is_title = True
        if is_title:
            player.add_video(submission)





