from PIL import Image
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from propagate import *
from wave_front import Wave_Front

img_path = 'resource/world.png'

img = Image.open(img_path)
img = img.convert('RGB')
img_w, img_h = img.size

data = np.asarray(img)


def rgb_to_number(c):
    v = 0
    for i in c:
        v += i
    return v


world = []
for row in data:
    nr = []
    for px in row:
        px = rgb_to_number(px)
        if (px != 765):
            nr.append(0)
        else:
            nr.append(-1)
    world.append(nr)

_, axes = plt.subplots(1, 2)

adler = Wave_Front(world)

propagated_world = adler.propagate((112, 116))
axes[0].imshow(adler.create_show_world(propagated_world))

propagated_world2 = adler.propagate((10, 278))
axes[1].imshow(adler.create_show_world(propagated_world2))

plt.show()
