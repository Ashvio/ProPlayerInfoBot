import praw
import time
r = praw.Reddit("ProPlayerInfo v 1.0")
keywords = set(["bjergson","dyrus", "talon"])
for word in keywords:
    print(word)
#r.login("ProPlayerInfoBot", "MojoJojoBridgeUnderTroubledWater")
already_visited = set()
run_count = 0
while True:
    print("Running " + run_count.__str__())
    run_count += 1
    submissions = r.get_subreddit("leagueoflegends").get_hot(limit=5)
    for submission in submissions:
        text = submission.title.lower()
        domain = submission.domain
        is_title = domain == "youtube.com"
        list_of_words = str.split(text)
        contains_keyword = False
        for word in list_of_words:
            if keywords.__contains__(word):
                containsKeyword = True
        if not already_visited.__contains__(submission.id) and contains_keyword and is_title:
            already_visited.add(submission.id)
            print("SUCCESS!")
    time.sleep(1800)



