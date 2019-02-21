# https://lbs.amap.com/api/webservice/guide/api/staticmaps/
import requests
filename = 'fuckdu'
size = 600

for i in range(2):
    data = requests.get('https://restapi.amap.com/v3/staticmap?&'
                        'zoom=15&size=' + str(size) + '*' + str(size) +
                        '&location=116.441119,39.901121&'
                        'scale=2&'
                        'traffic=' + str(i) +
                        '&key=2be4c36d53e74e0c585326d62d6fe6e3')
    with open(filename + str(i) + '.png', 'wb') as file:
        file.write(data.content)
#
# size = 600
# filename = 'test'
# for i in range(2):
#     data = requests.get('https://restapi.amap.com/v3/staticmap?&'
#                         'zoom=17&size=' + str(size) + '*' + str(size) +
#                         '&location=116.352615,39.908664&'
#                         'scale=2&'
#                         'traffic=' + str(i) +
#                         '&key=2be4c36d53e74e0c585326d62d6fe6e3')
#     with open(filename + str(i) + '.png', 'wb') as file:
#         file.write(data.content)
