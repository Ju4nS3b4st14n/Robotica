import time
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685

# Configurar la comunicación I2C
i2c = busio.I2C(SCL, SDA)

# Crear una instancia del objeto PCA9685
pca = PCA9685(i2c)

# Establecer la frecuencia del reloj en Hz (por defecto es 50Hz)
pca.frequency = 60

# Función para mover un servo a una posición específica
def move_servo(channel, angle):
    # Convertir el ángulo deseado (0-180) a un valor de pulso (150-600)
    pulse = int(2.5 + angle / 180 * 20)  # Fórmula aproximada para el cálculo del pulso
    pca.channels[channel].duty_cycle = int(pulse / 20 * 65535)  # Escalar el valor de pulso al rango de 0-65535

# Mover el servo conectado al canal 0 a 0 grados
move_servo(channel=0, angle=0)
time.sleep(1)

# Mover el servo conectado al canal 0 a 180 grados
move_servo(channel=0, angle=180)
time.sleep(1)

# Detener el movimiento del servo
move_servo(channel=0, angle=90)

# Puedes ajustar los valores de los canales y los ángulos según tus necesidades
