import pygame

WINDOW_WIDTH = 360 # Ancho de la ventana
WINDOW_HEIGHT = 750 # Alto de la ventana

def draw_board():
    pygame.init() # Inicializar pygame
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Crear la ventana
    pygame.display.set_caption("Tetris") # Titulo de la ventana

    clock = pygame.time.Clock() # Crear un temporizador
    running = True # Variable para controlar si el juego esta corriendo

    return window , clock , running