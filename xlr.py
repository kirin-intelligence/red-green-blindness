import xlrd
readbook = xlrd.open_workbook(r'Book1.xlsx')
sheet = readbook.sheet_by_index(0)
nrows = sheet.nrows
ncols = sheet.ncols
arr=[]
arr1=[]
for i in range(3,nrows):
    start = sheet.cell_value(i,2)
    end = sheet.cell_value(i, 6)
    start_place=sheet.cell_value(i,0)
    end_place=sheet.cell_value(i,4)
    minute=0
    type=sheet.cell_value(i,9)
    length=sheet.cell_value(i,8)
    print(start_place,end_place,type,length)
    lng=float(start.split(',')[0])
    lat=float(start.split(',')[1])
    lng1=float(end.split(',')[0])
    lat1=float(end.split(',')[1])
    arr.append({
        'point':[lng,lat],
        'desc':start_place,
        'type':'yellow' if type =="橙色" else 'red',
        'length':length
    })
    arr1.append({
        'point':[lng1,lat1],
        'desc':end_place,
    })
print(arr)
print(len(arr))
print(len(arr1))