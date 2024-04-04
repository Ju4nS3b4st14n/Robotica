import RPi.GPIO as GPIO
import time

# Definir los pines de control del motor
IN1 = 13  # Puede ser cualquier pin GPIO disponible en tu Raspberry Pi
IN2 = 6  # Puede ser cualquier pin GPIO disponible en tu Raspberry Pi
IN3 = 5  # Puede ser cualquier pin GPIO disponible en tu Raspberry Pi
IN4 = 12  # Puede ser cualquier pin GPIO disponible en tu Raspberry Pi

# Configurar los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Definir la secuencia de control para el motor
sequence = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

# Función para mover el motor una cantidad específica de vueltas
def move_motor_vueltas(direction, vueltas):
    pasos_por_vuelta = 360 / 7.5  # Cada vuelta son 360 grados y el motor tiene una resolución de 7.5° por paso
    pasos_totales = pasos_por_vuelta * vueltas
    
    for _ in range(int(pasos_totales)):
        for i in range(len(sequence)):
            GPIO.output(IN1, sequence[i][0])
            GPIO.output(IN2, sequence[i][1])
            GPIO.output(IN3, sequence[i][2])
            GPIO.output(IN4, sequence[i][3])
            time.sleep(0.01)  # Ajusta el tiempo de espera según la velocidad del motor

# Mover el motor en sentido horario durante 10 vueltas
move_motor_vueltas(direction="clockwise", vueltas=10)

# Detener el motor
GPIO.output(IN1, 0)
GPIO.output(IN2, 0)
GPIO.output(IN3, 0)
GPIO.output(IN4, 0)

# Limpiar los pines GPIO
GPIO.cleanup()
