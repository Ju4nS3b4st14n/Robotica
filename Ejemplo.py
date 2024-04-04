import RPi.GPIO as GPIO
import time

# Definir los pines de control del motor
IN1 = 17  # Puede ser cualquier pin GPIO disponible en tu Raspberry Pi
IN2 = 18  # Puede ser cualquier pin GPIO disponible en tu Raspberry Pi
IN3 = 22  # Puede ser cualquier pin GPIO disponible en tu Raspberry Pi
IN4 = 23  # Puede ser cualquier pin GPIO disponible en tu Raspberry Pi

# Configurar los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Definir la secuencia de control para el motor
# Puedes ajustar esta secuencia según el tipo de motor que estés utilizando
sequence = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

# Función para mover el motor en una dirección específica durante un tiempo determinado
def move_motor(direction, duration):
    steps = len(sequence)
    for _ in range(int(duration / (0.001 * steps))):
        for i in range(steps):
            GPIO.output(IN1, sequence[i][0])
            GPIO.output(IN2, sequence[i][1])
            GPIO.output(IN3, sequence[i][2])
            GPIO.output(IN4, sequence[i][3])
            time.sleep(0.001)

# Mover el motor en una dirección durante 5 segundos (por ejemplo, en sentido horario)
move_motor(direction="clockwise", duration=5)

# Detener el motor
GPIO.output(IN1, 0)
GPIO.output(IN2, 0)
GPIO.output(IN3, 0)
GPIO.output(IN4, 0)

# Limpiar los pines GPIO
GPIO.cleanup()
