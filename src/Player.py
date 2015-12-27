
class Player:

    def __init__(self, player_name):
        self.name = player_name
        self.team_name = ""
        self.region = ""
        self.position = ""
        self.stream_link = ""
        self.stream_site = ""
        self.list_of_videos = set()


    def add_video(self, new_video):
        self.list_of_videos.add(new_video)

    def to_comment(self):
        return self.info_table() + self.video_table()

    def info_table(self):
        data = "|{name}|{team_name}|{region}|{position}|[{stream_site}]({stream_link})|"
        return data.format(name=self.name, team_name=self.team_name, region=self.region, position=self.position,
                           stream_site=self.stream_site, stream_link=self.stream_link)


    def video_table(self):
        heading = "|"

class Video

    def __init__(self, title):
        self.title = title
        self.link = ""
        self.players_list = []
        self.upvotes = 0


    def to_table_row(self):
        data = "|{"

def player_to_comment(players):
    heading = "|Player | Team | Region | Position | Stream |\n|:--:|:--:|:--:|:--:|:--:|:--:|:--:|\n"
    data = ""
    for player in players:
        data += player.info_table() + "\n"

    return heading + data


def print_info_table(player):
    pass


def print_video_table(player):
    pass
