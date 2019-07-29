import datetime
import time
import numpy as np
import cv2
from math import radians, cos, sin, asin, sqrt
import os
import socket
import gc
from urllib.request import urlopen
from constant import THREAD_FLAG, GLOBAL_CONFIG, SPACING_TIME,DATA_DIR, WORK_TIME, ALPHA,BELTA,GAMA,SOCKET_TIMEOUT

socket.setdefaulttimeout(SOCKET_TIMEOUT)

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
        if not GLOBAL_CONFIG[THREAD_FLAG]:
            print('线程终止')
            exit()
        try:
            time_now = datetime.datetime.now()
            time_h = time_now.hour
            if time_h in GLOBAL_CONFIG[WORK_TIME]:
                child_path = "{0}_{1}/".format(time.strftime("%Y_%m_%d"), str(time_h))
                if not os.path.exists("{}{}".format(GLOBAL_CONFIG[DATA_DIR], child_path)):
                    os.mkdir("{}{}".format(GLOBAL_CONFIG[DATA_DIR], child_path))
                name_string = "{0}{1}{2}_{3}_{4}_{5}.npz".format(GLOBAL_CONFIG[DATA_DIR], child_path, time.strftime("%Y_%m_%d"),
                                                                 str(time_h), str(GPS_x), str(GPS_y))
                URL = "https://restapi.amap.com/v3/staticmap?&zoom=15&size=600*600&location={0},{1}&scale=2&traffic=1&key=2be4c36d53e74e0c585326d62d6fe6e3".format(
                    str(GPS_x), str(GPS_y))
                img_data = urlopen(URL).read()
                img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
                del img_data
                gc.collect()
                hot_map = get_line_hotmap(img)
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
                print([GPS_x, GPS_y])
                time.sleep(GLOBAL_CONFIG[SPACING_TIME])
                print("Working...{}".format(str(time_now)))
            else:
                gc.collect()
                time.sleep(GLOBAL_CONFIG[SPACING_TIME])
                print("Waiting...{}".format(str(time_now)))
        except Exception as e:
            print(e)


color_dic = {'RED_l': np.array([0, 0, 220]), 'RED_h': np.array([0, 0, 222]),
             'YELLO_l': np.array([0, 202, 253]), 'YELLO_h': np.array([0, 204, 255]),
             'GREEN_l': np.array([0, 175, 49]), 'GREEN_h': np.array([0, 177, 51]),
             'DEEPRED_l': np.array([13, 13, 138]), 'DEEPRED_h': np.array([13, 13, 140]), }


def get_line_hotmap(frame):
    return np.float32(0.001) * np.sign(cv2.inRange(frame, color_dic['GREEN_l'], color_dic['GREEN_h'])) + np.float32(
        0.001) * np.sign(cv2.inRange(frame, color_dic['YELLO_l'], color_dic['YELLO_h'])) + np.float32(2) * np.sign(
        cv2.inRange(frame, color_dic['RED_l'], color_dic['RED_h'])) + np.float32(2) * np.sign(
        cv2.inRange(frame, color_dic['DEEPRED_l'], color_dic['DEEPRED_h']))


def get_line(frame):
    # get mask
    r = cv2.inRange(frame, color_dic['RED_l'], color_dic['RED_h'])
    y = cv2.inRange(frame, color_dic['YELLO_l'], color_dic['YELLO_h'])
    g = cv2.inRange(frame, color_dic['GREEN_l'], color_dic['GREEN_h'])
    dr = cv2.inRange(frame, color_dic['DEEPRED_l'], color_dic['DEEPRED_h'])
    mask = r + y + g + dr
    res = cv2.bitwise_and(frame, frame, mask=mask)
    return res, g, y, r, dr


def run_rgb(hmap, count):
    hmap = hmap / count
    red_ori = hmap > ALPHA
    yellow_ori = (hmap > BELTA) & (hmap <= ALPHA)
    green_ori = (hmap <= BELTA) & (hmap > GAMA)

    red = red_ori[:, :, np.newaxis]
    yellow = yellow_ori[:, :, np.newaxis]
    green = green_ori[:, :, np.newaxis]

    red = np.repeat(red, 3, axis=2)
    yellow = np.repeat(yellow, 3, axis=2)
    green = np.repeat(green, 3, axis=2)

    red = red * color_dic['RED_l']
    yellow = yellow * color_dic['YELLO_l']
    green = green * color_dic['GREEN_l']

    final = red + yellow + green
    final = np.asarray(final, dtype=np.uint8)
    return final, red, yellow, green


def head_end(tuzi_map):
    def calcul_dis(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    gray = np.uint8(tuzi_map)
    ls = cv2.HoughLinesP(gray, 1, np.pi / 180, threshold=60, minLineLength=60, maxLineGap=5)
    head_max, end_max = None, None
    if ls is None:
        return head_max, end_max

    head_end = ls[:, 0, :]
    max_dis = 0
    for i in head_end:
        head = tuple(i[0: 2])
        end = tuple(i[2: 4])
        current_dis = calcul_dis(head, end)
        if current_dis > max_dis:
            max_dis = current_dis
            head_max, end_max = head, end
    return head_max, end_max


def no_eages(img):
    img[0: 50, :] = 0
    img[-50:, :] = 0
    img[:, 0: 50] = 0
    img[:, -50:] = 0
    img_without_eage = np.asarray(img, dtype=np.uint8)
    return img_without_eage


def solve(input_map, origin_data):
    count = 0
    point_paer = []
    input_map = no_eages(input_map)
    try:
        _, labels = cv2.connectedComponents(input_map, connectivity=8)
        labels_lst = np.reshape(labels, [-1])
        labels_lst = [x for x in range(1, _)]
        for i in labels_lst:
            single_connect = (labels == i)
            if np.sum(single_connect) > 50:
                point = head_end(single_connect)
                if point != (None, None):
                    time_conunt = origin_data * single_connect
                    avg_time = np.sum(time_conunt) / np.sum(np.sign(time_conunt))
                    datapack = list(point)
                    datapack.append(avg_time)
                    point_paer.append(datapack)
                count += 1
    except:
        pass
    return point_paer


def la_le_point(data_pack, type, center):
    points = data_pack[0:2]
    px = 0.0124 / (1200 - 44)
    py = 0.009 / (1200 - 104)
    zero_point = [center[0] - 600 * px, center[1] - 600 * py]
    lat_points_pack = []
    for point in points:
        lat_point = [zero_point[0] + px * point[0], zero_point[1] + py * (1200 - point[1]), type]
        lat_points_pack.append(list(lat_point))
    lat_points_pack.append(data_pack[-1])
    return lat_points_pack


def report(img, gps_centor, ori_data):
    res_map, green, yellow, red, _ = get_line(img)
    ans = solve(red, ori_data)
    ans_y = solve(yellow, ori_data)
    ans_g = solve(green, ori_data)
    result = []
    for i in ans_g:
        cv2.circle(res_map, i[0], 5, color=(255, 255, 255))
        cv2.circle(res_map, i[1], 5, color=(255, 255, 255))
        ans_g = la_le_point(i, 'green', gps_centor)
        result.append(ans_g)
    for i in ans:
        cv2.circle(res_map, i[0], 5, color=(255, 255, 255))
        cv2.circle(res_map, i[1], 5, color=(255, 255, 255))
        red = la_le_point(i, 'red', gps_centor)
        result.append(red)
    for i in ans_y:
        cv2.circle(res_map, i[0], 5, color=(255, 0, 255))
        cv2.circle(res_map, i[1], 5, color=(255, 0, 255))
        yellow = la_le_point(i, 'yellow', gps_centor)
        result.append(yellow)
    point_res_map = cv2.resize(res_map, (1024, 1024))
    return result, point_res_map


def geodistance(lng1,lat1,lng2,lat2):
    #lng1,lat1,lng2,lat2 = (120.12802999999997,30.28708,115.86572000000001,28.7427)
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])# 经纬度转换成弧度
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    distance = 2*asin(sqrt(a))*6371*1000# 地球平均半径，6371km
    distance = round(distance/1000, 3)
    return distance


def cal_middle(lng1,lat1,lng2,lat2):
    return (lng1+lng2)/2, (lat1+lat2)/2

def cal_length(ans_pair):
    new_ans = []
    for ans in ans_pair:
        length = geodistance(ans[0][0], ans[0][1], ans[1][0], ans[1][1])
        ans.append(length)
        ans.append(cal_middle(ans[0][0], ans[0][1], ans[1][0], ans[1][1]))
        new_ans.append(ans)
    return new_ans
