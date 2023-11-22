# ALGORITMO DE BÚSQUEDA

Mapa de Rumanía con los costes entre ciudades

![Mapa de Rumania para práctica](./mapa.png)

En el proyecto debemos encontrar las rutas mas cortas entre las diferentes ciudades

## MÉTODOS USADOS

1. DFS (Depth First Graph Search): Con este método vamos añadiendo los diferentes nodos a una pila y comprobando si el nodo es el objetivo, si no lo es añadimos los nuevos nodos al principio de la pila.

2. BFS (Breath First Graph Search): Con este método añadimos los nodos a una cola usando FIFO y comprobando si este es el objetivo, si no lo es seguimos añadiendo al final de la cola.

3. Ramificación y acotación (Branch & Bound): Con Branch & Bound añadiremos los nodos de uno a uno en una lista e iremos comprobando si es el objetivo, sino pasaremos al siguiente y cuando lo encontremos ordenaremos la lista en base al coste acumulado.

4. Ramificación y acotación con subestimación (Branch and Bound ): Con este método vamos añadiendo a una lista los diferentes nodos y comprobando si este es el nodo objetivo, sino pasamos al siguiente y al final ordenamos la lista de mejor a peor según el coste acumulado y la heurística.

## ARCHIVOS

[run.py](./run.py) → Aquí se encuentran las diferentes pruebas y los Output.

[search.py](./search.py) → Aquí es donde se encuentra el programa principal y donde se realizaran todos los métodos, también se encuentran los valores de las diferentes ciudades.

[utils.py](./utils.py) → En este archivo es donde se crean los metodos para las pilas, colas... que usaremos para los DFS y BFS.

## TESTS

- Resultados esperados:

| ID  | Origen  | Destino   | Amplitud                                                                                                                            | Profundidad                                                                                                                                                                  | Ramificación y acotación                                                                                                            | Ramificación y acotación con subestimación                                                                                          |
| --- | ------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Arad    | Bucharest | **Generados:** 21 **Visitados:** 16 **Costo total:** 450 **Ruta:** [Node B, Node F, Node S, Node A]                                 | **Generados:** 18 **Visitados:** 10 **Costo total:** 733 **Ruta:** [Node B, Node P, Node C, Node D, Node M, Node L, Node T, Node A]                                          | **Generados:** 31 **Visitados:** 24 **Costo total:** 418 **Ruta:** [Node B, Node F, Node R, Node S, Node A]                         | **Generados:** 5 **Visitados:** 16 **Costo total:** 418 **Ruta:** [Node B, Node F, Node R, Node S, Node A]                          |
| 2   | Oradea  | Eforie    | **Generados:** 45 **Visitados:** 43 **Costo total:** 730 **Ruta:** [Node E, Node H, Node U, Node B, Node F, Node S, Node O]         | **Generados:** 41 **Visitados:** 31 **Costo total:** 698 **Ruta:** [Node E, Node H, Node U, Node B, Node P, Node R, Node S, Node O]                                          | **Generados:** 43 **Visitados:** 40 **Costo total:** 698 **Ruta:** [Node E, Node H, Node U, Node B, Node P, Node R, Node S, Node O] | **Generados:** 32 **Visitados:** 15 **Costo total:** 698 **Ruta:** [Node E, Node H, Node U, Node B, Node P, Node R, Node S, Node O] |
| 3   | Giurgiu | Zerind    | **Generados:** 41 **Visitados:** 34 **Costo total:** 615 **Ruta:** [Node Z, Node A, Node S, Node F, Node B, Node G]                 | **Generados:** 32 **Visitados:** 21 **Costo total:** 1284 **Ruta:** [Node Z, Node A, Node T, Node L, Node M, Node D, Node C, Node P, Node R, Node S, Node F, Node B, Node G] | **Generados:** 41 **Visitados:** 35 **Costo total:** 583 **Ruta:** [Node Z, Node A, Node S, Node R, Node P, Node B, Node G]         | **Generados:** 26 **Visitados:** 12 **Costo total:** 583 **Ruta:** [Node Z, Node A, Node S, Node R, Node P, Node B, Node G]         |
| 4   | Neamt   | Dobreta   | **Generados:** 32 **Visitados:** 26 **Costo total:** 765 **Ruta:** [Node D, Node C, Node P, Node B, Node U, Node V, Node I, Node N] | **Generados:** 31 **Visitados:** 19 **Costo total:** 1151 **Ruta:** [Node D, Node C, Node P, Node R, Node S, Node F, Node B, Node U, Node V, Node I, Node N]                 | **Generados:** 32 **Visitados:** 26 **Costo total:** 765 **Ruta:** [Node D, Node C, Node P, Node B, Node U, Node V, Node I, Node N] | **Generados:** 23 **Visitados:** 12 **Costo total:** 765 **Ruta:** [Node D, Node C, Node P, Node B, Node U, Node V, Node I, Node N] |
| 5   | Mehadia | Faragas   | **Generados:** 31 **Visitados:** 23 **Costo total:** 520 **Ruta:** [Node F, Node S, Node R, Node C, Node D, Node M]                 | **Generados:** 29 **Visitados:** 18 **Costo total:** 928 **Ruta:** [Node F, Node B, Node P, Node R, Node S, Node A, Node T, Node L, Node M]                                  | **Generados:** 36 **Visitados:** 27 **Costo total:** 520 **Ruta:** [Node F, Node S, Node R, Node C, Node D, Node M]                 | **Generados:** 25 **Visitados:** 16 **Costo total:** 520 **Ruta:** [Node F, Node S, Node R, Node C, Node D, Node M]                 |

- Resultados obtenidos:

| ID  | Origen  | Destino   |                                                                                        Amplitud                                                                                         |     |                                                                                                         Profundidad                                                                                                          |     |                                                                              Ramificación y acotación                                                                              |     |                                                                     Ramificación y acotación con subestimación                                                                      |     |
| --- | ------- | --------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-: |
| 1   | Arad    | Bucharest |                 **Generados:** 21 **Visitados:** 16 **Costo total:** 450 **Ruta:** [Node B, Node F, Node S, Node A] Tiempo de ejecución Amplitud: 9.179115295410156e-05                 | ✅  |                     **Generados:** 18 **Visitados:** 10 **Costo total:** 733 **Ruta:** [Node B, Node P, Node C, Node D, Node M, Node L, Node T, Node A] **Tiempo de ejecución:** 4.8160552978515625e-05                      | ✅  |             **Generados:** 31 **Visitados:** 24 **Costo total:** 418 **Ruta:** [Node B, Node P, Node R, Node S, Node A] **Tiempo de ejecución:** 8.487701416015625e-05             | ✅  |              **Generados:** 16 **Visitados:** 6 **Costo total:** 418 **Ruta:** [Node B, Node P, Node R, Node S, Node A] **Tiempo de ejecución:** 6.818771362304688e-05              | ✅  |
| 2   | Oradea  | Eforie    |     **Generados:** 45 **Visitados:** 43 **Costo total:** 730 **Ruta:** [Node E, Node H, Node U, Node B, Node F, Node S, Node O] Tiempo de ejecución Amplitud: 0.0009579658508300781     | ✅  |                      **Generados:** 41 **Visitados:** 31 **Costo total:** 698 **Ruta:** [Node E, Node H, Node U, Node B, Node P, Node R, Node S, Node O] **Tiempo de ejecución:** 8.296966552734375e-05                      | ✅  |  **Generados:** 43 **Visitados:** 40 **Costo total:** 698 **Ruta:** [Node E, Node H, Node U, Node B, Node P, Node R, Node S, Node O] **Tiempo de ejecución:** 9.918212890625e-05   | ✅  | **Generados:** 32 **Visitados:** 15 **Costo total:** 698 **Ruta:** [Node E, Node H, Node U, Node B, Node P, Node R, Node S, Node O] **Tiempo de ejecución:** 0.00013065338134765625 | ✅  |
| 3   | Giurgiu | Zerind    |         **Generados:** 41 **Visitados:** 34 **Costo total:** 615 **Ruta:** [Node Z, Node A, Node S, Node F, Node B, Node G] Tiempo de ejecución Amplitud: 8.487701416015625e-05         | ✅  | **Generados:** 32 **Visitados:** 21 **Costo total:** 1284 **Ruta:** [Node Z, Node A, Node T, Node L, Node M, Node D, Node C, Node P, Node R, Node S, Node F, Node B, Node G] **Tiempo de ejecución:** 0.00027108192443847656 | ✅  |    **Generados:** 41 **Visitados:** 34 **Costo total:** 583 **Ruta:** [Node Z, Node A, Node S, Node R, Node P, Node B, Node G] **Tiempo de ejecución:** 0.00010991096496582031     | ✅  |     **Generados:** 26 **Visitados:** 12 **Costo total:** 583 **Ruta:** [Node Z, Node A, Node S, Node R, Node P, Node B, Node G] **Tiempo de ejecución:** 0.00010180473327636719     | ✅  |
| 4   | Neamt   | Dobreta   | **Generados:** 32 **Visitados:** 26 **Costo total:** 765 **Ruta:** [Node D, Node C, Node P, Node B, Node U, Node V, Node I, Node N] Tiempo de ejecución Amplitud: 7.200241088867188e-05 | ✅  |         **Generados:** 31 **Visitados:** 19 **Costo total:** 1151 **Ruta:** [Node D, Node C, Node P, Node R, Node S, Node F, Node B, Node U, Node V, Node I, Node N] **Tiempo de ejecución:** 6.008148193359375e-05          | ✅  | **Generados:** 32 **Visitados:** 26 **Costo total:** 765 **Ruta:** [Node D, Node C, Node P, Node B, Node U, Node V, Node I, Node N] **Tiempo de ejecución:** 0.0002498626708984375 | ✅  | **Generados:** 23 **Visitados:** 12 **Costo total:** 765 **Ruta:** [Node D, Node C, Node P, Node B, Node U, Node V, Node I, Node N] **Tiempo de ejecución:** 0.00019407272338867188 | ✅  |
| 5   | Mehadia | Faragas   |        **Generados:** 31 **Visitados:** 23 **Costo total:** 520 **Ruta:** [Node F, Node S, Node R, Node C, Node D, Node M] Tiempo de ejecución Amplitud: 0.00019407272338867188         | ✅  |                 **Generados:** 29 **Visitados:** 18 **Costo total:** 928 **Ruta:** [Node F, Node B, Node P, Node R, Node S, Node A, Node T, Node L, Node M] **Tiempo de ejecución:** 0.00014162063598632812                  | ✅  |         **Generados:** 36 **Visitados:** 27 **Costo total:** 520 **Ruta:** [Node F, Node S, Node R, Node C, Node D, Node M] **Tiempo de ejecución:** 0.0001461505889892578         | ✅  |         **Generados:** 25 **Visitados:** 16 **Costo total:** 520 **Ruta:** [Node F, Node S, Node R, Node C, Node D, Node M] **Tiempo de ejecución:** 0.00014781951904296875         | ✅  |
