## Índice
1. [Descripción del problema](#descripción-del-problema)
2. [Descripción de la solución](#descripción-de-la-solución)
3. [Cómo ejecutar el programa](#cómo-ejecutar-el-programa)
4. [Video explicativo](#video-explicativo)
5. [Coevaluación](#coevaluación)
## Descripción del problema
***
El Sudoku es un antiguo juego de lógica y matemática inventado inicialmente por el matemático Leonhard Euler en 1783, y popularizado a finales de la década de 1970 por Walter MacKey, aunque no llegó a ser reconocido mundialmente hasta principio de los 2000. En su versión más clásica consta de una cuadrícula de 81 casillas (9x9), dividido en 9 subcuadrículas de 9 casillas cada una (3x3), El puzle comienza con la cuadrícula parcialmente rellenada con algunos números del 1 al 9 que funcionan como "pistas" para lograr encontrar los números que van en las casillas en blanco. El objetivo es rellenar todas las casillas con los números del 1 al 9, de tal manera que cada número aparezca una sola vez por fila, columna y subcuadrícula de 3x3.

A pesar de que el Sudoku posee unas reglas bastante simples, no se debe subestimar su complejidad de resolución, sobre todo cuando se juega en niveles más difíciles, pues la cantidad de posibles acciones a realizar luego de cada número escrito es muy amplia, además de que cada decisión puede llevar a resultados muy distintos, y que pueden o no estar completamente errados. Es por esto que la resolución de un Sudoku es visto en el área de las matemáticas como un problema combinatorio de satisfacción de restricciones, y que necesita de un metódico razonamiento para lograr llegar a su solución final, la cual suele ser única si está lo suficientemente bien hecho. Es por esto que las mejores técnicas de resolución de un Sudoku siempre apuntan a priorizar unas casillas sobre otras, siendo la heurística más común el avanzar por las casillas que tengan la menor cantidad de opciones posibles.

El desafío planteado para la resolución de este problema es la creación de un programa funcional, capaz de encontrar la solución de un sudoku dado haciendo uso de grafos implícitos y árboles de búsqueda para iterar entre las distintas posibilidades y caminos de su resolución. Además de implementar diferentes heurísticas en el proceso para optimizar los resultados, logrando llegar a un estado final en la menor cantidad de iteraciones posibles.
## Descripción de la solución
***
Inicialmente, para la resolución de este problema se optó por construir el programa en base al algoritmo de **Búsqueda en Profundidad** (o DFS), pues en este caso en específico se busca encontrar el estado final del puzle rápidamente, sin importar por los estados que pase antes.

En este contexto, se definió el Sudoku como una matriz de 9x9, cuyo estado inicial se constituye por la matriz parcialmente rellena con los números de un sudoku dado, representando los espacios en blanco con un 0. Por su parte, una acción fue definida como el número que se pondrá en la siguiente casilla en blanco, y la transición entonces, es el poner dicho número en su casilla asignada. Otras definiciones importantes son el estado válido y el estado final. El estado válido se refiere a un estado en donde no existan repeticiones de dígitos dentro de las filas, columnas y cuadrados de 3x3, y el estado final se define como un estado válido donde no haya casillas en 0.

Para el funcionamiento de este primer algoritmo de búsqueda utilizado se crearon funciones asociadas a la validación de el número que se está intentando poner en una casilla. La función de validación principal es `number_is_valid`, la cual utiliza a su vez 3 funciones más que chequean la factibilidad del número dentro de su fila `(check_row)`, columna `(check_col)` y cuadrado de 3x3 `(check_square)`.

Este algoritmo inicial funciona con lo llamado “fuerza bruta”, pues va buscando sucesivamente por todas las opciones posibles de cada estado, haciendo uso del *Back Tracking* cada vez que un camino llevaba a un estado invalido (donde no se pueden agregar más números sin que se repitan).

Para lograr optimizar este algoritmo, se optó primero por implementar una heurística en la definición de las acciones, describiéndolas ahora como un número a poner en la siguiente casilla con más restricciones, logrando así descartar posibles estados que no aseguraban encontrar la solución. Para esto se implementó una nueva función llamada `find_best_point`, que busca y cuenta las restricciones de cada casilla, retornando la que tenga la mayor cantidad.

Con este cambio se logró reducir enormemente la cantidad de iteraciones por Sudoku, sin embargo, los resultados se podían mejorar, por lo que se continuó probando con el algoritmo **Best First**, implementando la cola con prioridad y la función heurística asociada a ella.

En esta función, llamada `heuristic_eval`, se evalúan las casillas disponibles según su cantidad de restricciones, siendo mejor evaluadas aquellas casillas que tenían una mayor cantidad de estas (es decir, un menor número de valores posibles).

Gracias al uso de este algoritmo y su función heurística, se logró llegar a una menor cantidad de iteraciones en sudokus de niveles superiores.

## Cómo ejecutar el programa
***
Para poder probar el código es necesario abrir como proyecto la carpeta ```Desafio 1``` en un compilador compatible con Python. De esta forma el programa podrá abrir las instancias de Sudoku guardadas como ```txt``` en una carpeta vecina.

Nuestro proyecto dispone en total de 46 instancias de Sudoku para probar, las cuales están ordenadas por dificultad. Cada una está identificada con un número en el nombre del archivo, partiendo desde la ```s01``` hasta la ```s16```. Además, cada instancia contempla 3 versiones en donde varía el estado inicial, aumentando ligeramente la dificultad. Esto está denotado con las letras ```a```, ```b``` y ```c``` al final del nombre de los archivos, siendo la versión con letra ```a``` la más fácil y la versión con letra ```c``` la más difícil.

Por último, para cambiar de archivo de instancia se debe cambiar el nombre del archivo en la línea de código número 19, dentro del llamado a la función ```open```.
## Video explicativo
***
Para una mejor comprensión del problema y su resolución, se adjunta un video explicativo en el siguiente [link](https://www.youtube.com/watch?app=desktop&v=q4rLmbqxn9M&feature=youtu.be).
## Coevaluación
***
A continuación, tablas de coevaluación según estos criterios: [Criterios de coevaluación](https://docs.google.com/document/d/1YSba-KNP-ReP_TJePQkCHXJ1x4_MtOizQPIrNnriZbw/edit#)
1. **Asistencia y puntualidad**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | | | | |
| Carlos Núñez        |+| |+|+|
| Priscilla Riffo     | | | | |
| Katherine Sepúlveda |+|+|+| |
2. **Integración**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | | | | |
| Carlos Núñez        |+| |+|+|
| Priscilla Riffo     | | | | |
| Katherine Sepúlveda |+|+|+| |
3. **Responsabilidad**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | | | | |
| Carlos Núñez        |+| |+|+|
| Priscilla Riffo     | | | | |
| Katherine Sepúlveda |+|+|+| |
4. **Contribución**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | | | | |
| Carlos Núñez        |+| |+|+|
| Priscilla Riffo     | | | | |
| Katherine Sepúlveda |+|+|+| |
5. **Resolución de conflictos**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | | | | |
| Carlos Núñez        |+| |+|+|
| Priscilla Riffo     | | | | |
| Katherine Sepúlveda |+|+|+| |
