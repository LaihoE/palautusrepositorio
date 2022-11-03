from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


class Statistics:
    def __init__(self, pr: PlayerReader):
        self._players = pr.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player
        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )
        return list(players_of_team)

    def top(self, how_many, sort_by):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=lambda x: getattr(x, str(sort_by.name).lower())
        )
        return sorted_players[:how_many]