import pygame
from movimientoCaida.movedown import TetrisPiece

WINDOW_WIDTH = 360
WINDOW_HEIGHT = 750
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 30

# Simula el movimiento de caida de una pieza
class caida_shapes:
    def update(self, delta_time, keys_pressed):
        self.fall_time += delta_time

        speed = self.fast_fall_speed if keys_pressed[pygame.K_DOWN] else self.fall_speed

        if self.fall_time >= speed:
            new_pos = (self.piece.position[0], self.piece.position[1] + CELL_SIZE)
            if self.is_valid_position(self.piece.tetromino, new_pos):
                self.piece.move_down()
            else:
                self.lock_piece()
                self.clear_full_rows()
                self.piece = TetrisPiece('T')

            self.fall_time = 0

    def draw(self, window):
        window.fill((0, 0, 0))
        self.piece.draw(window)