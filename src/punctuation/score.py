class Score:
    """
    La clase Score se encarga de gestionar la puntuación, el nivel y las líneas eliminadas de un jugador
    en un juego basado en completar líneas (como Tetris). La puntuación se incrementa dependiendo del número
    de líneas eliminadas y del nivel del jugador.

    Atributos:
    - points (int): La puntuación actual del jugador.
    - level (int): El nivel actual del jugador. Aumenta a medida que el jugador elimina más líneas.
    - lines_cleared (int): El número total de líneas que el jugador ha eliminado.
    """

    def __init__(self):
        """
        Inicializa un nuevo objeto Score con los siguientes valores por defecto:
        - points: 0 (sin puntos iniciales)
        - level: 1 (el nivel inicial es 1)
        - lines_cleared: 0 (sin líneas eliminadas al comienzo)
        """
        self.points = 0
        self.level = 1
        self.lines_cleared = 0

    def update(self, lines_cleared):
        """
        Actualiza la puntuación del jugador y el número de líneas eliminadas basándose en
        cuántas líneas el jugador ha completado. La puntuación por línea eliminada aumenta
        según el nivel actual del jugador.

        Args:
        - lines_cleared (int): El número de líneas que el jugador ha eliminado en una sola acción.

        Lógica:
        - 1 línea = +100 puntos
        - 2 líneas = +300 puntos
        - 3 líneas = +500 puntos
        - 4 líneas = +800 puntos
        Estos valores se multiplican por el nivel actual del jugador.

        También verifica si el jugador ha eliminado suficientes líneas para subir de nivel,
        lo que ocurre cada 10 líneas eliminadas.
        """
        self.lines_cleared += lines_cleared
        
        # Sistema de puntuación basado en el número de líneas eliminadas simultáneamente
        points_per_line = {1: 100, 2: 300, 3: 500, 4: 800}
        self.points += points_per_line.get(lines_cleared, 0) * self.level

        # Verificar si es necesario aumentar el nivel
        if self.lines_cleared >= self.level * 10:
            self.level_up()

    def level_up(self):
        """
        Incrementa el nivel del jugador en 1. El nivel se incrementa cada vez que el jugador
        elimina suficientes líneas para completar un múltiplo de 10 líneas.
        """
        self.level += 1

    def reset(self):
        """
        Reinicia la puntuación, el nivel y las líneas eliminadas del jugador a los valores iniciales.
        Esto es útil para reiniciar el juego sin necesidad de crear un nuevo objeto Score.
        """
        self.points = 0
        self.level = 1
        self.lines_cleared = 0

    def get_level(self):
        """
        Retorna el nivel actual del jugador.

        Returns:
        - int: El nivel actual del jugador.
        """
        return self.level

    def get_lines_cleared(self):
        """
        Retorna el número total de líneas eliminadas por el jugador.

        Returns:
        - int: El número de líneas que el jugador ha eliminado.
        """
        return self.lines_cleared
