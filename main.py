from propagate import *
from wave_front import Wave_Front
world = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-1, -1, -1, -1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, -1, 0],
    [0, 0, 0, 0, 0, 0, 0, -1, 0],
]

# propagate(world, [], (4,6))

adler = Wave_Front(world)

adler.propagate((4, 6))
adler.propagate((0, 6))
