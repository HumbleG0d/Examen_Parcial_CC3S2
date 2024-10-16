# Tetris en Consola

## Tabla de Contenidos
## Tabla de Contenidos
1. [Configuración inicial del tablero Kanban y el Product Backlog](#configuración-inicial-del-tablero-kanban-y-el-product-backlog)
2. [Historias de usuario con criterios de aceptación en Gherkin](#historias-de-usuario-con-criterios-de-aceptación-en-gherkin)
3. [Labels sugeridos y su uso](#labels-sugeridos-y-su-uso)
4. [Añadir labels a las historias](#añadir-labels-a-las-historias)
5. [Asignación de puntos de historia](#asignación-de-puntos-de-historia)
6. [Asignación de miembros a cada historia de usuario](#asignación-de-miembros-a-cada-historia-de-usuario)
7. [Configuración de Sprints y reacion del Spring Blacklog](#configuración-de-sprints-y-reacion-del-spring-blacklog)
8. [Configuracion del Burndown Char](#configuracion-del-burndown-char)
9. [Estructura del proyecto](#estructura-del-proyecto)
10. [Instalacion](#instalacion)
11. [Monitoreo con Prometheus y Grafana](#monitoreo-con-prometheus-y-grafana)

## Configuración inicial del tablero Kanban y el Product Backlog

- **Tablero Kanban**: Se creó el tablero Kanban en GitHub para gestionar y visualizar el progreso del proyecto. El tablero contiene las siguientes columnas:
  - **Backlog**: Todas las tareas que aún no han sido trabajadas.
  - **In Progress**: Tareas que están siendo implementadas.
  - **In Review**: Tareas listas para ser revisadas.
  - **Done**: Tareas completadas.
![Imagen del Tablero Kanban](src/Images/KanbanBoard.png)

 - Historias clave para el Proyecto:
    - **Creacion del Tablero.**
    - **Creacion del Tetrominó.**
    - **Rotacion de Tetrominós.**
    - **Detección de Líneas Completas**
    - **Incremento de la velocidad de caída**
    - **Sistema de Puntuación**
    - **Deteccion de Fin del Juego**

## Historias de usuario con criterios de aceptación en Gherkin

Se escribieron las historias de usuario utilizando la sintaxis Gherkin para facilitar la definición clara de criterios de aceptación.

### Se crearon las siguientes historias de usuario

**Historia de Usuario 1: Creacion del Tablero**

- **As a** jugador
- **I need** un tablero donde los tetrominós caigan y se acumulen
- **So that** pueda organizar las piezas para completar líneas y seguir jugando.

### Details and Assumptions
* El tablero tiene un tamaño estándar (por ejemplo, 12 columnas x 25 filas).
* Los tetrominós deben caer dentro del tablero, y una vez que colisionen con el fondo o con otras piezas, deben detenerse.
* El tablero debe actualizarse visualmente en cada movimiento de las piezas.

```gherkin
Given el tablero de juego ha sido creado
When el jugador inicia el juego
Then el tablero debe aparecer vacío y las piezas deben caer dentro de sus límites
```
**Historia de Usuario 2: Creación del Tetrominó**

- **As a** jugador
- **I need** crear un tetrominó que pueda caer y moverse dentro del tablero
- **So that** pueda organizar y rotar las piezas para completar líneas y seguir jugando

### Details and Assumptions
* Los tetrominós pueden ser de diferentes formas (por ejemplo, I, J, L, O, S, T, Z).
* Cada tetrominó debe definirse en una matriz de 4x4.
* El tetrominó debe poder moverse hacia la izquierda, derecha y hacia abajo.
* El jugador debe poder rotar el tetrominó utilizando las teclas de dirección.
* Los tetrominós deben caer desde la parte superior del tablero y detenerse al colisionar con el fondo o con otras piezas.

```gherkin
Given un tetrominó ha sido creado
When el jugador inicia el juego
Then el tetrominó debe aparecer en la parte superior del tablero
And el jugador debe poder moverlo a la izquierda, derecha y hacia abajo
And el jugador debe poder rotar el tetrominó usando la tecla de rotación
```

**Historia de Usuario 3: Rotación de Tetrominós**

- **As a** jugador
- **I need** poder rotar los tetrominós
- **So that** pueda ajustarlos para completar líneas en el tablero

### Details and Assumptions
* Los tetrominós deben rotar 90 grados en el sentido de las agujas del reloj.
* No deben rotar si están bloqueados por otros bloques o los bordes del tablero.

```gherkin
Given un tetromino está cayendo
When el jugador presiona la tecla de rotación
Then el tetromino rota 90 grados si no hay obstrucciones
```

**Historia de Usuario 4: Sistema de caída**

- **As a** Desarrollador 
- **I need** implementar un sistema de caída de piezas
- **So that** para que el juego tenga un correcto funcionamiento

### Details and Assumptions
* El sistema de caída tiene que ser el mismo para todas las partidas de juego

```gherkin
Given que el juego esta en curso
When aparece una pieza de juego
Then esta pieza empieza a simular un efecto de caida
```

**Historia de Usuario 5: Detección de Líneas Completas**

- **As a** jugador
- **I need** que las líneas completas desaparezcan cuando están llenas
- **So that** pueda liberar espacio en el tablero y seguir jugando.

### Details and Assumptions
* El tablero detecta cuando una fila está completamente llena de bloques y elimina esa fila.
* Las filas superiores deben caer una posición después de que una línea desaparece.


```gherkin
Given el jugador ha colocado bloques en el tablero
When una línea del tablero se completa
Then la línea debe desaparecer y las filas superiores deben caer
```
**Historia de Usuario 6: Incremento de velocidad de caída**

- **As a** jugador
- **I need** que la velocidad del juego aumente con el tiempo
- **So that** el juego se vuelva más desafiante

### Details and Assumptions
* La velocidad del juego debe aumentar gradualmente con el tiempo
* Los tetrominos deben caer más rápido a medida que se este más tiempo en el juego


```gherkin
Given el juego está en curso
When el jugador ya esta jugando un tiempo considerable
Then las piezas del juego simulan una caída más rápida
```

**Historia de Usuario 7: Sistema de Puntuación**

- **As a** jugador
- **I need** un sistema de puntuación que se actualice cuando completo líneas
- **So that** ver cuantos puntos he ganado

### Details and Assumptions
* El juego debe registrar la puntuación, que debe incrementarse cuando el jugador completa una o más líneas.
* El puntaje debe mostrarse al jugador en tiempo real.

```gherkin
Given el jugador completa una línea
When la línea desaparece del tablero
Then la puntuación debe incrementarse en función de las líneas eliminadas
```

**Historia de Usuario 8: Detección de Fin del Juego**

- **As a** jugador 
- **I need** que el juego termine cuando los tetrominós lleguen a la parte superior del tablero
- **So that** se finalice la partida y se muestre mi puntaje final

### Details and Assumptions
* El juego debe terminar si los tetrominós llenan el tablero hasta la parte superior.
* Debe mostrarse un mensaje de "Game Over" y la puntuación final.

```gherkin
Given los tetrominós llenan la parte superior del tablero
When no hay más espacio para que caiga otro tetromino
Then el juego termina y se muestra el puntaje final
```

En cada historia de usuario se empleo el siguiente template:
![Imagen del Template](src/Images/Template.png)

## Labels sugeridos y su uso

Se crearon algunos labels para luego asignarlos a cada historia de usuario, segun sus características y funcionalidad

### Segun su Prioridad

- **high priority**: Para indicar que una historia de usuario o tarea es de alta prioridad.
- **medium priority**: Para elementos de prioridad media.
- **low priority**: Para ítems que no requieren atención inmediata.

### Segun su tipo de tarea

- **enhancement**: Etiqueta para mejoras solicitadas o nuevas características que se desean agregar al proyecto. Se usa para separar las mejoras o nuevas funcionalidades de los problemas existentes.

## Añadir labels a las historias

Procederemos a etiquetar cada historia de usuario con su label correspondiente , segun su funcionalidad y función.

**Historia de Usuario 1: Creacion del Tablero**

- **Label:** ```high priority```
- **Justificación:** El tablero es esencial para el juego. Todas las demás funcionalidades dependen de su existencia, por lo que es prioritario implementarlo.

- **Label:** ```enhancement```
- **Justificación:** La creación del tablero es una característica central del juego. Sin un tablero, no se puede ejecutar el juego, ya que es donde ocurren todas las interacciones.


**Historia de Usuario 2: Creacion del Tetrominó**

- **Label:** ```high priority```
- **Justificación:** La creación del tetrominó es una funcionalidad fundamental para el juego de Tetris. Sin los tetrominós, no habría piezas para jugar, lo que hace que esta característica sea esencial para el funcionamiento básico del juego. 
- **Label:** ```enhancement```
- **Justificación:** Se aplica porque la creación del tetrominó es una nueva característica que mejora significativamente la funcionalidad del juego.

**Historia de Usuario 3: Rotacion de Tetrominós**

- **Label:** ```high priority```
- **Justificación:** La rotación es fundamental para la jugabilidad, ya que sin esta opción, el jugador no podría colocar los tetrominós de forma estratégica, afectando negativamente la experiencia de juego.
- **Label:** ```enhancement```
- **Justificación:** La rotación de tetrominós es una característica esencial del juego de Tetris que permite al jugador ajustar las piezas para completar líneas de manera eficiente..

**Historia de Usuario 4: Sistema de caída**

- **Label:** ```high priority```
- **Justificación:** La funcionalidad de caída es crucial para que el juego sea jugable. Sin esta característica, no sería posible jugar, por lo que es una alta prioridad.

- **Label:** ```enhancement```
- **Justificación:** La caída de tetrominós es una funcionalidad clave en el juego de Tetris, ya que los bloques deben caer de manera automática para que el jugador pueda interactuar con ellos.


**Historia de Usuario 5: Deteccion de Lineas Completas**

- **Label:** ```high priority```
- **Justificación:** Esta funcionalidad es clave para la jugabilidad, ya que sin ella el tablero se llenaría rápidamente, haciendo que el juego sea imposible de continuar..

- **Label:** ```enhancement```
- **Justificación:** La detección de líneas completas es una de las mecánicas fundamentales de Tetris, ya que permite al jugador ganar puntos y liberar espacio en el tablero.

**Historia de Usuario 6: Incremento de velocidad de caída**

- **Label:** ```medium priority```
- **Justificación:** La velocidad de caída es crucial para la dificultad del juego, ya que afecta directamente la rapidez con que las piezas deben ser manejadas.

- **Label:** ```enhancement```
- **Justificación:** El aumento de la velocidad de caída es una característica esencial del juego de Tetris, ya que permite al jugador avanzar más rápidamente.

**Historia de Usuario 7: Sistema de Puntuacion**

- **Label:** ```medium priority```
- **Justificación:** Aunque es importante para el juego, la funcionalidad de puntuación no es esencial para que el juego funcione inicialmente. El juego puede funcionar sin un sistema de puntuación, por lo que se le asigna una prioridad media.

- **Label:** ```enhancement```
- **Justificación:** El sistema de puntuación es una característica importante del juego que permite al jugador recibir retroalimentación sobre su progreso y rendimiento.


**Historia de Usuario 8: Deteccion de Fin del Juego**

- **Label:** ```medium priority```
- **Justificación:** Aunque es necesaria para cerrar correctamente una partida, el juego puede funcionar temporalmente sin la detección del fin de juego, pero debe implementarse para ofrecer una experiencia completa.

- **Label:** ```enhancement```
- **Justificación:** La detección del fin del juego es una funcionalidad crucial que define el final de una partida, cuando el tablero está lleno de piezas.


## Asignación de puntos de historia

Para asignar puntos de historia a cada una de las historias de usuario del proyecto, tomaremos en cuenta la **complejidad**, el **esfuerzo** requerido y la **incertidumbre**. Utilizaré la **secuencia de Fibonacci** (1, 2, 3, 5, 8, 13, etc.) como referencia, donde:

- **1 punto**: Historia muy simple, poca o ninguna complejidad.
- **2 puntos**: Relativamente sencilla, con poco esfuerzo o complejidad.
- **3 puntos**: Moderada complejidad, requerirá más esfuerzo pero no demasiada incertidumbre.
- **5 puntos**: Historia compleja, con más trabajo y algún nivel de incertidumbre.
- **8 puntos**: Historia con mucha complejidad o incertidumbre, que requerirá un esfuerzo considerable.
- **13 puntos**: Historia muy compleja con alta incertidumbre, probablemente requiera bastante investigación.

**Historia de Usuario 1: Crear Tablero**

- **Puntos de historia :** ```5```
- **Justificación:** La creación del tablero requiere definir una estructura inicial de datos y la lógica básica de renderización. Aunque es esencial, no presenta mucha complejidad técnica, pero puede necesitar iteraciones y pruebas para que funcione bien.

**Historia de Usuario 2: Creacion de Tetrominós**

- **Puntos de historia :** ```8```
- **Justificación:** La creación de tetrominós implica una complejidad considerable y cierto nivel de incertidumbre. Se requiere definir estructuras de datos para representar las diferentes formas de las piezas.

**Historia de Usuario 3: Rotacion de Tetrominós**

- **Puntos de historia :** ```8```
- **Justificación:** La rotación de los tetrominós agrega un nivel significativo de complejidad, ya que debes asegurarte de que las piezas no atraviesen otras piezas o salgan del tablero. Además, la rotación debe funcionar en cualquier posición del tablero, lo que requiere múltiples pruebas y ajustes.


**Historia de Usuario 4: Sistema de caída**

- **Puntos de historia :** ```8```
- **Justificación:** Implementar la caída de los tetrominós implica trabajar con la lógica de la gravedad.

**Historia de Usuario 5: Deteccion de Lineas Completas**

- **Puntos de historia :** ```5```
- **Justificación:** La detección de líneas completas y su eliminación es una funcionalidad fundamental de Tetris. Aunque conceptualmente es simple, se necesita implementar la lógica para detectar la condición de una fila llena y manejar la actualización del tablero correctamente.

**Historia de Usuario 6: Incremento de velocidad de caída**

- **Puntos de historia :** ```5```
- **Justificación:** El incremento de velocidad a medida que el jugador avanza introduce una mayor dificultad técnica. Es necesario sincronizar el aumento progresivo de la velocidad con la caída de los tetrominós sin que afecte la fluidez del juego.

**Historia de Usuario 7: Sistema de Puntuacion**

- **Puntos de historia :** ```3```
- **Justificación:** La implementación del sistema de puntuación es relativamente sencilla comparada con otras funcionalidades. Solo requiere incrementar un contador basado en el número de líneas completadas, pero sigue siendo importante para el juego

**Historia de Usuario 8: Deteccion de Fin del Juego**

- **Puntos de historia :** ```3```
- **Justificación:** Detectar cuándo el tablero está lleno es una tarea de baja complejidad, ya que solo implica revisar si hay bloques en la fila superior. No es particularmente difícil desde el punto de vista técnico


## Asignación de miembros a cada historia de usuario

Nos hemos asignado cada historia de usario de acuerdo a el conocimiento y la capacidad de cada uno, siendo asi la creacion de ramas especificas para cada entidad, en este caso **fallen**, **shapes1** y **punctuation**

- **Crear Tablero** Sergio Gil
- **Crear Tetrominós** Sergio Gil
- **Rotacion de Tetrominós** Sergio Gil
- **Sistema de caída** Carlos Canto
- **Deteccion de Lineas Completas** Kevin Palomino
- **Incremento de velocidad de caída** Carlos Canto
- **Sistema de Puntuacion** Kevin Palomino
- **Deteccion de Fin del Juego** Kevin Palomino

## Configuración de Sprints y reacion del Spring Blacklog

Se introduce **"Sprint"** como el nombre del campo, eligimos **"Iteration"** como el tipo de campo. Mantenmos la duración en una semana

Luego de asginar los puntos de historia estimados y un sprint, y moveremos las historias del Product Backlog al Sprint Backlog para construir nuestro plan.


![Imagen SpringBlacklog](src/Images/SpringBlacklog.png)


Ahora que ya nos asignamos moveremos a la columna In progress para que se de a conocer que ya se esta trabajando esa historia de usuario en dicha rama.

![Imagen in Progress](src/Images/InProgres.png)

Una vez que se termine de trabajar en la historia, es momento de solicitar una revisión.
Si se registrasto código en GitHub, este es el paso donde se haría un pull request para fusionar el código en la rama main. Movemos la historia de In Progress a Review.

Mientras se espera una revisión, se comienza a trabajar en otra historia. Tomamos la
siguiente historia de la parte superior del Sprint Backlog

![Imagen in Review](src/Images/InReview.png)

Nuestro pull request para la historia inicial ha sido aprobado, y el proceso de revisión se ha
completado. Ahora, se mueve la historia **Crear Tablero** de la columna Review a la columna Done.

Hemos completado el trabajo en la segunda y tercera historia y hemos hecho otro pull request. Movemos las historias **Creacion del Tetrominó** y **Rotación de Tetrominós**  de la columna In Progress a la columna Review para solicitar una revisión, mientras que, ya esta en progeso las historias de usuario **Sistema de caída** y **Deteccion de Lineas Completas**

![Imagen Done1](src/Images/Done1.png)

Nuestro pull request para las historias han sido aprobado, y el proceso de revisión se ha
completado. Ahora, se mueve las historias **Creacion del Tetrominó** y **Rotación de Tetrominós** de la columna Review a la columna Done.

Hemos completado el trabajo y hemos hecho otro pull request. Movemos las historias **Sistema de caída** y **Deteccion de Lineas Completas** de la columna In Progress a la columna Review para solicitar una revisión.

![Imagen Done2](src/Images/Done2.png)

Nuestro pull request para la historia inicial ha sido aprobado, y el proceso de revisión se ha
completado. Ahora, se mueve las historias **Sistema de caída** y **Deteccion de Lineas Completas**  de la columna Review a la columna Done.

Movemos la historia **Incremento de velocidad de caída** de la columna Sprint Backlog a la columna In Progress.

![Imagen Done3](src/Images/Done3.png)

Hemos completado el trabajo y hemos hecho otro pull request. Movemos la historia **Incremento de velocidad de caída** de la columna In Progress a la columna Review para solicitar una revisión.

Movemos las historias **Sistema de Puntuacion** y **Deteccion de Fin del Juego** de la columna Sprint Backlog a la columna In Progress.

![Imagen Done4](src/Images/Done4.png)

Nuestro pull request para la historia inicial ha sido aprobado, y el proceso de revisión se ha
completado. Ahora, se mueve las historias **Incremento de velocidad de caída**  de la columna Review a la columna Done.

Hemos completado el trabajo y hemos hecho otro pull request. Movemos las historias **Sistema de Puntuacion** y **Deteccion de Fin del Juego** de la columna In Progress a la columna Review para solicitar una revisión.


![Imagen Done5](src/Images/Done5.png)

Nuestro pull request ha sido aprobado, y el proceso de revisión se ha
completado. Ahora, se mueve las historias **Sistema de Puntuacion** y **Deteccion de Fin del Juego**  de la columna Review a la columna Done.

![Imagen Done6](src/Images/AllDone.png)

## Configuracion del Burndown Char

![Imagen Burndown Char ](src/Images/Statuschart1.png)

Este grafico nos muestra la cantidad de  puntos de historias totales que se le asigno a cada miembro y que perntencen al sprint

## Estructura del proyecto

  Examen_Parcial_CCS2/
  │
  ├── src/
  │   ├── game.py           # Archivo principal del juego
  │   ├── tetromino
  │   │   └── tetromino.py # Definición de las formas de los tetrominós y su rotación
  │   │   └── colors.py # Definición de los colores de los tetrominós
  │   │   └── radown_tetromino.py # Generación de tetrominós aleatorios
  │   │   └── rotation.py # Rotación de tetrominós
  │   │   └── draw.py # Dibujo de tetrominós
  │   ├── board
  │   │   └── board.py          # Lógica del tablero, detección de líneas y gestión de colisiones
  │   ├── punctuation
  │   │   └── score.py          # Gestión del sistema de puntuación y líneas completadas
  │   ├── movimientovelocidad
  │   │   └── movimientovelocidad.py # Movimiento y velocidad de caída de tetrominós
  │   ├── game.py # Lógica del juego
  ├── tests/
  │   ├── features/
  │   │   ├── steps/
  │   │   │   └── test_caida_shapes.py # Test de la caida de los tetrominós
  │   │   │   └── test_rotacion_piezas.py # Test de la rotacion de los tetrominós
  │   │   │   └── test_velocidad_shapes.py # Test de la velocidad de caida de los tetrominós
  │   │   │   └── TestPuntuacion.py # Test de la puntuación
  │   │   └── caida_shapes.feature  # Definicion de la historia de usuario 4
  │   │   └── rotacion_piezas.feature # Definición de la historia de usuario 3
  │   │   └── velocidad_shapes.feature # Definición de la historia de usuario 6
  │   │   └── puntuacion.feature # Definición de la historia de usuario 7
  │
  ├── assets/               # Recursos gráficos o sonidos
  │
  ├── Dockerfile            # Archivo de configuración de Docker
  ├── docker-compose.yml    # Orquestación del servicio Docker
  ├── requirements.txt      # Dependencias del proyecto
  └── README.md             # Descripción del proyecto


## Instalacion

### Clonar el Repositorio

Primero, clona el repositorio a tu máquina local:

```bash
git clone git@github.com:HumbleG0d/Examen_Parcial_CC3S2.git
cd Examen_Parcial_CC3S2
```
### Ejecución en local

Debemos tener instalado python 3.10 o superior, luego instalar las dependencias del proyecto con el siguiente comando:

```bash
pip install -r requirements.txt
```

Luego de instalar las dependencias, se debe ejecutar el siguiente comando para iniciar el juego:

```bash
python game.py
```

### Ejecución con Docker

También puedes ejecutar utilizando Docker. Para esto, necesitas tener Docker instalado en tu máquina.

* Como pygame no se puede ejecutar mediante docker, se debe ejecutar en local , para esto se debe instalar pygame en su maquina.Pero podemos hacer que el contenedor Docker tenga acceso al servidor local X11 para que se pueda visualizar la ventana de pygame:
 
    ```bash
    xhost +local:docker
    ```

* En el directorio , donde se encuentra el archivo `Dockerfile` , ejecute el siguiente comando para construir la imagen: 
    
    ```bash
    docker build -t <name> .
    ```
* Luego de que se termine de construir la imagen, se debe ejecutar el contenedor con el siguiente comando:

    ```bash
    docker run -it --rm --privileged -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix <name>
    ```

* Debe ejecutar el comando en una terminal diferente a la que ejecuta el contenedor, para que pueda interacturar con el contenedor.

* Una vez terminada el uso del contenedor se debe revertir el permiso otorgado a docker:

  ```bash
  xhost -local:docker
  ```

## Reglas de juego

- El juego se inicia con un tablero de 10x20, y se genera un tetrominó aleatorio en la parte superior del tablero.

- El jugador puede mover el tetrominó hacia la izquierda o derecha usando las flechas del teclado.

- El jugador puede rotar el tetrominó usando la tecla de la flecha hacia arriba.

- El jugador puede caer el tetrominó usando la tecla de la flecha hacia abajo.

- El jugador recibe puntos por cada línea que completa, y la velocidad del tetrominó aumenta con cada línea completada.

- El juego termina cuando el tablero está lleno y no hay espacio para colocar más tetrominós.

    ![Gif del juego](src/Images/tetris_gif.gif)

## Monitoreo con Prometheus y Grafana

### Acceso a Prometheus

1. Una vez que todos los contenedores estén corriendo, puedes acceder a la interfaz web de Prometheus en:

    ```
    http://localhost:9090
    ```

    ![Imagen Prometheus](src/Images/Prometheus.jpg)

### Acceso a Grafana

1. También puedes acceder a la interfaz web de Grafana en:

    ```
    http://localhost:3000
    ```
2. Las credenciales de acceso son:
    * Usuario: admin
    * Contraseña: admin

3.  Una vez dentro de Grafana:
    - Ve a la sección de **Configuration** y selecciona **Data Sources**.
    - Agrega **Prometheus** como una fuente de datos usando la siguiente URL para conectarlo:

      ```
      http://prometheus:9090
      ```
4. Crea un dashboard para visualizar las métricas:
    - Ve a **Create** > **Dashboard**.
    - Selecciona **Add a new panel** y en la sección de **Data source**, selecciona **Prometheus**.
    - Escribe una consulta para mostrar una métrica.
    - Guarda el panel y agrégalo a un dashboard.

    ![Imagen Grafana](src/Images/Grafana.jpg)
    
    