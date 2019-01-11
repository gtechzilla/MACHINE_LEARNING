import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(4, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(14, GPIO.OUT)         #LED output pin
while True:
	i=GPIO.input(4)
		if i==0:                 #When output from motion sensor is LOW
			print "No intruders",i
