#pilapse

import time
import picamera
from time import strftime, gmtime

tyme = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
camera = picamera.PiCamera()

camera.capture('image.jpg')

print "your picture is done"
print "the current time is " + str(tyme)

piTime = tyme[16:22]

print piTime
