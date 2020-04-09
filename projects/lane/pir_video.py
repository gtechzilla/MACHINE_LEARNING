import RPi.GPIO as GPIO
import time
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)

pirPin = 7
GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)
camera = PiCamera()
counter = 1

while True:
    if GPIO.input(pirPin) == GPIO.LOW:
        try: 
            camera.start_preview()
            <strong>camera.start_recording('/home/pi/video%s.h264' % counter)</strong>
            counter = counter + 1
            <strong>time.sleep(5)</strong>
            <strong>camera.stop_recording()</strong>
            camera.stop_preview()
        except:
            camera.stop_preview()
    time.sleep(3)
