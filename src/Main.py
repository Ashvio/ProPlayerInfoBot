import praw
import time
r = praw.Reddit("ProPlayerInfo v 1.0")
keywords = set(["bjergson","dyrus", "talon"])
#r.login("ProPlayerInfoBot", "MojoJojoBridgeUnderTroubledWater")
already_visited = set()
run_count = 0
while True:
    print("Running " + run_count.__str__())
    run_count += 1
    submissions = r.get_subreddit("leagueoflegends").get_hot(limit=5)
    for submission in submissions:
        #check if video
        domain = submission.domain
        is_title = (domain == "youtube.com" or domain == "youtu.be" or domain == "twitch.tv" or domain == "oddshot.tv")
        body_text = str.split(submission.selftext.lower())
        for word in body_text:
            if word.__contains__("oddshot") or word.__contains__("youtu.be") or word.__contains__("twitch.tv") or word.__contains__("youtube"):
                is_title = True

        #check for keyword
        text = submission.title.lower()
        list_of_words = str.split(text)
        contains_keyword = False
        for word in list_of_words:
            if keywords.__contains__(word):
                containsKeyword = True

        #return related videos here
        if not already_visited.__contains__(submission.id) and contains_keyword and is_title:
            already_visited.add(submission.id)

    time.sleep(1800)



