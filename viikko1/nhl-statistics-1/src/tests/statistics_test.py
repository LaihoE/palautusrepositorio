import unittest
from statistics import Statistics, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_team(self):
        players = []
        for player in self.statistics.team("EDM"):
            players.append(str(player))
        self.assertEqual(players, ['Semenko EDM 4 + 12 = 16', 'Kurri EDM 37 + 53 = 90', 'Gretzky EDM 35 + 89 = 124'])
    
    def test_search(self):
        player = self.statistics.search("Kurri")
        self.assertEqual(str(player), 'Kurri EDM 37 + 53 = 90')
    
    def test_top_points(self):
        self.assertEqual(str(self.statistics.top(1, SortBy.POINTS)[0]), "Gretzky EDM 35 + 89 = 124")

    def test_top_goals(self):
        self.assertEqual(str(self.statistics.top(1, SortBy.GOALS)[0]), "Lemieux PIT 45 + 54 = 99")
    
    def test_top_assists(self):
        self.assertEqual(str(self.statistics.top(1, SortBy.ASSISTS)[0]), "Gretzky EDM 35 + 89 = 124")

    def test_search_not_found(self):
        player = self.statistics.search("Emil")
        self.assertEqual(player, None)
