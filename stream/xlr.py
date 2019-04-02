import json

import requests
import xlrd
from xlutils.copy import copy
from redis import StrictRedis, ConnectionPool

pool = ConnectionPool(host='123.56.19.49', password='wscjxky123', port=6379, db=7, decode_responses=True)
redis = StrictRedis(connection_pool=pool)

def move_erhuan():
    pool1 = ConnectionPool(host='123.56.19.49', password='wscjxky123', port=6379, db=7, decode_responses=True)
    redis1 = StrictRedis(connection_pool=pool1)
    for i in range(1136,1147):
        data=redis.hgetall('morning:'+str(i))
        print(data)
        redis1.hmset('morning:'+str((i-1136)+(534)),data)
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
    workbook = xlrd.open_workbook('data.xls')
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
        worksheet.write(index+start, 0, label="%s" % no)
        worksheet.write(index+start, 1, label="%s" % start_place)
        worksheet.write(index+start, 2, label="%s,%s" % (start_point[0], start_point[1]))
        worksheet.write(index+start, 3, label="%s" % end_place)
        worksheet.write(index+start, 4, label="%s,%s" % (end_point[0], end_point[1]))
        worksheet.write(index+start, 5, label="%s" % distance)
        worksheet.write(index+start, 6, label="%s" % "红色" if type == 'red' else "黄色")
        # worksheet.write(index, 7, label=point)
        hset_name = "%s:%s" % (day, no)
        redis.hset(hset_name, "no", no)
        redis.hset(hset_name, "start_point", json.dumps(start_point[:-1]))
        redis.hset(hset_name, "end_point", json.dumps(end_point[:-1]))
        redis.hset(hset_name, "type", type)
        redis.hset(hset_name, "distance", distance)
        redis.hset(hset_name, "start_place", start_place)
        redis.hset(hset_name, "end_place", end_place)
        redis.hset(hset_name, "paths", json.dumps(paths))
        redis.hset(hset_name, "day", day)
        redis.hset(hset_name, "gps_center", json.dumps(gps_center))
        print(point)
    workbook.save('data.xls')
    return len(points)


gps_center = [116.30756199999999, 39.944875999999994]

day = 'morning'
# write_excel(points, day,gps_center)

#
# readbook = xlrd.open_workbook(r'/home/kaiyuan_xu/Downloads/'+day+'.xlsx')
# sheet = readbook.sheet_by_index(0)
# nrows = sheet.nrows
# ncols = sheet.ncols
# arr = []
# import requests
#
# arr1 = []
# for i in range(0, nrows):
#     start = sheet.cell_value(i, 0)
#     end = sheet.cell_value(i, 1)
#     type = sheet.cell_value(i, 2)
#     lng = float(start.split(',')[0])
#     lat = float(start.split(',')[1])
#     lng1 = float(end.split(',')[0])
#     lat1 = float(end.split(',')[1])
#     url = 'https://restapi.amap.com/v3/geocode/regeo?key=2be4c36d53e74e0c585326d62d6fe6e3&location=%s,%s&poitype=&radius=1000&extensions=base&batch=false&roadlevel=0' % (lng, lat)
#     data = json.loads(requests.get(url).text)
#     start_place = (data['regeocode']['formatted_address'])
#     url = 'https://restapi.amap.com/v3/geocode/regeo?key=2be4c36d53e74e0c585326d62d6fe6e3&location=%s,%s' \
#           '&poitype=&radius=1000&extensions=base&batch=false&roadlevel=0' % (lng1, lat1)
#     data = json.loads(requests.get(url).text)
#     end_place = (data['regeocode']['formatted_address'])
#     url = "https://restapi.amap.com/v3/direction/driving?origin=%s,%s&destination=%s,%s&key=2be4c36d53e74e0c585326d62d6fe6e3"%(lng,lat,lng1,lat1)
#     data = json.loads(requests.get(url).text)
#     dis=(data['route']['paths'][0]['distance'])
#     print(end_place)
#     # print(dis)
#
#     arr.append({
#         'point': [lng, lat],
#         'type': 'DarkSalmon ' if type == "黄色" else 'Crimson',
#         'desc': start_place
#     })
#     arr1.append({
#         'point': [lng1, lat1],
#         'desc': end_place
#     })
# # for i in arr:
# #     print(i)
# print("var positions1=" + str(arr))
# print("var positions2=" + str(arr1))
# print(len(arr))
# print(len(arr1))
#
