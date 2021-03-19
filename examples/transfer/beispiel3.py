import RPi.GPIO as gpio
from MyMax7219 import MyMatrix
from random import randint
import time

matrix = MyMatrix()

while True:
  for i in range(8):
    for j in range(8):
      matrix.pixel(i,j,randint(0,1))
      time.sleep(0.0002)