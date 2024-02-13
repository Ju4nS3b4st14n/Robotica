print("Hola mundo '2024'")

import numpy as np

# Vectores previamente inicializados
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Suma de vectores
suma = vector1 + vector2

# Resta de vectores
resta = vector1 - vector2

# Producto punto
producto_punto = np.dot(vector1, vector2)

# Producto cruz
producto_cruz = np.cross(vector1, vector2)

# División de vectores elemento a elemento
division = vector1 / vector2

print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("Suma:", suma)
print("Resta:", resta)
print("Producto punto:", producto_punto)
print("Producto cruz:", producto_cruz)
print("División:", division)

#a.2 
import numpy as np

# Matrices previamente inicializadas
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])

# Suma de matrices
suma = matriz1 + matriz2

# Resta de matrices
resta = matriz1 - matriz2

# Producto punto
producto_punto = np.dot(matriz1.flatten(), matriz2.flatten())

# Producto cruz
# No está definida la operación de producto cruz para matrices en numpy

# División de matrices elemento a elemento
division = matriz1 / matriz2

print("Matriz 1:\n", matriz1)
print("Matriz 2:\n", matriz2)
print("Suma:\n", suma)
print("Resta:\n", resta)
print("Producto punto:", producto_punto)
print("División:\n", division)