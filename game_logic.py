class Game:
    def __init__(self, grid):
        self.grid = grid
        self.current_player = "X"

    def drop_token(self, column):
        for row in reversed(self.grid.grid):
            if row[column] == " ":
                row[column] = self.current_player
                return True
        print(f"La colonne {column + 1} est pleine. Essayez une autre colonne.")

        return False
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

        return False

