import time
import pygame
from behave import given, when, then
from src.game import main
from src.tetromino.radown_tetromino import generate_random_tetromino
from src.game import is_valid_position
from src.movimientovelocidad.caidashapes import FallManager

@given(u'el juego está en curso')
def step_given_game_in_progress(context):
    context.fall_manager = FallManager()  # Inicializa el FallManager

@when(u'el jugador ya está jugando un tiempo considerable')
def step_when_player_is_playing_a_long_time(context):
    # Guarda la velocidad de caída antes de simular el tiempo
    fall_speed_before = context.fall_manager.fall_speed

    # Simula un tiempo que debería hacer que la velocidad de caída disminuya
    context.fall_manager.update_fall_speed(3000)  # Simula 3 segundos

    # Guarda la velocidad de caída después de la simulación
    context.fall_speed_after = context.fall_manager.fall_speed
    context.fall_speed_before = fall_speed_before  # Guarda la velocidad anterior para comparación

@then(u'las piezas del juego simulan una caída más rápida')
def step_then_shapes_fall_faster(context):
    # La velocidad de caída debe haber disminuido, por lo que fall_speed_after debe ser menor que fall_speed_before
    assert context.fall_speed_after < context.fall_speed_before, (
        f"La velocidad de caída no ha cambiado como se esperaba: "
        f"antes: {context.fall_speed_before}, después: {context.fall_speed_after}"
    )