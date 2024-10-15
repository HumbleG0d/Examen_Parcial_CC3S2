import pygame

WINDOW_WIDTH = 300  # Ancho de la ventana
WINDOW_HEIGHT = 600  # Alto de la ventana
GRID_WIDTH = 10  # Ancho de la cuadrícula en bloques
GRID_HEIGHT = 20  # Alto de la cuadrícula en bloques
BLOCK_SIZE = 30  # Tamaño de cada bloque en píxeles

def draw_board():
    pygame.init()  # Inicializar pygame
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Crear la ventana
    pygame.display.set_caption("Tetris")  # Título de la ventana

    clock = pygame.time.Clock()  # Crear un temporizador
    running = True  # Variable para controlar si el juego está corriendo

    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]  # Crear la cuadrícula vacía
    score = 0  # Inicializar la puntuación
    
    return window, clock, running, grid, score

def check_lines(grid):
    lines_cleared = 0
    for y in range(len(grid)):
        if all(grid[y]):  # Verifica si la fila está completamente llena
            del grid[y]  # Elimina la fila completa
            grid.insert(0, [0 for _ in range(len(grid[0]))])  # Añade una nueva fila vacía en la parte superior
            lines_cleared += 1
    
    return lines_cleared


def calculate_score(lines_cleared):
    # Puntuación por el número de líneas eliminadas simultáneamente
    return {1: 100, 2: 300, 3: 500, 4: 800}.get(lines_cleared, 0)

def update_score(window, score):
    font = pygame.font.Font(None, 36)  # Fuente para el texto de la puntuación
    score_text = font.render(f"Puntuación: {score}", True, (255, 255, 255))  # Renderizar el texto de la puntuación
    window.blit(score_text, (10, 10))  # Mostrar el texto en la ventana
