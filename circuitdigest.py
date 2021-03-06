

import RPi.GPIO as gpio
import picamera
import time


led=17
pir=18
HIGH=1
LOW=0
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(led, gpio.OUT)            # initialize GPIO Pin as outputs
gpio.setup(pir, gpio.IN)            # initialize GPIO Pin as input
data=""

def capture_image():
    data= time.strftime("%d_%b_%Y|%H:%M:%S")
    camera.start_preview()
    time.sleep(2)
    print ("motiondetected")
    camera.capture('%s.jpg'%data)
    camera.stop_preview()
    time.sleep(1)
    

gpio.output(led , 0)
camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55
while 1:
    if gpio.input(pir)==1:
        gpio.output(led, HIGH)
        capture_image()
        while(gpio.input(pir)==1):
            time.sleep(1)
        
    else:
        gpio.output(led, LOW)
        time.sleep(0.01)
