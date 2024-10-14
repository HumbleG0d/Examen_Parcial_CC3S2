import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from src.punctuation.score import Score  

class TestScore(unittest.TestCase):

    def setUp(self):
        # Inicializamos una nueva instancia de la clase Score antes de cada prueba
        self.score = Score()

    def test_initial_score_is_zero(self):
        # Verificamos que la puntuación inicial sea 0
        self.assertEqual(self.score.points, 0)
        self.assertEqual(self.score.level, 1)
        self.assertEqual(self.score.lines_cleared, 0)

    def test_update_score_single_line(self):
        # Verificamos que al eliminar una línea, el puntaje aumente correctamente
        self.score.update(1)
        self.assertEqual(self.score.points, 100)

    def test_update_score_multiple_lines(self):
        # Verificamos que al eliminar 2 líneas, el puntaje aumente correctamente
        self.score.update(2)
        self.assertEqual(self.score.points, 300)

    def test_update_score_with_level(self):
        # Aumentamos las líneas eliminadas y verificamos que el nivel sube correctamente
        for _ in range(10):
            self.score.update(1)  # Esto debe aumentar el nivel después de 10 líneas
        self.assertEqual(self.score.level, 2)  # El nivel debe ser 2
        self.assertEqual(self.score.points, 1000)  # 100 puntos por cada línea, nivel 1

    def test_reset_score(self):
        # Verificamos que la función reset reinicia correctamente los valores
        self.score.update(1)
        self.score.reset()
        self.assertEqual(self.score.points, 0)
        self.assertEqual(self.score.level, 1)
        self.assertEqual(self.score.lines_cleared, 0)

if __name__ == '__main__':
    unittest.main()
