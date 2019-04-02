import xlwt

workbook = xlwt.Workbook()
worksheet=workbook.add_sheet('0')
from web.backup.config import *

keys = redis.keys('gaode:*')
for k in keys:
    time=redis.hget(k,'time')
    points=eval(redis.hget(k,'points'))
    for i,v in enumerate(points):
        worksheet.write(i,4,str(time))
        for ind,lng in enumerate(v):

            worksheet.write(i,ind, lng)


    workbook.save('a.xls')
    break
