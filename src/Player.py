
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
