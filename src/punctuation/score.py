class Score:
    def __init__(self):
        self.points = 0
        self.level = 1
        self.lines_cleared = 0

    def update(self, lines_cleared):
        self.lines_cleared += lines_cleared
        
        # Sistema de puntuación basado en el número de líneas eliminadas
        points_per_line = {1: 100, 2: 300, 3: 500, 4: 800}
        self.points += points_per_line.get(lines_cleared, 0) * self.level

        # Actualizar el nivel
        if self.lines_cleared >= self.level * 10:
            self.level_up()

    def level_up(self):
        self.level += 1

    def reset(self):
        # Reiniciar la puntuación, el nivel y las líneas eliminadas
        self.points = 0
        self.level = 1
        self.lines_cleared = 0

    def get_level(self):
        return self.level

    def get_lines_cleared(self):
        return self.lines_cleared
