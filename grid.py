class Grid:
    def __init__(self, rows=6, columns=7):
        """
        Initialise une grille vide pour le Puissance 4.
        :param rows: Nombre de lignes (par défaut 6).
        :param columns: Nombre de colonnes (par défaut 7).
        """
        self.rows = rows
        self.columns = columns
        self.grid = [[" " for _ in range(columns)] for _ in range(rows)]

    def display(self):
        """Affiche la grille dans la console."""
        for row in self.grid:
            print("| " + " | ".join(row) + " |")
        print("  " + "   ".join(map(str, range(1, self.columns + 1))))
