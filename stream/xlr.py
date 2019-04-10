import json

import requests
import xlrd
from xlutils.copy import copy
from redis import StrictRedis, ConnectionPool

pool = ConnectionPool(host='123.56.19.49', password='wscjxky123', port=6379, db=8, decode_responses=True)
redis = StrictRedis(connection_pool=pool)

def write_excel(day='evening'):

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
    for index,k in enumerate(redis.keys('evening*')):
        start_point = redis.hget(k,'start_point').strip('[').strip(']')
        print(start_point)
        end_point = redis.hget(k,'end_point').strip('[').strip(']')
        start_place = redis.hget(k,'start_place')
        end_place = redis.hget(k,'end_place')
        distance = redis.hget(k,'distance')
        no = int(redis.hget(k,'no'))
        type = redis.hget(k,'type')
        worksheet.write(no+1, 0, label="%s" % no)
        worksheet.write(no+1, 1, label="%s" % start_place)
        worksheet.write(no+1, 2, label="%s,%s" % (start_point, start_point))
        worksheet.write(no+1, 3, label="%s" % end_place)
        worksheet.write(no+1, 4, label="%s,%s" % (end_point, end_point))
        worksheet.write(no+1, 5, label="%s" % distance)
        if type=='red':
            color='红色'
        elif type=='yellow':
            color='橙黄'
        else:
            color='黄色'
        worksheet.write(no, 6, label=color)
        # worksheet.write(index, 7, label=point)
        # break


    workbook.save('data.xls')

write_excel()
