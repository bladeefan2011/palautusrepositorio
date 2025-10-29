import unittest
from statistics_service import StatisticsService
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_existing_player(self):
        player = self.stats.search("Gretzky")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Gretzky")

    def test_search_returns_none_if_player_not_found(self):
        player = self.stats.search("Nonexistent")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        team_players = self.stats.team("EDM")
        names = [p.name for p in team_players]
        self.assertEqual(len(team_players), 3)
        self.assertIn("Kurri", names)
        self.assertIn("Gretzky", names)
        self.assertIn("Semenko", names)

    def test_top_returns_players_in_correct_order(self):
        top_players = self.stats.top(3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")

    def test_top_returns_exact_number_of_players(self):
        top_players = self.stats.top(1)
        self.assertEqual(len(top_players), 1)
        self.assertEqual(top_players[0].name, "Gretzky")


if __name__ == '__main__':
    unittest.main()

