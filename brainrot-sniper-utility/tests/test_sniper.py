import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src import Sniper, find_brainrot_games
from unittest.mock import patch, MagicMock
import unittest

class TestFinder(unittest.TestCase):
    @patch("src.finder.requests.get")
    def test_find_brainrot_games(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "data": [
                {"id": 1, "name": "skibidi toilet", "description": "rizz", "playing": 10},
                {"id": 2, "name": "normal game", "description": "nothing", "playing": 5},
            ]
        }
        mock_get.return_value = mock_resp
        games = find_brainrot_games(max_games=10)
        self.assertEqual(len(games), 1)
        self.assertEqual(games[0]["id"], 1)

class TestSniper(unittest.TestCase):
    @patch("src.sniper.requests.get")
    def test_fetch_players(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "data": [
                {"playing": 20},
                {"playing": 30},
            ]
        }
        mock_get.return_value = mock_resp
        sniper = Sniper(12345)
        total = sniper._fetch_players()
        self.assertEqual(total, 50)

if __name__ == "__main__":
    unittest.main()