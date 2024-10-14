import pygame
#from src.tetromino.tetromino import TETROMINOS
CELL_SIZE = 30

# Logica de como cambia la posicion una pieza en caida
class TetrisPiece:
    def move_down(self):
        new_pos = (self.position[0], self.position[1] + CELL_SIZE)
        self.position = new_pos