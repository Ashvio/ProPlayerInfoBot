import praw
r = praw.Reddit(user_agent="first_script")
submissions = r.get_subreddit("leagueoflegends").get_hot(limit=5)
for x in submissions:
    print(x)
