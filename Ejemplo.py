from gpiozero import DistanceSensor
import time

# Configurar el sensor de ultrasonido en los pines GPIO específicos
sensor = DistanceSensor(echo=18, trigger=17)

try:
    while True:
        # Leer la distancia medida por el sensor
        distancia = sensor.distance
        print(f"Distancia: {distancia} metros")

        # Esperar un breve tiempo antes de tomar otra lectura
        time.sleep(1)

except KeyboardInterrupt:
    print("Lectura del sensor detenida por el usuario")
