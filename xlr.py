import json

import xlrd

readbook = xlrd.open_workbook(r'/home/kaiyuan_xu/Downloads/evening.xlsx')
sheet = readbook.sheet_by_index(0)
nrows = sheet.nrows
ncols = sheet.ncols
arr = []
import requests

arr1 = []
for i in range(1, nrows):
    start = sheet.cell_value(i, 0)
    end = sheet.cell_value(i, 1)
    type = sheet.cell_value(i, 2)
    lng = float(start.split(',')[0])
    lat = float(start.split(',')[1])
    lng1 = float(end.split(',')[0])
    lat1 = float(end.split(',')[1])
    url = 'https://restapi.amap.com/v3/geocode/regeo?key=2be4c36d53e74e0c585326d62d6fe6e3&location=%s,%s' \
          '&poitype=&radius=1000&extensions=base&batch=false&roadlevel=0'%(lng,lat)
    data=json.loads(requests.get(url).text)
    start_place=(data['regeocode']['formatted_address'])
    url = 'https://restapi.amap.com/v3/geocode/regeo?key=2be4c36d53e74e0c585326d62d6fe6e3&location=%s,%s' \
          '&poitype=&radius=1000&extensions=base&batch=false&roadlevel=0'%(lng1,lat1)
    data=json.loads(requests.get(url).text)
    end_place=(data['regeocode']['formatted_address'])
    arr.append({
        'point': [lng, lat],
        'type': 'darkorange' if type == "橙色" else 'red',
        'desc':start_place
    })
    arr1.append({
        'point': [lng1, lat1],
        'desc':end_place
    })
print("var positions1=" + str(arr))
print("var positions2=" + str(arr1))
print(len(arr))
print(len(arr1))
