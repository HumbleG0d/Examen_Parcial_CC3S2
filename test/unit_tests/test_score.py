import unittest
import sys
import os

# Añade la ruta a 'src' al sistema de búsqueda de módulos para poder importar la clase 'Score'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from src.punctuation.score import Score  # Importamos la clase Score para realizar las pruebas

class TestScore(unittest.TestCase):
    """
    Clase que contiene las pruebas unitarias para la clase Score.
    Se encarga de verificar que el sistema de puntuación funciona como se espera.
    """

    def setUp(self):
        """
        Método que se ejecuta antes de cada prueba.
        Inicializa una nueva instancia de la clase Score para asegurarse de que
        cada prueba empiece con un objeto Score limpio.
        """
        self.score = Score()

    def test_initial_score_is_zero(self):
        """
        Prueba que verifica que la puntuación inicial, el nivel y las líneas eliminadas
        sean todos iguales a 0 al instanciar un objeto de la clase Score.
        """
        self.assertEqual(self.score.points, 0)
        self.assertEqual(self.score.level, 1)
        self.assertEqual(self.score.lines_cleared, 0)

    def test_update_score_single_line(self):
        """
        Prueba que verifica que al eliminar una línea, la puntuación se incremente en 100 puntos.
        Esto es consistente con las reglas típicas de juegos de tipo Tetris.
        """
        self.score.update(1)
        self.assertEqual(self.score.points, 100)

    def test_update_score_multiple_lines(self):
        """
        Prueba que verifica que al eliminar 2 líneas simultáneamente, la puntuación se incremente en 300 puntos.
        Esto simula la mecánica de juego donde eliminar más líneas otorga más puntos.
        """
        self.score.update(2)
        self.assertEqual(self.score.points, 300)

    def test_update_score_with_level(self):
        """
        Prueba que verifica que el nivel se incremente adecuadamente después de eliminar un cierto número de líneas (10 en este caso).
        Además, verifica que la puntuación se actualice correctamente al eliminar líneas en distintos niveles.
        """
        for _ in range(10):
            self.score.update(1)  # Simula la eliminación de 10 líneas

        self.assertEqual(self.score.level, 2)  # Verifica que el nivel ha aumentado a 2
        self.assertEqual(self.score.points, 1000)  # Verifica que la puntuación total es 1000 (100 por cada línea eliminada)

    def test_reset_score(self):
        """
        Prueba que verifica que el método 'reset' reinicia la puntuación, el nivel y las líneas eliminadas a 0.
        Esto asegura que el sistema de puntuación puede restablecerse correctamente cuando sea necesario.
        """
        self.score.update(1)  # Aumenta la puntuación para luego comprobar el reinicio
        self.score.reset()  # Reinicia el estado del objeto Score
        self.assertEqual(self.score.points, 0)  # Verifica que la puntuación es 0
        self.assertEqual(self.score.level, 1)  # Verifica que el nivel es 1
        self.assertEqual(self.score.lines_cleared, 0)  # Verifica que las líneas eliminadas son 0

if __name__ == '__main__':
    # Ejecuta las pruebas si el archivo se ejecuta directamente
    unittest.main()
