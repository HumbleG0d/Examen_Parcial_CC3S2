def rotate_tetromino(tetromino):
    return [list(row) for row in zip(*tetromino[::-1])] # Rota el tetromino en sentido horario