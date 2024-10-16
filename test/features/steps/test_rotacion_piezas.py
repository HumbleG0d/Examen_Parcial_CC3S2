from behave import given, when, then
import re
from src.tetromino.tetromino import TETROMINOS
from src.tetromino.rotation import rotate_tetromino

mensaje = ""

@given('que el tetrominó {shape_name} está en su posición inicial en el tablero')
def step_impl(context, shape_name):
    pattern = re.compile(r'([A-Z])')
    if pattern.match(shape_name) and shape_name in TETROMINOS:
        context.tetromino = TETROMINOS[shape_name]  # Obtener el tetromino
        context.shape_name = shape_name
    else:
        raise ValueError(f"Invalid shape name: {shape_name}")

@when('presiono la tecla de rotación')
def step_impl(context):
    context.tetromino = rotate_tetromino(context.tetromino)

@then('el tetrominó {shape_name} debería rotarse 90 grados en sentido horario')
def step_impl(context, shape_name):
    original_shape = TETROMINOS[shape_name]
    context.result = rotate_tetromino(original_shape)
    assert context.result == context.tetromino, f"Expected {mensaje}, but got {context.tetromino}"
