# draw.py
import pygame
from tetromino.colors import COLORS

def draw_tetromino(surface, shape, position, shape_name):
    x_offset, y_offset = position # Obtener la posicion del tetromino   
    for i, row in enumerate(shape): # Recorrer cada fila del tetromino
        for j, cell in enumerate(row): # Recorrer cada celda de la fila
            if cell:  # Si es un bloque (1)
                pygame.draw.rect(surface, COLORS[shape_name], # Dibujar el bloque
                                 (x_offset + j * 30, y_offset + i * 30, 30, 30))
                pygame.draw.rect(surface, (0, 0, 0), # Dibujar el borde del bloque  
                                 (x_offset + j * 30, y_offset + i * 30, 30, 30), 1)  # Bordes