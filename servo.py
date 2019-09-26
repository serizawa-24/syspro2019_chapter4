import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

def setservo(rand):
	angle=((0.01*(rand+90.0))+0.5)*5.0
	servo.ChangeDutyCycle(angle)
	time.sleep(1.0)

setservo(90.0)
setservo(-90.0)

GPIO.cleanup()
