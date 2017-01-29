#pilapse

import time
import picamera
from time import strftime, gmtime

def getCurrentTime():
	tyme = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
	return str(tyme)

camera = picamera.PiCamera()

camera.capture('image.jpg')

print "your picture is done"
print "the current time is %s " % (getCurrentTime())

piTime = getCurrentTime()[16:22]

print piTime


