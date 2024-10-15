import pygame
from tetromino.rotation import rotate_tetromino 
from tetromino.draw import draw_tetromino  
from board.board import draw_board, check_lines
from tetromino.radown_tetromino import generate_random_tetromino
from punctuation.score import Score
from movimientovelocidad.caidashapes import FallManager

NEW_TETROMINO_TIME = 2000

def main():
    window, clock, running, grid, score = draw_board()
    
    # Inicializamos la puntuación
    score = Score()

    tetromino, shape_name = generate_random_tetromino()
    position = [120, 0]
    creation_timer = 0

    fall_manager = FallManager()

    while running:
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
                fix_tetromino_in_place(grid, tetromino, position)
                
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
                    print("Game Over")
                    running = False

        window.fill((0, 0, 0))
        draw_tetromino(window, tetromino, position, shape_name)
        draw_grid(window, grid)
        display_score(window, score.points)
        pygame.display.flip()

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

def fix_tetromino_in_place(grid, tetromino, position):
    for y, row in enumerate(tetromino):
        for x, cell in enumerate(row):
            if cell:
                grid_y = (position[1] // 30) + y
                grid_x = (position[0] // 30) + x
                grid[grid_y][grid_x] = cell

# Función para dibujar la cuadrícula
def draw_grid(window, grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(window, (128, 128, 128), pygame.Rect(x * 30, y * 30, 30, 30))

# Función para mostrar la puntuación en pantalla
def display_score(window, points):
    font = pygame.font.SysFont(None, 30)
    score_surface = font.render(f"Puntuación: {points}", True, (255, 255, 255))
    window.blit(score_surface, (10, 10))

if __name__ == "__main__":
    main()
