def printVec(vec: list[int]):
  print()
  for i in vec:
    for a in i:
      if a == -1:
        print(' + ',  end='')
        continue
      print(f' {a} ', end='')
    print()
  print()

cartesian = [
  [0, 0, 0, 0, -1, -1, -1, -1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, -1, 0, -1, 0, 0, 0, 0],
  [0, 0, -1, 0, -1, 0, 0, 0, 0],
  [0, 0, -1, 0, -1, 0, 0, 0, 0],
  [0, 0, -1, 0, -1, 0, 0, 0, 0],
  [0, 0, -1, 0, -1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, -1, 0],
  [0, 0, 0, 0, 0, 0, 0, -1, 0],
]

printVec(cartesian)

for x, row in enumerate(cartesian):
  for y, col in enumerate(row):
    positionValue = cartesian[x][y]

    if(cartesian[x][y+1] == 0):
      cartesian[x][y+1] = positionValue + 1

    if(cartesian[x+1][y] == 0):
      cartesian[x+1][y] = positionValue + 1

    print()


printVec(cartesian)




