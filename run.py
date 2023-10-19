# Search methods

import search, time

# A -> B
ab = search.GPSProblem('A', 'B', search.romania)
print("\n\t\t---- [A -> B] ----")
inicio = time.time()
print("\n\t-Amplitud-")
print("Ruta: " + str(search.breadth_first_graph_search(ab).path()))
print("Tiempo de ejecución Amplitud: " + str(time.time() - inicio))
inicio = time.time()

print("\n\t-Profundidad-")
print("Ruta: " + str(search.depth_first_graph_search(ab).path()))
print("Tiempo de ejecución Profundidad: " + str(time.time() - inicio))

# O -> E
oe = search.GPSProblem('O', 'E', search.romania)
print("\n\t\t---- [O -> E] ----")
inicio = time.time()
print("\n\t-Amplitud-")
print("Ruta: " + str(search.breadth_first_graph_search(oe).path()))
print("Tiempo de ejecución Amplitud: " + str(time.time() - inicio))
inicio = time.time()

print("\n\t-Profundidad-")
print("Ruta: " + str(search.depth_first_graph_search(oe).path()))
print("Tiempo de ejecución Profundidad: " + str(time.time() - inicio))

# G -> Z
gz = search.GPSProblem('G', 'Z', search.romania)
print("\n\t\t---- [G -> Z] ----")
inicio = time.time()
print("\n\t-Amplitud-")
print("Ruta: " + str(search.breadth_first_graph_search(gz).path()))
print("Tiempo de ejecución Amplitud: " + str(time.time() - inicio))
inicio = time.time()

print("\n\t-Profundidad-")
print("Ruta: " + str(search.depth_first_graph_search(gz).path()))
print("Tiempo de ejecución Profundidad: " + str(time.time() - inicio))

# N -> D
nd = search.GPSProblem('N', 'D', search.romania)
print("\n\t\t---- [N -> D] ----")
inicio = time.time()
print("\n\t-Amplitud-")
print("Ruta: " + str(search.breadth_first_graph_search(nd).path()))
print("Tiempo de ejecución Amplitud: " + str(time.time() - inicio))
inicio = time.time()

print("\n\t-Profundidad-")
print("Ruta: " + str(search.depth_first_graph_search(nd).path()))
print("Tiempo de ejecución Profundidad: " + str(time.time() - inicio))

# M -> F
mf = search.GPSProblem('M', 'F', search.romania)
print("\n\t\t---- [M -> F] ----")
inicio = time.time()
print("\n\t-Amplitud-")
print("Ruta: " + str(search.breadth_first_graph_search(mf).path()))
print("Tiempo de ejecución Amplitud: " + str(time.time() - inicio))
inicio = time.time()

print("\n\t-Profundidad-")
print("Ruta: " + str(search.depth_first_graph_search(mf).path()))
print("Tiempo de ejecución Profundidad: " + str(time.time() - inicio))

