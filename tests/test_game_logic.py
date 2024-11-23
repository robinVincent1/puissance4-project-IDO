import unittest
from grid import Grid
from game_logic import Game


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()
        self.game = Game(self.grid)

    def test_drop_token(self):
        self.assertTrue(self.game.drop_token(0))  # Jeton ajouté avec succès
        self.assertEqual(self.grid.grid[-1][0], "X")

    def test_switch_player(self):
        self.game.switch_player()
        self.assertEqual(self.game.current_player, "O")

    def test_column_full(self):
        for _ in range(6):
            self.game.drop_token(0)
        self.assertFalse(self.game.drop_token(0))  # Colonne pleine


if __name__ == "__main__":
    unittest.main()
