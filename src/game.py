import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ["SDL_AUDIODRIVER"] = "dummy"
import pygame
from tetromino.rotation import rotate_tetromino 
from tetromino.draw import draw_tetromino  
from board.board import draw_board, check_lines
from tetromino.radown_tetromino import generate_random_tetromino
from punctuation.score import Score
from movimientovelocidad.caidashapes import FallManager
from tetromino.colors import COLORS
from prometheus_client import start_http_server, Counter
import time

game_counter = Counter('tetris_games_played','Total number of Tetris games played')

def main():

    start_http_server(8000)
    running = True
    game_over = False

    while running:
        if game_over:
            # Mostrar la pantalla de Game Over
            display_game_over(window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # Reiniciar el juego si se presiona la barra espaciadora
                    game_over = False
                    window, clock, running, grid, score = reset_game()

        else:
            window, clock, running, grid, score = draw_board()
            # Inicializamos la puntuación
            score = Score()

            tetromino, shape_name = generate_random_tetromino()
            position = [120, 0]
            creation_timer = 0

            fall_manager = FallManager()

            while running and not game_over:
                time_passed = clock.get_rawtime()
                creation_timer += time_passed

                clock.tick(60)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            new_position = [position[0] - 30, position[1]]
                            if is_valid_position(new_position, tetromino, grid, window):
                                position = new_position
                        elif event.key == pygame.K_RIGHT:
                            new_position = [position[0] + 30, position[1]]
                            if is_valid_position(new_position, tetromino, grid, window):
                                position = new_position
                        elif event.key == pygame.K_DOWN:
                            new_position = [position[0], position[1] + 30]
                            if is_valid_position(new_position, tetromino, grid, window):
                                position = new_position
                        elif event.key == pygame.K_UP:
                            rotated_tetromino = rotate_tetromino(tetromino)
                            if is_valid_position(position, rotated_tetromino, grid, window):
                                tetromino = rotated_tetromino

                fall_manager.update_fall_speed(time_passed)

                if fall_manager.update_fall_timer(time_passed):
                    new_position = [position[0], position[1] + 30]
                    if is_valid_position(new_position, tetromino, grid, window):
                        position = new_position
                    else:
                        # Fijar el tetrominó en la cuadrícula
                        fix_tetromino_in_place(grid, tetromino, position, shape_name)
                        
                        # Verificar cuántas líneas se completaron
                        lines_cleared = check_lines(grid)
                        
                        # Actualizar la puntuación
                        score.update(lines_cleared)
                        
                        # Generar una nueva pieza
                        tetromino, shape_name = generate_random_tetromino()
                        position = [120, 0]
                        creation_timer = 0

                        # Verificar si el nuevo tetrominó puede aparecer
                        if not is_valid_position(position, tetromino, grid, window):
                            game_over = True

                window.fill((0, 0, 0))
                draw_tetromino(window, tetromino, position, shape_name)
                draw_grid(window, grid)
                display_score(window, score.points)
                pygame.display.flip()

                time.sleep(1)

    pygame.quit()

# Función para verificar si una posición es válida
def is_valid_position(position, tetromino, grid, window):
    for y, row in enumerate(tetromino):
        for x, cell in enumerate(row):
            if cell:
                px = position[0] // 30 + x
                py = position[1] // 30 + y
                if (px < 0 or px >= len(grid[0]) or
                    py >= len(grid) or
                    grid[py][px]):
                    return False
    return True

def fix_tetromino_in_place(grid, tetromino, position, shape_name):
    for y, row in enumerate(tetromino):
        for x, cell in enumerate(row):
            if cell:
                grid_y = (position[1] // 30) + y
                grid_x = (position[0] // 30) + x
                #grid[grid_y][grid_x] = cell
                grid[grid_y][grid_x] = COLORS[shape_name]

# Función para mostrar la pantalla de Game Over
def display_game_over(window):
    font = pygame.font.SysFont(None, 72)
    game_over_surface = font.render("Game Over", True, (255, 0, 0))
    window.blit(game_over_surface, (window.get_width() // 2 - 150, window.get_height() // 2 - 36))

    font_small = pygame.font.SysFont(None, 30)
    restart_surface = font_small.render("Press Space to Restart", True, (255, 255, 255))
    window.blit(restart_surface, (window.get_width() // 2 - 100, window.get_height() // 2 + 50))

    pygame.display.flip()

# Función para reiniciar el juego
def reset_game():
    window, clock, running, grid, score = draw_board()
    return window, clock, running, grid, score

# Función para dibujar la cuadrícula
def draw_grid(window, grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(window, cell, pygame.Rect(x * 30, y * 30, 30, 30))
                pygame.draw.rect(window, (0, 0, 0), pygame.Rect(x * 30, y * 30, 30, 30), 1)

# Función para mostrar la puntuación en pantalla
def display_score(window, points):
    font = pygame.font.SysFont(None, 30)
    score_surface = font.render(f"Puntuación: {points}", True, (255, 255, 255))
    window.blit(score_surface, (10, 10))

if __name__ == "__main__":
    main()
