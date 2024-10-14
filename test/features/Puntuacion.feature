Feature: Sistema de puntuación
  Como jugador, necesito un sistema de puntuación que se actualice cuando completo líneas, para que pueda ver cuántos puntos he ganado.

  Scenario: El jugador completa una línea
    Given el jugador tiene una puntuación inicial de 0
    When el jugador completa una línea
    Then la puntuación debe incrementarse en 100 puntos

  Scenario: El jugador completa múltiples líneas
    Given el jugador tiene una puntuación inicial de 0
    When el jugador completa 2 líneas
    Then la puntuación debe incrementarse en 300 puntos
