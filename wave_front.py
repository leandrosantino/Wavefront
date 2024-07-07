import os
import time
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import copy


class Wave_Front:

    __world: list[list[int]]

    def __init__(self, world: list[list[int]]) -> None:
        self.__world = world

    def propagate(self, coords: tuple[int, int]):
        propagated_world = copy.deepcopy(self.__world)
        x, y = coords

        circular_points = self.__getCircularPoints(coords)
        current_value = propagated_world[x][y]

        for x, y in circular_points:
            if (self.__verifyPosition(propagated_world, coords, (x, y))):
                propagated_world[x][y] = current_value + 1

        while (len(circular_points) > 0):
            next_points = []
            for x, y in circular_points:

                try:
                    current_value = propagated_world[x][y]
                except IndexError:
                    continue

                circular_points = self.__getCircularPoints((x, y))

                for x, y in circular_points:
                    if (self.__verifyPosition(propagated_world, coords, (x, y))):
                        next_points.append((x, y))
                        propagated_world[x][y] = current_value + 1

                circular_points = next_points

        return propagated_world

    def __getCircularPoints(self, coords: tuple[int, int]):
        x, y = coords
        return [
            (x-1, y),
            (x, y+1),
            (x+1, y),
            (x, y-1)
        ]

    def __verifyPosition(self, world: list[list[int]], initialPoint: tuple[int, int], coords: tuple[int, int]):
        try:
            x, y = coords
            if (x < 0 or y < 0):
                return False
            if (world[x][y] > 0):
                return False
            if (world[x][y] < 0):
                return False
            if (coords == initialPoint):
                return False
            return True
        except IndexError:
            return False

    def printVec(self, vec: list[list[int]]):
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
                    print(
                        f'{Fore.GREEN}{str(a).center(4, " ")}{Style.RESET_ALL}', end='',)
            print()
        print()

    def create_show_world(self, world: list[list[int]]):
        maxi = 0
        for row in world:
            for px in row:
                if (px > maxi):
                    maxi = px

        ratio = (255 / maxi)

        show_word = []
        for row in world:
            nr = []
            for px in row:
                if (px < 0):
                    nr.append((255, 255, 255))
                    continue

                if (px >= 0 and px <= 1):
                    nr.append((225, 235, 154))
                    continue

                value = int(px * ratio)
                value = 255 - value

                # if (value <= 30):
                #     value = 30
                # if (value > 30 and value <= 102):
                #     value = 102
                # if (value > 102 and value <= 153):
                #     value = 153
                # if (value > 153 and value <= 204):
                #     value = 204
                # if (value > 204):
                #     value = 220

                nr.append((value, int(value/2), 0))
            show_word.append(nr)

        return show_word
