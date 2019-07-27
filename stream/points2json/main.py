import json

import requests

GAODE_KEY = '2be4c36d53e74e0c585326d62d6fe6e3'


def get_place(point):
    url = 'https://restapi.amap.com/v3/geocode/regeo?key=2be4c36d53e74e0c585326d62d6fe6' \
          'e3&location=%s,%s&poitype=&radius=1000&extensions=base&batch=false&roadlevel=0' % (point[0], point[1])
    data = json.loads(requests.get(url).text)
    place = (data['regeocode']['formatted_address'])
    return place


def get_distance(start_point, end_point):
    waypoints = []
    url = "https://restapi.amap.com/v3/direction/driving?origin=%s,%s&destina" \
          "tion=%s,%s&strategy=2&waypoints=%s&extension=all&key=2be4c36d53e74e0c585326d62d6fe6e3" % (
              start_point[0], start_point[1], end_point[0], end_point[1], waypoints)
    data_first = json.loads(requests.get(url).text)['route']['paths'][0]

    return data_first

    # print(data_first)
    # data_second
    # paths = data['route']['paths'][0]['steps'][0]['polyline']
    # paths = paths.split(';')
    # new_paths = []
    # for point in paths:
    #     point = point.split(',')
    #     new_point = []
    #     for p in point:
    #         new_point.append(float(p))
    #     new_paths.append(new_point)
    #
    # return dis, new_paths


def get_line_road(start_p, end_p):
    line_url = f'https://restapi.amap.com/v3/distance?origins={start_p[0]},{start_p[1]}&' \
        f'type=0&destination={end_p[0]},{end_p}&key={GAODE_KEY}'
    dis = json.loads(requests.get(line_url).text)['results'][0]['distance']
    polyline = [start_p, end_p]
    return dis, polyline


def get_right_steps(s_point, e_point):
    data_first = get_distance(s_point, e_point)
    data_second = get_distance(e_point, s_point)
    dis_first = int(data_first['distance'])
    dis_second = int(data_second['distance'])
    if dis_first < dis_second:
        right_steps = data_first['steps']
        right_dis = dis_first
    else:
        # TODO
        # 判断去掉右转
        right_steps = data_second['steps']
        right_dis = dis_second

    new_polylines = []
    if right_dis > 700:
        return False
    for step in right_steps:
        polylines = step['polyline']
        polylines = polylines.split(';')
        for point in polylines:
            point = point.split(',')
            new_point = [float(p) for p in point]
            new_polylines.append(new_point)
    return right_dis, new_polylines


if __name__ == '__main__':
    point = [116.359855, 39.932406]
    e_point = [116.356319, 39.932566]
    p = get_place(point)

    dis, polylines = get_right_steps(point, e_point)

    print(dis,polylines)
