mport RPi.GPIO as GPIO
import sys
from time import sleep

class MotorControl:
    def _init_(self):
        self.selected_motor = None

    def move_motor(self, motor_id, angle):
        if motor_id not in ["1", "2"]:
            self.selected_motor = None
            return
        if motor_id == "1":
            self.selected_motor = 19
        elif motor_id == "2":
            self.selected_motor = 16

        if self.selected_motor is not None:
            self.move_servo(self.selected_motor, angle)

    def move_servo(self, servo_pin, angle):
        if servo_pin is None:
            return
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(servo_pin, GPIO.OUT)
        pulso = GPIO.PWM(servo_pin, 50)
        pulso.start(1.5)
        
        for i in range(0, angle):
            grados = ((1.0/18.0) * i) + 2.5
            pulso.ChangeDutyCycle(grados)
            sleep(0.05)  # Agregar un pequeño retardo entre cada movimiento
        sleep(2)
        pulso.stop()
        GPIO.cleanup()

if _name_ == "_main_":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    control = MotorControl()
    motor_id = input("Enter motor ID (1 or 2): ")
    angle = int(input("Enter angle: "))
    control.move_motor(motor_id, angle)
