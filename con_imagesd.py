import time
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

import os

UNIT_SIZE = 2048
TARGET_WIDTH = UNIT_SIZE * 3


def con_to_pic():
    con_y()
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    dirn = 'images/y/'
    UNIT_SIZE = 2048
    x= 2048-85
    left = x
    right = left+ UNIT_SIZE
    target = Image.new('RGB', (TARGET_WIDTH, TARGET_WIDTH))
    image = Image.open(dirn + os.listdir(dirn)[0])
    print(image.size)
    target.paste(image, (0, 0, UNIT_SIZE,TARGET_WIDTH ))
    for i in os.listdir(dirn)[1:]:
        image = Image.open(dirn + i)
        print( left, 0, right, UNIT_SIZE)
        target.paste(image, (left, 0, right, TARGET_WIDTH))

        left += x  # left是左上角的横坐标，依次递增
        right = left + UNIT_SIZE  # right是右下的横坐标，依次递增
    target.save('images/x/'+now+'.png', quality=1)
    return 'images/x/'+now+'.png'

# 左、上、右和下
# 1095
def con_y():
    for i in range(3):
        dirn = 'images/full/%d/'%i
        y = 2048-75
        top = y
        bottom = y + UNIT_SIZE
        target = Image.new('RGB', (UNIT_SIZE, TARGET_WIDTH))
        image = Image.open(dirn + os.listdir(dirn)[0])
        target.paste(image, (0, 0, UNIT_SIZE, UNIT_SIZE))
        for index, value in enumerate(os.listdir(dirn)[1:]):
            image = Image.open(dirn + value)
            print((0, top, UNIT_SIZE, bottom))
            target.paste(image, (0, top, UNIT_SIZE, bottom))  # 将image复制到target的指定位置中
            top += y  # left是左上角的横坐标，依次递增
            bottom = top + UNIT_SIZE  # right是右下的横坐标，依次递增
        target.save("images/y/" + str(i) + '.png', quality=1)

