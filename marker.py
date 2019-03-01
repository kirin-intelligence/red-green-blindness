# https://lbs.amap.com/api/webservice/guide/api/staticmaps/
import json
import os

import requests
import time
from redis import StrictRedis, ConnectionPool
from get_line import find_point
from config import *

pool = ConnectionPool(host='123.56.19.49', password='wscjxky123', port=6379, db=1)
redis = StrictRedis(connection_pool=pool)

count = 0
x_list = [x1 + i * x_step for i in range(x_count)]
y_list = [y1 - i * y_step for i in range(x_count)]
hsetname = 'jiaot:' + str(count)
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
redis.hset(hsetname, 'time', now)
flag=0
for xi, xv in enumerate(x_list):
    sum = 0
    for yi, yv in enumerate(y_list[8:]):

        dirname = 'images/test/' + str(xi)
        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        filename = dirname + '/' + str(sum) + '.png'
        url = ('https://restapi.amap.com/v3/staticmap?&'
               'zoom=15&size=' + str(size) + '*' + str(size) +
               '&location=' + str(xv) + ',' + str(yv) + '&'
                                                        'scale=2&'
                                                        'traffic=' + str(1) +

               '&key=2be4c36d53e74e0c585326d62d6fe6e3')
        print(str(xv) + ',' + str(yv))
        data = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(data.content)
        points = find_point(filename, [xv, yv])
        if points:
            print(points)
            flag=1
            break
        sum += 1
    if flag==1:
        break