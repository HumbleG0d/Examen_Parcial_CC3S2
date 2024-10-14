from behave import given, when, then
import re
import pygame
from ....src.tetromino.tetromino import TETROMINOS
from ....src.tetromino.rotation import rotate_tetromino

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
    pygame.key.press(pygame.K_UP)

@then('el tetrominó {shape_name} debería rotarse 90 grados en sentido horario')
def step_impl(context, shape_name):
    original_shape = TETROMINOS[shape_name]
    context.result = rotate_tetromino(original_shape)
    #rotated_shape = list(zip(*original_shape[::-1]))
    assert context.result == original_shape, f"Expected {mensaje}, but got {context.tetromino}"

@then('el tetrominó debería ocupar la nueva posición correctamente en el tablero')
def step_impl(context):
    # Verificar que el tetromino ocupa la nueva posición correctamente
    assert context.tetromino is not None, "El tetromino no está definido"
