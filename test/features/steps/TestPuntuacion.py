from behave import given, when, then

# Simulación de la clase Game para el sistema de puntuación
class Game:
    """
    Esta clase simula el sistema de puntuación de un juego.
    Cada vez que se completan líneas, se incrementa la puntuación según el número de líneas completadas.
    """
    def __init__(self):
        """
        Inicializa la puntuación en 0.
        """
        self.score = 0

    def complete_lines(self, lines):
        """
        Incrementa la puntuación según el número de líneas completadas.
        
        - 1 línea -> +100 puntos
        - 2 líneas -> +300 puntos
        - 3 líneas -> +500 puntos
        - 4 líneas -> +800 puntos

        Args:
        - lines (int): El número de líneas completadas por el jugador.
        """
        if lines == 1:
            self.score += 100
        elif lines == 2:
            self.score += 300
        elif lines == 3:
            self.score += 500
        elif lines == 4:
            self.score += 800


# Definición de pasos BDD (Given, When, Then) para las pruebas con behave

@given('el jugador tiene una puntuación inicial de {initial_score:d}')
def step_given_puntuacion_inicial(context, initial_score):
    """
    Paso 'Given' que establece la puntuación inicial del jugador.
    Inicializa un nuevo objeto `Game` y asigna la puntuación inicial.

    Args:
    - initial_score (int): La puntuación inicial del jugador.
    """
    context.game = Game()  # Crea una nueva instancia de Game
    context.game.score = initial_score  # Establece la puntuación inicial


@when('el jugador completa una línea')
def step_when_completa_una_linea(context):
    """
    Paso 'When' que simula que el jugador completa una línea.
    Llama al método `complete_lines` del objeto `Game` para incrementar la puntuación.

    """
    context.game.complete_lines(1)  # Simula que se completó una línea


@when('el jugador completa {lines:d} líneas')
def step_when_completa_varias_lineas(context, lines):
    """
    Paso 'When' que simula que el jugador completa varias líneas.
    Incrementa la puntuación dependiendo del número de líneas completadas.

    Args:
    - lines (int): El número de líneas completadas.
    """
    context.game.complete_lines(lines)  # Simula que se completan múltiples líneas


@then('la puntuación debe incrementarse en {expected_score:d} puntos')
def step_then_verificar_incremento_puntuacion(context, expected_score):
    """
    Paso 'Then' que verifica que la puntuación del jugador es la esperada.
    Compara la puntuación actual del objeto `Game` con la puntuación esperada.

    Args:
    - expected_score (int): La puntuación esperada después de completar las líneas.

    Raises:
    AssertionError: Si la puntuación actual no coincide con la esperada, lanza un error de aserción.
    """
    assert context.game.score == expected_score, (
        f"La puntuación esperada era {expected_score}, pero se obtuvo {context.game.score}"
    )
