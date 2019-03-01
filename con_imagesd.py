import time
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from config import *

import os

TARGET_WIDTH = UNIT_SIZE * x_count

def con_to_pic():
    con_y()
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    dirn = 'images/y/'
    UNIT_SIZE = 2048
    x= 2048-85
    left = x
    right = left+ UNIT_SIZE
    target = Image.new('RGB', (TARGET_WIDTH, TARGET_WIDTH))
    image = Image.open(dirn + "0.png")
    print(image.size)
    target.paste(image, (0, 0, UNIT_SIZE,TARGET_WIDTH ))
    for i in range(1,x_count):
        image = Image.open(dirn + str(i) + '.png')
        target.paste(image, (left, 0, right, TARGET_WIDTH))
        left += x  # left是左上角的横坐标，依次递增
        right = left + UNIT_SIZE  # right是右下的横坐标，依次递增
        image.close()
    target.save('images/x/'+now+'.png', quality=1)
    return 'images/x/'+now+'.png'

# 左、上、右和下
# 1095
def con_y():
    for i in range(x_count):
        dirn = 'images/full/%d/'%i
        y = 2048-75
        top = y
        bottom = y + UNIT_SIZE
        target = Image.new('RGB', (UNIT_SIZE, TARGET_WIDTH))
        image = Image.open(dirn +'0.png')

        target.paste(image, (0, 0, UNIT_SIZE, UNIT_SIZE))
        for j in range(1, x_count):
            image = Image.open(dirn + str(j)+'.png')
            target.paste(image, (0, top, UNIT_SIZE, bottom))  # 将image复制到target的指定位置中
            top += y  # left是左上角的横坐标，依次递增
            bottom = top + UNIT_SIZE  # right是右下的横坐标，依次递增
        target.save("images/y/" + str(i) + '.png', quality=1)

for xi in range(20):


    with open('images/x/' + str(xi) + '.html', 'w')as f:
        st = '''<iframe   frameborder='0'    src='../../%s0.html' scrolling='no'  width='2048' height='2048' >
                               </iframe>'''%(xi)
        for yi in range(1,20):
            st+='''<iframe   frameborder='0' style="margin-top: -89px"     src='../../%s%s.html' scrolling='no'  width='2048' height='2048' >
            </iframe>'''%(xi,yi)
        print(st)
        f.write('''<!DOCTYPE html>
        <html>
        <head>
            <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
        </head>
        <style>

            *{
                padding: 0;
                margin: 0;
            }
            body html{
            !important;width:2048px;

            }


        </style>
        <body>
        %s

        </body>
        </html>
        '''%st)