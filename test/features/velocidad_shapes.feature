Feature: Simular la aceleración de la caída de piezas en Tetris

  Scenario: Las piezas caen más rápido después de un tiempo considerable
    Given el juego está en curso
    When el jugador ya está jugando un tiempo considerable
    Then las piezas del juego simulan una caída más rápida