class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.team_name = ""
        self.region = ""
        self.position = ""
        self.stream_link = ""
        self.stream_site = ""
        self.video_list = []

    def add_video(self, new_video):
        self.video_list.append(new_video)

    def to_comment(self):
        heading = "|Player | Team | Region | Position | Stream |\n|:--:|:--:|:--:|:--:|:--:|:--:|:--:|\n"
        return heading + self.info_table() + "\n\n" + self.video_table()

    def info_table(self):
        row = "|{name}|{team_name}|{region}|{position}|[{stream_site}]({stream_link})|"
        return row.format(name=self.name, team_name=self.team_name, region=self.region, position=self.position,
                          stream_site=self.stream_site, stream_link=self.stream_link)

    def video_table(self):
        heading = "|Video|Score|Other players in video|\n|:--:|:--:|:--|\n"
        rows = ""
        for video in self.video_list:
            rows += video.to_table_row(self) + "\n"
        return heading + rows


class Video:
    def __init__(self, title, link, players_list, upvotes):
        self.title = title
        self.link = link
        self.players_list = players_list
        self.upvotes = upvotes

    def to_table_row(self, current_player):
        row = "|[{title}]({link})|+{upvotes}|{players}|"
        players = ""
        for player in self.players_list:
            if player.name is not current_player.name:
                players += player.name + ", "
        players = players[:-2]
        return row.format(title=self.title, link=self.link, upvotes=self.upvotes, players=players)


def player_to_comment(players):
    heading = "|Player | Team | Region | Position | Stream |\n|:--:|:--:|:--:|:--:|:--:|:--:|:--:|\n"
    data = ""
    for player in players:
        data += player.info_table() + "\n"

    return heading + data
