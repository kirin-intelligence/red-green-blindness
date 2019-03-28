import json

import requests
import xlrd
from xlutils.copy import copy
from redis import StrictRedis, ConnectionPool

pool = ConnectionPool(host='123.56.19.49', password='wscjxky123', port=6379, db=5, decode_responses=True)
redis = StrictRedis(connection_pool=pool)


def get_place(point):
    url = 'https://restapi.amap.com/v3/geocode/regeo?key=2be4c36d53e74e0c585326d62d6fe6' \
          'e3&location=%s,%s&poitype=&radius=1000&extensions=base&batch=false&roadlevel=0' % (point[0], point[1])
    data = json.loads(requests.get(url).text)
    place = (data['regeocode']['formatted_address'])
    return place


def get_distance(start_point, end_point):
    url = "https://restapi.amap.com/v3/direction/driving?origin=%s,%s&destina" \
          "tion=%s,%s&key=2be4c36d53e74e0c585326d62d6fe6e3" % (
              start_point[0], start_point[1], end_point[0], end_point[1])
    data = json.loads(requests.get(url).text)
    dis = (data['route']['paths'][0]['distance'])
    return dis


def write_excel(points, day, start=0, gps_center=0):
    start_count = 0
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
        distance = get_distance(start_point, end_point)
        no = start_count + index
        type = point[0][2]
        worksheet.write(index, 0, label="%s" % no)
        worksheet.write(index, 1, label="%s" % start_place)
        worksheet.write(index, 2, label="%s,%s" % (start_point[0], start_point[1]))
        worksheet.write(index, 3, label="%s" % end_place)
        worksheet.write(index, 4, label="%s,%s" % (end_point[0], end_point[1]))
        worksheet.write(index, 5, label="%s" % distance)
        worksheet.write(index, 6, label="%s" % "红色" if type == 'red' else "黄色")
        # worksheet.write(index, 7, label=point)
        hset_name = "%s:%s" % (day, no)
        redis.hset(hset_name, "no", no)
        redis.hset(hset_name, "start_point", json.dumps(start_point))
        redis.hset(hset_name, "end_point", json.dumps(end_point))
        redis.hset(hset_name, "type", type)
        redis.hset(hset_name, "distance", distance)
        redis.hset(hset_name, "start_place", start_place)
        redis.hset(hset_name, "end_place", end_place)

        print(point)
        workbook.save('data.xls')


points = [[[116.35424435294117, 39.97429023357663, 'red'], [116.35452324567473, 39.97006943065693, 'red']],
          [[116.35105853979238, 39.97647454014598, 'red'], [116.35333258823528, 39.97647454014598, 'red']],
          [[116.35266753633216, 39.968041145985396, 'red'], [116.35298933564012, 39.9686816569343, 'red']],
          [[116.35497376470586, 39.96859132846715, 'red'], [116.35587480276814, 39.968238226277364, 'red']],
          [[116.36193535640136, 39.967819430656924, 'red'], [116.36358725951555, 39.967819430656924, 'red']],
          [[116.3562073287197, 39.967778372262764, 'red'], [116.35878172318337, 39.967778372262764, 'red']],
          [[116.35895334948096, 39.96781121897809, 'red'], [116.361677916955, 39.96781121897809, 'red']],
          [[116.35346130795845, 39.967778372262764, 'red'], [116.3561858754325, 39.967778372262764, 'red']],
          [[116.35072601384081, 39.9677619489051, 'red'], [116.35343985467127, 39.9677619489051, 'red']],
          [[116.3562073287197, 39.96767162043795, 'red'], [116.3585457370242, 39.96767162043795, 'red']],
          [[116.35433016608995, 39.976581291970795, 'yellow'], [116.35539210380621, 39.976581291970795, 'yellow']],
          [[116.35362220761245, 39.97656486861313, 'yellow'], [116.35411563321797, 39.97656486861313, 'yellow']],
          [[116.35346130795845, 39.967663408759115, 'yellow'], [116.35599279584774, 39.967663408759115, 'yellow']],
          [[116.36021909342558, 39.96767983211678, 'yellow'], [116.361677916955, 39.96767983211678, 'yellow']]]

day = 'morning'
write_excel(points, day)

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
# var positions1=[{'point': [116.309898, 39.934405], 'type': 'DarkSalmon ', 'desc': '北京市海淀区八里庄街道西三环北路辅路中国外文大厦'}, {'point': [116.31008, 39.93545], 'type': 'Crimson', 'desc': '北京市海淀区八里庄街道西三环北路'}, {'point': [116.31002, 39.939224], 'type': 'Crimson', 'desc': '北京市海淀区八里庄街道西三环北路金龙潭大饭店'}, {'point': [116.309374, 39.951084], 'type': 'DarkSalmon ', 'desc': '北京市海淀区紫竹院街道西三环北路辅路中国青年政治学院'}, {'point': [116.308317, 39.960205], 'type': 'DarkSalmon ', 'desc': '北京市海淀区紫竹院街道西三环北路西三环北路1号院办公楼'}]
# var positions2=[{'point': [116.309909, 39.932796], 'desc': '北京市海淀区八里庄街道西三环北路辅路西三环北路101号院'}, {'point': [116.310086, 39.934948], 'desc': '北京市海淀区八里庄街道西三环北路辅路中国外文大厦'}, {'point': [116.310015, 39.938442], 'desc': '北京市海淀区八里庄街道西三环北路辅路中化石油首石缘加油站'}, {'point': [116.309556, 39.94842], 'desc': '北京市海淀区紫竹院街道西三环北路辅路北科大厦'}, {'point': [116.30873, 39.958359], 'desc': '北京市海淀区紫竹院街道西三环北路中元国际工程大厦'}]
