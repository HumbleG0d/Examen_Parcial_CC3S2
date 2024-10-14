import pygame
from tetromino.rotation import rotate_tetromino 
from tetromino.draw import draw_tetromino  
from board.board import draw_board;
from tetromino.radown_tetromino import generate_random_tetromino
NEW_TETROMINO_TIME = 500
def main():
    window , clock , running = draw_board()

# Falta agregar la simulacion de caida de la pieza, condicionado a correciones de la tabla y piezas del juego

    tetromino, shape_name = generate_random_tetromino()
    position = (120, 0)  # Definimos la posicion inicial del tetromino
    creation_timer = 0  # Control del tiempo de creación de nuevos tetrominós

    while running:
        creation_timer += clock.get_rawtime()  # Aumenta el temporizador en función del tiempo transcurrido
        clock.tick(60)  # Mantener 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Si se cierra la ventana
                running = False
            if event.type == pygame.KEYDOWN: # Si se presiona una tecla
                if event.key == pygame.K_LEFT: # Si se presiona la tecla izquierda
                    # Mover a la izquierda
                    position = (position[0] - 30, position[1])
                elif event.key == pygame.K_RIGHT: # Si se presiona la tecla derecha
                    # Mover a la derecha
                    position = (position[0] + 30, position[1])
                elif event.key == pygame.K_DOWN: # Si se presiona la tecla abajo
                    # Mover hacia abajo
                    position = (position[0], position[1] + 30)
                elif event.key == pygame.K_UP: # Si se presiona la tecla arriba
                    # Rotar el tetrominó
                    tetromino = rotate_tetromino(tetromino)

        if creation_timer > NEW_TETROMINO_TIME: # Si el temporizador es mayor que el tiempo de creacion de un nuevo tetromino
            tetromino, shape_name = generate_random_tetromino()  # Generar un nuevo tetrominó aleatorio
            position = (120, 0)  # Restablecer la posición inicial del nuevo tetrominó
            creation_timer = 0  # Reiniciar el temporizador de creación

        window.fill((0, 0, 0))  # Limpiar la ventana (fondo negro)
        draw_tetromino(window, tetromino, position, shape_name)  # Dibujar el tetrominó
        pygame.display.flip()  # Actualizar la pantalla

    pygame.quit()

if __name__ == "__main__":
    main()