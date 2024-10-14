import pygame
from src.tetromino.tetromino import TETROMINOS
from src.tetromino.draw import draw_tetromino
CELL_SIZE = 30

class TetrisPiece:
    def move_down(self):
        new_pos = (self.position[0], self.position[1] + CELL_SIZE)
        self.position = new_pos