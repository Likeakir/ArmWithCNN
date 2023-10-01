from pyfirmata import Arduino, SERVO
from time import sleep

port = '/dev/cu.usbserial-10'
board = Arduino(port)


board.digital[2].mode = SERVO
servo1 = board.digital[2]

def rotate_servo(servo, angle):
    servo.write(angle)
    sleep(0.015)
while True:
    for i in range(0,180):
         rotate_servo(servo1, i)
    for i in range(190,1,-1):
         rotate_servo(servo1, i)