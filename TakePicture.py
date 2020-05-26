from picamera import PiCamera
from time import sleep
import os
import datetime
import sys

Path_arg = sys.argv[1]

path = Path_arg

dt = datetime.datetime.now()
title = dt.strftime("%Y%m%d%H%M%S")
#print(title)
camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture(path +'/' + title +'.jpg')
camera.stop_preview()
