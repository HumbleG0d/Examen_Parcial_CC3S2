import pygame

WINDOW_WIDTH = 360 # Ancho de la ventana
WINDOW_HEIGHT = 750 # Alto de la ventana
GRID_WIDTH = 10 # Ancho de la cuadrícula en bloques
GRID_HEIGHT = 20 # Alto de la cuadrícula en bloques
BLOCK_SIZE = 30 # Tamaño de cada bloque en píxeles

def draw_board():
    pygame.init() # Inicializar pygame
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Crear la ventana
    pygame.display.set_caption("Tetris") # Titulo de la ventana

    clock = pygame.time.Clock() # Crear un temporizador
    running = True # Variable para controlar si el juego esta corriendo

    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    score = 0
    
    return window, clock, running, grid, score

def check_lines(grid, score):
    lines_cleared = 0
    for y in range(GRID_HEIGHT - 1, -1, -1):
        if all(grid[y]):
            del grid[y]
            grid.insert(0, [0 for _ in range(GRID_WIDTH)])
            lines_cleared += 1
    
    if lines_cleared > 0:
        score += calculate_score(lines_cleared)
    
    return score

def calculate_score(lines_cleared):
    return {1: 100, 2: 300, 3: 500, 4: 800}.get(lines_cleared, 0)

def update_score(window, score):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Puntuación: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))
