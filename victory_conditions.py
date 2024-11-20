class VictoryChecker:
    def __init__(self, grid):
        self.grid = grid.grid

    def check_horizontal(self, player):
        for row in self.grid:
            for col in range(len(row) - 3):
                if all(cell == player for cell in row[col:col + 4]):
                    return True
        return False