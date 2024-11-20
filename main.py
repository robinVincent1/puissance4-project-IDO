from grid import Grid

if __name__ == "__main__":
    # Initialiser la grille
    grid = Grid()

    # Afficher la grille initiale
    print("Grille initiale :")
    grid.display()

    # Modifier manuellement la grille (pour simuler un jeu)
    grid.grid[0][0] = "X"
    grid.grid[1][1] = "O"
    print("\nGrille modifiée :")
    grid.display()

    # Réinitialiser la grille
    grid.reset()
    print("\nGrille après réinitialisation :")
    grid.display()
