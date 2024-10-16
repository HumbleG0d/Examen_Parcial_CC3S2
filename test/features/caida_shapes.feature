Feature: Simular el efecto de caida de una pieza de Tetris

    Scenario: Aparece una pieza y comienza a caer
        Given que el juego está en curso
        When aparece una pieza de juego
        Then esta pieza empieza a simular un efecto de caida
