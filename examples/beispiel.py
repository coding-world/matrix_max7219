from MyMax7219 import MyMatrix
from random import randint
import time

matrix = MyMatrix()

matrix.showMessage('MOIN')

for i in range(9):
    matrix.letter(str(9-i))
    time.sleep(0.2)

matrix.clear()
time.sleep(0.2)

for i in range(8):
    for j in range(8):
        matrix.pixel(j,i,1)
        time.sleep(0.02)
    time.sleep(0.1)

for i in range(0,250,20):
    matrix.brightness(i)
    time.sleep(0.2)

matrix.clear()
time.sleep(0.2)

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(len(abc)):
    matrix.letter(abc[i])
    time.sleep(0.2)

while True:
  for i in range(8):
    for j in range(8):
      matrix.pixel(i,j,randint(0,1))
      time.sleep(0.0002)