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