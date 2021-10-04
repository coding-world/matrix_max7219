import RPi.GPIO as gpio
import time
from MyMax7219 import MyMatrix
from random import randint
from highscore import updateScore
global apfel, snake

gpio.setmode(gpio.BCM)
taster = [14,15,18,23]
matrixe = 2
matrix = MyMatrix(cascaded=matrixe)
height = 7
width = (8*matrixe)-1

def steuerung(gpio):
  print('steuerung')
  print(gpio)
  global richtung
  if(gpio == 14):  #rechts
    richtung = [1,0]
  elif(gpio == 15): #oben
    richtung = [0,-1]
  elif(gpio == 18): #unten
     richtung = [0,1]
  elif(gpio == 23): #links
    richtung = [-1,0]

for i in taster:
  gpio.setup(i,gpio.IN,pull_up_down=gpio.PUD_UP)
  gpio.add_event_detect(i, gpio.FALLING, 
  callback=steuerung)
def startSpiel():
  global snake, richtung, apfel
  snake = [[randint(3,width-4),randint(3,height-4)]]
  richtung = [0,0]
  while richtung == [0,0]:
    matrix.showMessage("READY")
  neuerApfel()

def neuerApfel():
  global apfel, snake
  apfelSnake = False
  while apfelSnake == False:
    apfelSnake = True
    apfel = [randint(0,width),randint(0,height)]
    for i in snake:
      if(i == apfel):
        apfelSnake = False
  print(apfel)

def endOfGame():
  for i in range(0,2):
    matrix.clear()
    for i in range(0,width+1):
      for j in range(0,height+1):
        matrix.pixel(i,j,1)
        time.sleep(0.001)
    time.sleep(0.01)
  matrix.showMessage("GAME OVER")
  punkte = len(snake)-1
  matrix.showMessage(str(punkte)+" PUNKTE")
  ranking = updateScore(punkte)
  matrix.showMessage(str(ranking))

  startSpiel()

startSpiel()

while True:
  keinePause = False
  newSnake = [snake[0][0]+richtung[0],
              snake[0][1]+richtung[1]]
  for i in snake:
    if(i == newSnake):
      endOfGame()
      pass

  if(newSnake == apfel):
     neuerApfel()
     keinePause = True
  else:
     snake.pop()
  snake.insert(0,newSnake)

  if(snake[0][0] > width or snake[0][1] > height
    or snake[0][0] < 0 or snake[0][1] < 0 ):
    endOfGame()
    pass

  matrix.clear()
  for i in snake:
    matrix.pixel(i[0],i[1], 1)
  matrix.pixel(apfel[0],apfel[1],1)
  if(keinePause == False):
    newLength = (len(snake)-2)*0.01
    time.sleep(0.3-newLength)
  else:
    time.sleep(0.3)
