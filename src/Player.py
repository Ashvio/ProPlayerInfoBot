import operator


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
        self.video_list.sort(key=operator.attrgetter("upvotes"), reverse=True)

    def to_comment(self):
        heading = "|Player | Team | Region | Position | Stream |\n|:--:|:--:|:--:|:--:|:--:|:--:|:--:|\n"
        return heading + self.info_table() + "\n\n" + self.video_table()

    def info_table(self):
        row = "|{name}|{team_name}|{region}|{position}|[{stream_site}]({stream_link})|"
        row = row.format(name=self.name, team_name=self.team_name, region=self.region, position=self.position,
                         stream_site=self.stream_site, stream_link=self.stream_link)
        return row.replace("|[]()|", "")

    def video_table(self):
        heading = "|Video|Score|Other Players|\n|:--:|:--:|:--|\n"
        rows = ""
        for index, video in enumerate(self.video_list):
            if (index >= 5):
                break
            rows += video.to_table_row(self) + "\n"
        if rows is not "":
            return heading + rows
        else:
            return ""


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
        return row.format(title=self.title.replace("|", "-"), link=self.link, upvotes=self.upvotes, players=players)

    def add_player(self, player):
        self.players_list.append(player)


def to_comment(players):
    heading = "|Player | Team | Region | Position | Stream |\n|:--:|:--:|:--:|:--:|:--:|:--:|:--:|\n"
    data = ""
    for player in players:
        data += player.info_table() + "\n"
    for player in players:
        video_table = player.video_table()
        if video_table is not "":
            data += "#####Top 5 Links with " + player.name + ":\n\n"
            data += video_table
        else:
            data += "No videos found for " + player.name + "\n\n"

    return heading + data
