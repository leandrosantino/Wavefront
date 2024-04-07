import os
import time
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


initialPoint = (0, 0)
def propagate(world:list, points: list[list], coords: tuple[int, int] = None):
  global initialPoint

  if(coords):
    x, y = coords

    current_value = world[x][y]
    initialPoint = (x, y)

    next_points = getCircularPoints(x, y)

    for x, y in next_points:
      if(verifyPosition(world, (x, y))):
        world[x][y] = current_value + 1
    
    printVec(world)
    
    propagate(world, next_points)
    return

  if(len(points)>0):

    p = []

    for x, y in points:
      current_value = 0
      try:
        current_value = world[x][y]
      except IndexError:
        continue

      next_points = getCircularPoints(x, y)

      for x3, y3 in next_points:
        if(verifyPosition(world, (x3, y3))):
          p.append((x3, y3))
          world[x3][y3] = current_value + 1
          
    printVec(world)
    
    propagate(world, p)
    return
  


def verifyPosition(world:list, coords: tuple[int, int]):
  global initialPoint
  try:
    x, y = coords
    if(x<0 or y<0): return False
    if(world[x][y] > 0): return False
    if(world[x][y] < 0): return False
    if(coords == initialPoint): return False
    return True
  except IndexError:
    return False
  

def printVec(vec: list[int]):
  colorama_init()
  time.sleep(1)
  os.system('cls')
  print()
  for i in vec:
    for a in i:
      if a == -1:
        print('()'.center(4, ' '),  end='')
        continue
      if a == 0: 
        print(f'{str(a).center(4, " ")}', end='',)
      else:
        print(f'{Fore.GREEN}{str(a).center(4, " ")}{Style.RESET_ALL}', end='',)
    print()
  print()


def getCircularPoints(x:int, y:int):
  return [
    (x-1, y),
    (x, y+1),
    (x+1, y),
    (x, y-1)
  ]