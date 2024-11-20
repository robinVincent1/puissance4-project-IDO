class VictoryChecker:
    def __init__(self, grid):
        """
                 Initializes victory detector.
                :param grid: Grid instance.
                """
        self.grid = grid.grid

    def check_horizontal(self, player):
        """Check horizontal victories"""
        for row in self.grid:
            for col in range(len(row) - 3):
                if all(cell == player for cell in row[col:col + 4]):
                    return True
        return False

    def check_vertical(self, player):
        """Check vertical victories"""
        for col in range(len(self.grid[0])):
            for row in range(len(self.grid) - 3):
                if all(self.grid[row + i][col] == player for i in range(4)):
                    return True
        return False