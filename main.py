from grid import Grid
from game_logic import Game
from victory_conditions import VictoryChecker
from interface import Interface

if __name__ == "__main__":
    grid = Grid()
    game = Game(grid)
    checker = VictoryChecker(grid)
    interface = Interface(game, checker)

    interface.run()