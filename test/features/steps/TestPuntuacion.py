from behave import given, when, then

# Simulación de la clase Game para el sistema de puntuación
class Game:
    def __init__(self):
        self.score = 0

    def complete_lines(self, lines):
        if lines == 1:
            self.score += 100
        elif lines == 2:
            self.score += 300
        elif lines == 3:
            self.score += 500
        elif lines == 4:
            self.score += 800

@given('el jugador tiene una puntuación inicial de {initial_score:d}')
def step_given_puntuacion_inicial(context, initial_score):
    context.game = Game()
    context.game.score = initial_score

@when('el jugador completa una línea')
def step_when_completa_una_linea(context):
    context.game.complete_lines(1)

@when('el jugador completa {lines:d} líneas')
def step_when_completa_varias_lineas(context, lines):
    context.game.complete_lines(lines)

@then('la puntuación debe incrementarse en {expected_score:d} puntos')
def step_then_verificar_incremento_puntuacion(context, expected_score):
    assert context.game.score == expected_score, f"La puntuación esperada era {expected_score}, pero se obtuvo {context.game.score}"
