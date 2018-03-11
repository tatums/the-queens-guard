from time import sleep
import RPi.GPIO as GPIO
from datetime import datetime
import lib.store

GPIO.setmode(GPIO.BOARD)
button1=16
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)


def DoorIsOpen():
  return GPIO.input(button1)==1

while(1):
  if DoorIsOpen():
    event = datetime.utcnow()
    dateString = event.isoformat()
    year = event.strftime("%Y")
    month = event.strftime("%m")
    day = event.strftime("%d")
    time = event.strftime("%H:%M:%S")
    lib.store.save(dateString, year, month, day, time)

    while DoorIsOpen() == True:
      sleep(.2)
  sleep(.2)
