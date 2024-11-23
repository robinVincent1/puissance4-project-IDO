class Game:
    def __init__(self, grid):
        self.grid = grid
        self.current_player = "X"

    def drop_token(self, column):
        for row in reversed(self.grid.grid):
            if row[column] == " ":
                row[column] = self.current_player
                return True
        return False