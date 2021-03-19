import RPi.GPIO as gpio
from MyMax7219 import MyMatrix
from random import randint
import time

gpio.setmode(gpio.BCM)
taster = 23
gpio.setup(taster,gpio.IN,pull_up_down=gpio.PUD_UP)
matrix = MyMatrix()

def neue_zahl(channel):
  matrix.letter(str(randint(1,6)))

gpio.add_event_detect(taster, gpio.RISING,
        callback=neue_zahl)

matrix.letter("?")

while True:
  time.sleep(0.01)