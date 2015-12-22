
class Player:

    def __init__(self, player_name):
        self.name = player_name
        self.team_name = None
        self.region = None
        self.position = None
        self.stream_link = None
        self.stream_site = None
        self.list_of_videos = set()
    def add_video(self, new_video):
        self.list_of_videos.add(new_video)


