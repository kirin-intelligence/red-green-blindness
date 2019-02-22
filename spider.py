# https://lbs.amap.com/api/webservice/guide/api/staticmaps/
import json

import requests
import time
from redis import StrictRedis,ConnectionPool

from get_line import find_point

pool = ConnectionPool(host='123.56.19.49',password='wscjxky123', port=6379, db=0)
redis = StrictRedis(connection_pool=pool)

size = 600
count=0
while True:
    hsetname = 'jiaot:' + str(count)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename = 'images/jiaot_'+now+ '.png'
    url = ('https://restapi.amap.com/v3/staticmap?&'
                        'zoom=15&size=' + str(size) + '*' + str(size) +
                        '&location=116.340247,39.959533&'
                        'scale=2&'
                        'traffic=' + str(1) +
                        '&key=2be4c36d53e74e0c585326d62d6fe6e3')

    data = requests.get(url)
    with open(filename , 'wb') as file:
        file.write(data.content)
    find_points=find_point(filename)
    redis.hset(hsetname,'points',json.dumps(find_points))

    redis.hset(hsetname,'url',url)
    redis.hset(hsetname,'image_name',filename)
    redis.hset(hsetname, 'time', now)
    count += 1
    print(find_points)
    print(url)
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
