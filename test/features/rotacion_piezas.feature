Feature: Rotación de las piezas del juego
  Como jugador
  Quiero poder rotar las piezas
  Para poder organizarlas mejor y completar líneas en el tablero

  Scenario: Rotar el tetrominó T 90 grados en sentido horario
    Given que el tetrominó T está en su posición inicial en el tablero
    When presiono la tecla de rotación
    Then el tetrominó T debería rotarse 90 grados en sentido horario
