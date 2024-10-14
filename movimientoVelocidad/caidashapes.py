import pygame
from src.tetromino.colors import COLORS

# Dimensiones del juego
WINDOW_WIDTH = 360
WINDOW_HEIGHT = 750
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 30

class caida_shapes:
    def update(self, delta_time, keys_pressed):
        """Actualiza el estado del juego."""
        self.fall_time += delta_time

        # Controlar la velocidad de caída
        speed = self.fast_fall_speed if keys_pressed[pygame.K_DOWN] else self.fall_speed

        if self.fall_time >= speed:
            new_pos = (self.piece.position[0], self.piece.position[1] + CELL_SIZE)
            if self.is_valid_position(self.piece.tetromino, new_pos):
                self.piece.move_down()
            else:
                # Bloquear la pieza y generar una nueva
                self.lock_piece()
                self.clear_full_rows()
                self.piece = TetrisPiece('T')  # Nueva pieza (puede cambiarse para hacerlo aleatorio)

            self.fall_time = 0  # Reiniciar el temporizador

    def draw(self, window):
        """Dibuja el tablero y la pieza actual."""
        window.fill((0, 0, 0))  # Fondo negro
        self.piece.draw(window)