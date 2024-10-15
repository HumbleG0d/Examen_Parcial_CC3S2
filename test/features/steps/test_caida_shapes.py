from behave import given, when, then
import time
import threading
from src.game import main

current_position = None

@given('que el juego está en curso')
def step_given_game_in_progress(context):
    context.running = True
    context.game_thread = threading.Thread(target=main)
    context.game_thread.start()

@when('aparece una pieza de juego')
def step_when_a_piece_appears(context):
    time.sleep(1)
    global current_position
    current_position = [120, 0]

@then('esta pieza empieza a simular un efecto de caida')
def step_then_piece_falls(context):
    time.sleep(1)
    new_position = [current_position[0], current_position[1] + 30]

    assert new_position[1] > current_position[1], "La pieza no se ha movido hacia abajo."

def after_scenario(context):
    context.running = False
    context.game_thread.join()