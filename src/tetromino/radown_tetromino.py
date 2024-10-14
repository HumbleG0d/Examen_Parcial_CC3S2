import random
from tetromino.tetromino import TETROMINOS
def generate_random_tetromino():
    shape_name = random.choice(list(TETROMINOS.keys()))  # Elegir un tetrominó aleatoriamente
    tetromino = TETROMINOS[shape_name] # Obtener el tetromino
    return tetromino, shape_name # Devolver el tetromino y el nombre del tetromino