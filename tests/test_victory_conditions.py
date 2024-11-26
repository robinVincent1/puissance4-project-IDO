import unittest
from grid import Grid
from victory_conditions import VictoryChecker


class TestVictoryConditions(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()
        self.checker = VictoryChecker(self.grid)

    def test_horizontal_victory(self):
        self.grid.grid[0][:4] = ["X", "X", "X", "X"]
        self.assertTrue(self.checker.check_victory("X"))

    def test_vertical_victory(self):
        for i in range(4):
            self.grid.grid[i][0] = "X"
        self.assertTrue(self.checker.check_victory("X"))

    def test_no_victory(self):
        self.assertFalse(self.checker.check_victory("X"))


if __name__ == "__main__":
    unittest.main()
