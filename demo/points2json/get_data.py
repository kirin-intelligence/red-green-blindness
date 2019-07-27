import threading
import config
import datetime
import time
import requests
import util
import numpy as np
import cv2
import os
import socket
import gc

timeout = 25
socket.setdefaulttimeout(timeout)
base_path = "data/"

headers = {
    'Connection': 'close',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept - Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
    'Host': 'restapi.amap.com',
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
}


def background_worker(GPS_x, GPS_y):
    while True:
        try:
            time_now = datetime.datetime.now()
            time_h = time_now.hour
            if time_h in config.worktime:
                child_path = "{0}_{1}/".format(time.strftime("%Y_%m_%d"), str(time_h))
                if not os.path.exists("{}{}".format(base_path, child_path)):
                    os.mkdir("{}{}".format(base_path, child_path))
                name_string = "{0}{1}{2}_{3}_{4}_{5}.npz".format(base_path, child_path, time.strftime("%Y_%m_%d"), str(time_h), str(GPS_x), str(GPS_y))
                URL = "https://restapi.amap.com/v3/staticmap?&zoom=15&size=600*600&location={0},{1}&scale=2&traffic=1&key=2be4c36d53e74e0c585326d62d6fe6e3".format(str(GPS_x), str(GPS_y))
                img_data = requests.get(URL, headers=headers).content
                img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
                del img_data
                gc.collect()
                hot_map = util.get_line_hotmap(img)
                del img
                gc.collect()
                if os.path.exists(name_string):
                    old_data = np.load(name_string)
                    np.savez_compressed(name_string, old_data['arr_0'] + 1, old_data['arr_1'] + hot_map)
                    del old_data, hot_map, time_h, child_path, name_string, URL
                else:
                    np.savez_compressed(name_string, 1, hot_map)
                    del hot_map, time_h, child_path, name_string, URL
                gc.collect()
                print([GPS_x,GPS_y])
                time.sleep(120)
                print("Working...{}".format(str(time_now)))
            else:
                gc.collect()
                time.sleep(120)
                print("Waiting...{}".format(str(time_now)))
        except Exception as e:
            print(e)


def collect_data_main():
    if not os.path.exists(base_path):
        os.mkdir(base_path)
    x_list = [config.x1 + i * config.x_step for i in range(config.x_count)]
    y_list = [config.y1 - i * config.y_step for i in range(config.y_count)]
    point_lst = [(x, y) for x in x_list for y in y_list]

    for sp in config.special_point:
        point_lst.append(sp)

    t_lst = []
    for p in point_lst:
        t_lst.append(threading.Thread(target=background_worker, args=(p)))

    del x_list
    del y_list
    del point_lst
    gc.collect()

    try:
        for t in t_lst:
            t.setDaemon(True)
            t.start()
            time.sleep(120/len(t_lst))
        for t in t_lst:
            t.join()
    except Exception as e:
        print(e)
