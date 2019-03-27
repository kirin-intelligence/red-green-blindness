import json

import xlrd
import xlwt

readbook = xlrd.open_workbook(r'/home/kaiyuan_xu/Downloads/day.xlsx')
sheet = readbook.sheet_by_index(0)
nrows = sheet.nrows
ncols = sheet.ncols
arr = []
import requests

arr1 = []
for i in range(0, nrows):
    start = sheet.cell_value(i, 0)
    end = sheet.cell_value(i, 1)
    type = sheet.cell_value(i, 2)
    lng = float(start.split(',')[0])
    lat = float(start.split(',')[1])
    lng1 = float(end.split(',')[0])
    lat1 = float(end.split(',')[1])
    url = 'https://restapi.amap.com/v3/geocode/regeo?key=2be4c36d53e74e0c585326d62d6fe6e3&location=%s,%s&poitype=&radius=1000&extensions=base&batch=false&roadlevel=0' % (lng, lat)
    data = json.loads(requests.get(url).text)
    start_place = (data['regeocode']['formatted_address'])
    url = 'https://restapi.amap.com/v3/geocode/regeo?key=2be4c36d53e74e0c585326d62d6fe6e3&location=%s,%s' \
          '&poitype=&radius=1000&extensions=base&batch=false&roadlevel=0' % (lng1, lat1)
    data = json.loads(requests.get(url).text)
    end_place = (data['regeocode']['formatted_address'])
    url = "https://restapi.amap.com/v3/direction/driving?origin=%s,%s&destination=%s,%s&key=2be4c36d53e74e0c585326d62d6fe6e3"%(lng,lat,lng1,lat1)
    data = json.loads(requests.get(url).text)
    dis=(data['route']['paths'][0]['distance'])
    print(end_place)
    # print(dis)

    arr.append({
        'point': [lng, lat],
        'type': 'DarkSalmon ' if type == "黄色" else 'Crimson',
        'desc': start_place
    })
    arr1.append({
        'point': [lng1, lat1],
        'desc': end_place
    })
# for i in arr:
#     print(i)
print("var positions1=" + str(arr))
print("var positions2=" + str(arr1))
print(len(arr))
print(len(arr1))

var positions1=[{'point': [116.309898, 39.934405], 'type': 'DarkSalmon ', 'desc': '北京市海淀区八里庄街道西三环北路辅路中国外文大厦'}, {'point': [116.31008, 39.93545], 'type': 'Crimson', 'desc': '北京市海淀区八里庄街道西三环北路'}, {'point': [116.31002, 39.939224], 'type': 'Crimson', 'desc': '北京市海淀区八里庄街道西三环北路金龙潭大饭店'}, {'point': [116.309374, 39.951084], 'type': 'DarkSalmon ', 'desc': '北京市海淀区紫竹院街道西三环北路辅路中国青年政治学院'}, {'point': [116.308317, 39.960205], 'type': 'DarkSalmon ', 'desc': '北京市海淀区紫竹院街道西三环北路西三环北路1号院办公楼'}]
var positions2=[{'point': [116.309909, 39.932796], 'desc': '北京市海淀区八里庄街道西三环北路辅路西三环北路101号院'}, {'point': [116.310086, 39.934948], 'desc': '北京市海淀区八里庄街道西三环北路辅路中国外文大厦'}, {'point': [116.310015, 39.938442], 'desc': '北京市海淀区八里庄街道西三环北路辅路中化石油首石缘加油站'}, {'point': [116.309556, 39.94842], 'desc': '北京市海淀区紫竹院街道西三环北路辅路北科大厦'}, {'point': [116.30873, 39.958359], 'desc': '北京市海淀区紫竹院街道西三环北路中元国际工程大厦'}]
