from src.DatabaseManager import DatabaseManager, load_db, is_video, get_url
from src.Player import to_comment, Video, Player
import praw
import time
import re


def save(manager, filename):
    manager.save_db(filename)


def get_players(title, db):
    words = re.split(" |'", title)
    # for value in db.values():
    #     print(value.name)
    #     print(value.region)
    player_names = []
    for word in words:
        if word.lower() in db.keys():
            player_names.append(word.lower())

    if len(player_names) is 0:
        return None

    else:
        players = []
        for player in player_names:
            players.append(db[player])
        return players


def run_bot():
    UA = "Pro Player Info-- Helps players on /r/leagueoflegends learn about pro players and see their old plays. " \
         "Contact /u/ashivio."
    login = "ProPlayerInfoBot"
    pw = "fake_password"
    filename = "../Databases/dict-2-25-16.db"

    time0 = time.time()

    r = praw.Reddit(UA)
    r.login(login, pw, disable_warning=True)
    # database.find_videos()
    print("Loading database...", end="")
    manager = load_db(filename)
    print("[DONE]")
    db = manager.database
    # manager.done_submissions = []
    print("Reading submissions...")
    for s in praw.helpers.submission_stream(r, "bottesting", limit=1):

        print("Reading next submission: " + s.title)
        time1 = time.time()
        # Backup database every 5 minutes
        if time1 - time0 > 300:
            time0 = time1

        if not is_video(s):
            continue
        if manager.is_done(s):
            continue

        title = s.title.lower()
        players = get_players(title=title, db=db)
        if players is None:
            print("failed")
            continue

        head = "Hello! I am a new bot to help you find information and resources about your favorite pro players" \
               ". I noticed your post mentioned at least one pro player, so I have put together some information and " \
               "past videos about them. \n\n **Player(s) found in this post:**\n\n"
        body = to_comment(players) + "#\n\n"
        tail = "***\nmeep moop. \n\n  Feedback or questions? Is this posted on " \
               "something that doesn't have to do with pro players? Message me or my owner, /u/ashivio, or just reply" \
               "to this comment."
        print("Replying to submission at " + s.permalink + "...", end="")
        video = Video(s.title, get_url(s), players, s.score)
        # noinspection PyTypeChecker
        for player in players:
            player.add_video(video)

        s.add_comment(head + body + tail)
        print("[DONE]")
        manager.add_submission(s)
        save(manager, filename)

if __name__ == "__main__":
    while True:
        try:
            run_bot()
        except Exception:
            print(str(Exception))
