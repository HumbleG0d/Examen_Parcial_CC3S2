Feature: Rotación de las piezas del juego
  Como jugador
  Quiero poder rotar las piezas
  Para poder organizarlas mejor y completar líneas en el tablero

  Scenario: Rotar el tetrominó 'T' 90 grados en sentido horario
    Given que el tetrominó 'T' está en su posición inicial en el tablero
    When presiono la tecla de rotación
    Then el tetrominó 'T' debería rotarse 90 grados en sentido horario
    Then el tetrominó debería ocupar la nueva posición correctamente en el tablero

  Scenario: Rotar el tetrominó 'I' varias veces
    Given que el tetrominó 'I' está en su posición inicial en el tablero
    When presiono la tecla de rotación una vez
    Then el tetrominó 'I' debería rotarse 90 grados en sentido horario

    When presiono la tecla de rotación nuevamente
    Then el tetrominó 'I' debería rotarse otros 90 grados en sentido horario, quedando a 180 grados de su posición inicial

    When presiono la tecla de rotación una tercera vez
    Then el tetrominó 'I' debería rotarse a 270 grados

    When presiono la tecla de rotación una cuarta vez
    Then el tetrominó 'I' debería volver a su posición inicial
