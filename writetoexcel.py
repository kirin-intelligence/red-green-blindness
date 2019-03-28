import xlwt
import xlrd
import xlutils.copy
import xlwt
import xlsxwriter
workbook = xlwt.Workbook()
worksheet=workbook.add_sheet('0')
from config import *

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
