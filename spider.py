import requests
filename='jiaot'
size = 600
# traffic = 1  # 是否要实况图
for i in range(2):
    data = requests.get('https://restapi.amap.com/v3/staticmap?&'
                        # 'zoom=15&size=600*600'
                        'zoom=15&size=' + str(size) + '*' + str(size) +
                        '&location=116.346942,39.954295&'
                        'scale=2&'
                        'traffic=' + str(i) +
                        '&key=2be4c36d53e74e0c585326d62d6fe6e3')
    with open(filename+str(i)+'.png', 'wb') as file:
        file.write(data.content)


size = 600
filename='test'
for i in range(2):
    data = requests.get('https://restapi.amap.com/v3/staticmap?&'
                        # 'zoom=15&size=600*600'
                        'zoom=15&size=' + str(size) + '*' + str(size) +
                        '&location=116.352615,39.908664&'
                        'scale=2&'
                        'traffic=' + str(i) +
                        '&key=2be4c36d53e74e0c585326d62d6fe6e3')
    with open(filename+str(i)+'.png', 'wb') as file:
        file.write(data.content)
