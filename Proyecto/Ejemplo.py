import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear datos de ejemplo para la trayectoria
# Aquí asumiré que tienes una lista de coordenadas (x, y, z)
# Deberás reemplazar esto con tus propios datos de trayectoria.
trayectoria_x = [0, 1, 2, 3, 4]
trayectoria_y = [0, 1, 2, 1, 0]
trayectoria_z = [0, 0, 0, 0, 0]

# Crear la figura y el subplot en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la trayectoria con puntos
ax.scatter(trayectoria_x, trayectoria_y, trayectoria_z, c='b', marker='o')  # 'b' representa color azul, 'o' representa círculos

# Establecer etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar la figura
plt.show()
