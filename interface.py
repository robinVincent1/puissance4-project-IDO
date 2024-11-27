class Interface:
    def __init__(self, game, victory_checker):
        """
        Initialise l'interface utilisateur pour interagir avec le jeu.
        :param game: Instance du jeu (Game).
        :param victory_checker: Instance du vérificateur de victoire (VictoryChecker).
        """
        self.game = game
        self.victory_checker = victory_checker

    def get_player_input(self):
        """
        Demande au joueur de choisir une colonne.
        :return: Numéro de colonne (indexé à partir de 0).
        """
        while True:
            try:
                column = int(input(f"Joueur {self.game.current_player}, choisissez une colonne (1-{self.game.grid.columns}): ")) - 1
                if 0 <= column < self.game.grid.columns:
                    return column
                else:
                    print(f"Veuillez choisir un numéro entre 1 et {self.game.grid.columns}.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un numéro de colonne.")

    def play_turn(self):
        """
        Permet au joueur actuel de jouer son tour.
        """
        while True:
            column = self.get_player_input()
            if self.game.drop_token(column):
                break

    def run(self):
        """
        Lance le jeu complet jusqu'à ce qu'un joueur gagne ou qu'il y ait égalité.
        """
        while True:
            self.game.grid.display()
            self.play_turn()

            # Vérifie si le joueur courant a gagné
            if self.victory_checker.check_victory(self.game.current_player):
                self.game.grid.display()
                print(f"Félicitations ! Joueur {self.game.current_player} a gagné !")
                break

            # Vérifie si la grille est pleine
            if all(self.game.grid.grid[0][col] != " " for col in range(self.game.grid.columns)):
                self.game.grid.display()
                print("Match nul ! La grille est pleine.")
                break

            self.game.switch_player()
