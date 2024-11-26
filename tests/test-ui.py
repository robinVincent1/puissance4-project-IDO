import unittest
from unittest.mock import patch
from grid import Grid
from game_logic import Game
from victory_conditions import VictoryChecker
from interface import Interface


class TestInterface(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()
        self.game = Game(self.grid)
        self.checker = VictoryChecker(self.grid)
        self.interface = Interface(self.game, self.checker)

    @patch("builtins.input", side_effect=["1"])
    def test_get_player_input_valid(self, mock_input):
        column = self.interface.get_player_input()
        self.assertEqual(column, 0)

    @patch("builtins.input", side_effect=["-1", "8", "1"])
    def test_get_player_input_invalid(self, mock_input):
        column = self.interface.get_player_input()
        self.assertEqual(column, 0)


if __name__ == "__main__":
    unittest.main()
