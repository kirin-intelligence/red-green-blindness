import json

import requests

GAODE_KEY = '2be4c36d53e74e0c585326d62d6fe6e3'


def get_place(point):
    url = 'https://restapi.amap.com/v3/geocode/regeo?key=2be4c36d53e74e0c585326d62d6fe6' \
          'e3&location=%s,%s&poitype=&radius=1000&extensions=base&batch=false&roadlevel=0' % (point[0], point[1])
    data = json.loads(requests.get(url).text)
    place = (data['regeocode']['formatted_address'])
    return place


def get_driving_data(start_point, end_point):
    print(start_point,end_point)
    waypoint = [116.379779,39.94678]
    url = f"https://restapi.amap.com/v3/direction/driving?origin={start_point[0]},{start_point[1]}" \
      f"&destination={end_point[0]},{end_point[1]}&strategy=2&waypoints={waypoint[0]},{waypoint[1]}&extension=all&key=" \
      f"{GAODE_KEY}"
    data_first = json.loads(requests.get(url).text)['route']['paths'][0]
    print(data_first)

    return data_first


def get_line_road(start_p, end_p):
    line_url = f'https://restapi.amap.com/v3/distance?origins={start_p[0]},{start_p[1]}&' \
        f'type=0&destination={end_p[0]},{end_p[1]}&key={GAODE_KEY}'
    dis = json.loads(requests.get(line_url).text)['results'][0]['distance']
    polyline = [start_p, end_p]
    return dis, polyline



def get_right_steps(s_point, e_point):
    data_first = get_driving_data(s_point, e_point)
    data_second = get_driving_data(e_point, s_point)
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
        return get_line_road(s_point,e_point)

    # elif "左转" in str(right_steps) or "右转" in str(right_steps):
    #     return get_line_road(s_point,e_point)
    for step in right_steps:
        polylines = step['polyline']
        polylines = polylines.split(';')
        for point in polylines:
            point = point.split(',')
            new_point = [float(p) for p in point]
            new_polylines.append(new_point)
    return right_dis, new_polylines


if __name__ == '__main__':
    point = [
      116.3795485051903,
      39.945394065693435
    ]
    e_point = [
      116.37997757093426,
      39.948120343065696
    ]
    p = get_place(point)

    dis, polylines = get_right_steps(e_point, point)

    print(dis, polylines)
