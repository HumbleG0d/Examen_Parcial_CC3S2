import pygame
from tetromino.rotation import rotate_tetromino 
from tetromino.draw import draw_tetromino  
from board.board import draw_board
from tetromino.radown_tetromino import generate_random_tetromino
from punctuation.score import Score  # Importamos la clase Score
from movimientovelocidad.caidashapes import FallManager  # Importar la clase FallManager para gestionar la caída

NEW_TETROMINO_TIME = 2000

def main():
    window, clock, running, grid, score = draw_board()
    
    # Inicializamos la puntuación
    score = Score()

    tetromino, shape_name = generate_random_tetromino()
    position = (120, 0)  # Definimos la posición inicial del tetrominó
    creation_timer = 0  # Control del tiempo de creación de nuevos tetrominós

    fall_manager = FallManager()


    while running:
        time_passed = clock.get_rawtime()
        creation_timer += time_passed

        clock.tick(60)

        for event in pygame.event.get():

        pygame.display.flip()  # Actualizar la pantalla

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    position[0] -= 30
                elif event.key == pygame.K_RIGHT:
                    position[0] += 30
                elif event.key == pygame.K_DOWN:
                    position[1] += 30
                elif event.key == pygame.K_UP:
                    tetromino = rotate_tetromino(tetromino)

        fall_manager.update_fall_speed(time_passed)

        if fall_manager.update_fall_timer(time_passed):
            position[1] += 30

        if position[1] + len(tetromino) * 30 > window.get_height():
            tetromino, shape_name = generate_random_tetromino()
            position = [120, 0]
            creation_timer = 0

        window.fill((0, 0, 0))
        draw_tetromino(window, tetromino, position, shape_name)
        # Mostrar la puntuación en pantalla
        display_score(window, score.points)
        pygame.display.flip()


    pygame.quit()

# Función para mostrar la puntuación en pantalla
def display_score(window, points):
    font = pygame.font.SysFont(None, 30)
    score_surface = font.render(f"Puntuación: {points}", True, (255, 255, 255))
    window.blit(score_surface, (10, 10))

if __name__ == "__main__":
    main()
