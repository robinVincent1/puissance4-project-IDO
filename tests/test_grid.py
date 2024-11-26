import unittest
from grid import Grid


class TestGrid(unittest.TestCase):
    def test_initialization(self):
        grid = Grid()
        self.assertEqual(len(grid.grid), 6)  # Nombre de lignes
        self.assertEqual(len(grid.grid[0]), 7)  # Nombre de colonnes

    def test_reset(self):
        grid = Grid()
        grid.grid[0][0] = "X"
        grid.reset()
        self.assertEqual(grid.grid[0][0], " ")


if __name__ == "__main__":
    unittest.main()
