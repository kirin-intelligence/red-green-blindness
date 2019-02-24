# https://lbs.amap.com/api/webservice/guide/api/staticmaps/
import json
import os

import requests
import time
from redis import StrictRedis, ConnectionPool
from con_imagesd import con_to_pic
from get_line import find_point
from config import *

pool = ConnectionPool(host='localhost', password='wscjxky123', port=6379, db=1)
redis = StrictRedis(connection_pool=pool)

count = 0
x_list = [str(x1 + i * x_step) for i in range(x_count)]
y_list = [str(y1 - i * y_step) for i in range(x_count)]
while True:
    for xi, xv in enumerate(x_list):
        sum = 0
        for yi, yv in enumerate(y_list):
            dirname = 'images/full/' + str(xi)
            if not os.path.isdir(dirname):
                os.mkdir(dirname)
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            filename = dirname + '/jiaot_' + str(sum) + '.png'
            url = ('https://restapi.amap.com/v3/staticmap?&'
                   'zoom=15&size=' + str(size) + '*' + str(size) +
                   '&location=' + str(xv) + ',' + str(yv) + '&'
                                                            'scale=2&'
                                                            'traffic=' + str(1) +
                   '&key=2be4c36d53e74e0c585326d62d6fe6e3')
            data = requests.get(url)
            with open(filename, 'wb') as file:
                file.write(data.content)
            print(url)
            sum += 1
            # print(find_points)
    filename = con_to_pic()
    hsetname = 'jiaot:' + str(count)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    redis.hset(hsetname, 'time', now)
    redis.hset(hsetname, 'ori_pic', filename)


    points=[]
    for i in range(x_count):
        for f in os.listdir('images/full/%d' % i):
            filename = 'images/full/%d/%s' % (i, f)
            find_points = find_point(filename)
            points.append(find_points)
            redis.hset(hsetname, filename, json.dumps(find_points))

    filename = con_to_pic()
    redis.hset(hsetname, 'pri_pic', filename)
    redis.hset(hsetname, 'points',json.dumps(points))

    count += 1
    break
    time.sleep(120)




# size = 600
# filename = 'test'
# for i in range(2):
#     data = requests.get('https://restapi.amap.com/v3/staticmap?&'
#                         'zoom=17&size=' + str(size) + '*' + str(size) +
#                         '&location=116.352615,39.908664&'
#                         'scale=2&'
#                         'traffic=' + str(i) +
#                         '&key=2be4c36d53e74e0c585326d62d6fe6e3')
#     with open(filename + str(i) + '.png', 'wb') as file:
#         file.write(data.content)
