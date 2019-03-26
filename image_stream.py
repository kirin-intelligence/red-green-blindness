import requests
import time


def get_time():
    return time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


while True:
    url = (
    'https://restapi.amap.com/v3/staticmap?&zoom=14&size=1024*1024&location=116.309833,39.948593&scale=2&traffic=1&key=2be4c36d53e74e0c585326d62d6fe6e3')
    data = requests.get(url)
    with open('stream/%s.png' % get_time(), 'wb') as file:
        file.write(data.content)
    print(url)
    time.sleep(120)
