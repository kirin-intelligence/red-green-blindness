import json

import requests
import xlrd
import xlwt
from xlutils.copy import copy
from redis import StrictRedis, ConnectionPool

pool = ConnectionPool(host='123.56.19.49', password='wscjxky123', port=6379, db=8, decode_responses=True)
redis = StrictRedis(connection_pool=pool)
g = [[[116.355888, 39.933548, 'red'], [116.35562, 39.939498, 'red']],
     [[116.355571, 39.936919, 'red'], [116.355754, 39.933608], 'red']]
pool1 = ConnectionPool(host='123.56.19.49', password='wscjxky123', port=6379, db=6, decode_responses=True)
redis1 = StrictRedis(connection_pool=pool1)


# write_excel()


def get_place(point):
    url = 'https://restapi.amap.com/v3/geocode/regeo?key=2be4c36d53e74e0c585326d62d6fe6' \
          'e3&location=%s,%s&poitype=&radius=1000&extensions=base&batch=false&roadlevel=0' % (point[0], point[1])
    data = json.loads(requests.get(url).text)
    place = (data['regeocode']['formatted_address'])
    return place


def get_distance(start_point, end_point):
    url = "https://restapi.amap.com/v3/direction/walking?origin=%s,%s&destina" \
          "tion=%s,%s&key=2be4c36d53e74e0c585326d62d6fe6e3" % (
              start_point[0], start_point[1], end_point[0], end_point[1])
    data = json.loads(requests.get(url).text)
    dis = (data['route']['paths'][0]['distance'])
    paths = data['route']['paths'][0]['steps'][0]['polyline']
    paths = paths.split(';')
    new_paths = []
    for point in paths:
        point = point.split(',')
        new_point = []
        for p in point:
            new_point.append(float(p))
        new_paths.append(new_point)

    return dis, new_paths


def write_excel(points, day, start=0, gps_center=0):
    print(points)
    workbook = xlrd.open_workbook('data%s.xls' % day)
    workbook = copy(workbook)
    worksheet = workbook.get_sheet(0)
    worksheet.write(0, 0, label='序号')
    worksheet.write(0, 1, label='起点')
    worksheet.write(0, 2, label='起点经纬度')
    worksheet.write(0, 3, label='终点')
    worksheet.write(0, 4, label='终点经纬度')
    worksheet.write(0, 5, label='长度')
    worksheet.write(0, 6, label='拥堵情况（颜色）')
    # worksheet.write(0, 7, label='具体时间')
    for index, point in enumerate(points):
        start_point = point[0]
        end_point = point[1]
        start_place = get_place(start_point)
        end_place = get_place(end_point)
        distance, paths = get_distance(start_point, end_point)
        no = start + index
        type = point[0][2]
        worksheet.write(index + start, 0, label="%s" % no)
        worksheet.write(index + start, 1, label="%s" % start_place)
        worksheet.write(index + start, 2, label="%s,%s" % (start_point[0], start_point[1]))
        worksheet.write(index + start, 3, label="%s" % end_place)
        worksheet.write(index + start, 4, label="%s,%s" % (end_point[0], end_point[1]))
        worksheet.write(index + start, 5, label="%s" % distance)
        if type == 'red':
            color = '红色'
        elif type == 'yellow':
            color = '橙黄'
        else:
            color = '黄色'
        worksheet.write(index + start, 6, label="%s" % color)
        # worksheet.write(index, 7, label=point)
        # hset_name = "%s:%s" % (day, no)
        # redis.hset(hset_name, "no", no)
        # redis.hset(hset_name, "start_point", json.dumps(start_point[:-1]))
        # redis.hset(hset_name, "end_point", json.dumps(end_point[:-1]))
        # redis.hset(hset_name, "type", type)
        # redis.hset(hset_name, "distance", distance)

        # redis.hset(hset_name, "start_place", start_place)
        # redis.hset(hset_name, "end_place", end_place)
        # redis.hset(hset_name, "paths", json.dumps(paths))
        # redis.hset(hset_name, "day", day)
        # redis.hset(hset_name, "gps_center", json.dumps(gps_center))
        print(point)
    workbook.save('data%s.xls' % day)
    return len(points)


def add_redis(points, start=0, day='evening'):
    for index, point in enumerate(points):
        index += 2
        start_point = point[0]
        end_point = point[1]
        start_place = get_place(start_point)
        end_place = get_place(end_point)
        jam_time = point[2]
        no = start + index
        type = point[0][2]
        hset_name = "%s:%s" % (day, no)
        redis.hset(hset_name, "no", no)
        redis.hset(hset_name, "start_point", json.dumps(start_point[:-1]))
        redis.hset(hset_name, "end_point", json.dumps(end_point[:-1]))
        redis.hset(hset_name, "type", type)
        redis.hset(hset_name, "start_place", start_place)
        redis.hset(hset_name, "end_place", end_place)
        redis.hset(hset_name, "day", day)
        redis.hset(hset_name, "jam_time", 120 * jam_time)
    return start + len(points)


def write_to_excel(day='evening'):
    workbook = xlwt.Workbook()
    workbook.add_sheet('0')
    workbook.save('data%s.xls' % day)
    workbook = xlrd.open_workbook('data%s.xls' % day)
    workbook = copy(workbook)
    worksheet = workbook.get_sheet(0)
    worksheet.write(0, 0, label='序号')
    worksheet.write(0, 1, label='起点')
    worksheet.write(0, 2, label='起点经纬度')
    worksheet.write(0, 3, label='终点')
    worksheet.write(0, 4, label='终点经纬度')
    worksheet.write(0, 5, label='长度')
    worksheet.write(0, 6, label='拥堵情况（颜色）')
    worksheet.write(0, 7, label='拥堵时间（分钟）')

    for index, hset_name in enumerate(redis.keys(day + ':*')):
        print(index)
        start_point = json.loads(redis.hget(hset_name, "start_point"))
        end_point = json.loads(redis.hget(hset_name, "end_point"))
        start_place = redis.hget(hset_name, "start_place")
        end_place = redis.hget(hset_name, "end_place")
        jam_time = round(float(redis.hget(hset_name, "jam_time")),1)
        distance = redis.hget(hset_name, "distance")
        no = int(redis.hget(hset_name, "no"))
        type = redis.hget(hset_name, "type")
        worksheet.write(no - 1, 0, label="%s" % no)
        no = no - 1
        worksheet.write(no, 1, label="%s" % start_place)
        worksheet.write(no, 2, label="%s,%s" % (start_point[0], start_point[1]))
        worksheet.write(no, 3, label="%s" % end_place)
        worksheet.write(no, 4, label="%s,%s" % (end_point[0], end_point[1]))
        worksheet.write(no, 5, label="%s" % distance)
        if type == 'red':
            color = '红色'
        elif type == 'yellow':
            color = '橙黄'
        else:
            color = '黄色'
        worksheet.write(no, 6, label="%s" % color)
        worksheet.write(no, 7, label="%s" % jam_time)

    workbook.save('data%s.xls' % day)


def move_erhuan():
    offset = 568
    for index, i in enumerate(range(1136, 1147)):
        data = redis1.hgetall('morning:' + str(i))
        data['no'] = str((i - 1136) + (offset))
        redis.hmset('morning:' + str((i - 1136) + (offset)), data)
        start = (i - 1136) + (offset)
        a = list(json.loads(data['start_point']))
        a.append(data['type'])
        b = json.loads(data['end_point'])
        b.append(data['type'])
        print([[a, b]])
        write_excel(points=[[a, b]], day='morning', start=start)


if __name__ == '__main__':
    write_to_excel('morning')
    write_to_excel()
    # r=[]
    # a=redis.keys('evening' + ':*')
    # for i in a[:3]:
    #     r.append(i)
    # c=redis.scan(0,"morning*",10000)
    # print(len(c[1]))
    # print(c)
    pass


#164 - 68
#458  - 386
#412 - 219


# 晚
# 225 - 241