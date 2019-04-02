import requests

url = ('https://restapi.amap.com/v3/staticmap?&zoom=14&size=1024*1024&location=116.309833,39.948593&scale=2&traffic=1&key=2be4c36d53e74e0c585326d62d6fe6e3')
data = requests.get(url)

with open('test.png', 'wb') as file:
    file.write(data.content)
print(url)

