# https://lbs.amap.com/api/webservice/guide/api/staticmaps/
import json
import os
import re
import threading

import requests
import time
from get_line import find_point
from config import *


def get_time():
    return time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


class GaoDegraph(object):
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def url(self):
        return ('https://restapi.amap.com/v3/staticmap?&zoom=15&size=600*600&location=%s,%s&'
                'scale=2&traffic=1&key=2be4c36d53e74e0c585326d62d6fe6e3') % (
                   str(self.location[0]), str(self.location[1]))

    @property
    def hsetname(self):
        return self._hsetname

    @hsetname.setter
    def hsetname(self, value):
        self._hsetname = value

    @property
    def markers_url(self):
        points = redis.hget(self.hsetname, 'points')
        points = eval(points)
        color = '0xFFFF00'
        label = 'C'
        marker = ''
        print((points))
        for p in points[:-5]:
            x = str(p[0])
            y = str(p[1])
            type = str(p[2])
            if type == '0':
                color = '0xFFFF00'
                label = 'C'
            elif type == '1':
                color = '0xFFFF00'
                label = 'B'
            elif type == '2':
                color = '0x000000'
                label = 'A'
            marker += 'large,%s,%s:%s,%s|' % (color, label, str(x), str(y))

        url = ('https://restapi.amap.com/v3/staticmap?&zoom=15&size=600*600&location=%s,%s&'
               'scale=2&traffic=0&markers=%s&key=2be4c36d53e74e0c585326d62d6fe6e3') % (
                  str(self.location[0]),
                  str(self.location[1])
                  , marker
              )
        pattern = re.compile(r'\|&+')
        # 去掉最後一個 `|`
        url = re.sub(pattern, '&', url)
        print(marker)
        print(url)
        return url

    @property
    def markers(self):
        points = redis.hget(self.hsetname, 'points')
        points = eval(points)
        return points

    @property
    def name_list(self):
        return self._name_list

    @name_list.setter
    def name_list(self, value):
        self._name_list = value

    # list
    # list[0]=x
    # list[1]=y
    # list[2]=count 代表時間
    @property
    def filename(self):
        return self._filename

    def download_img(self):
        xi, yi = self.location
        dirname = 'images/'
        self._filename = dirname + str(xi) + str(yi) + '.png'
        # data = requests.get(self.url)
        # with open(self._filename, 'wb') as file:
        #     file.write(data.content)
        print(self.url)

    @property
    def gps_markers(self):
        find_points = find_point(self._filename, self.location)
        return find_points


def get_img(gaode_graph):
    gaode_graph.download_img()
    # gaode_graph.set_redis(hsetname)


def startthread(graph_list):
    print(len(graph_list))
    threadlist = []
    for g in graph_list:
        t = threading.Thread(target=get_img, args=(g,))
        t.setDaemon(True)
        threadlist.append(t)
    for t in threadlist:
        t.start()
    for j in threadlist:
        j.join()


if __name__ == '__main__':
    while True:
        graph_list = []
        x_list = [x1 + i * x_step for i in range(x_count)]
        y_list = [y1 - i * y_step for i in range(x_count)]
        now_time = get_time()
        for xi, xv in enumerate(x_list):
            for yi, yv in enumerate(y_list):
                graph = GaoDegraph()
                graph.location = [xv, yv]
                graph.time = now_time
                graph_list.append(graph)
        startthread(graph_list)
        try:
            markers = []
            for index, gra in enumerate(graph_list):
                print(gra.filename)
                find_points = find_point(gra.filename, gra.location)
                marker = gra.gps_markers
                markers += marker
                print(index)
            hsetname = "gaode:" + gra.time
            redis.hset(hsetname, 'points', json.dumps(markers))
            redis.hset(hsetname, 'time', gra.time)
        except Exception as e:
            with open('error', 'a')as f:
                f.write(gra.filename)
                f.write(str(e))
                print(e)
                print(gra.filename)
        time.sleep(10)

        # keys = redis.keys('gaode:*')
        # for k in keys:
        #     pattern=re.compile('gaode:(.+):(.+)')
        #     time = re.search(pattern, k.decode('utf8')).group(1)
        #     location = re.search(pattern, k.decode('utf8')).group(2)
        #     print(time, location)
        #     g1.hsetname = k
        #     g1.markers_url
