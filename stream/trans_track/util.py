import numpy as np
import cv2

alpha = 0.8
belta = 0.5
gama = 0.3

color_dic = {'RED_l': np.array([0, 0, 220]), 'RED_h': np.array([0, 0, 222]),
             'YELLO_l': np.array([0, 202, 253]), 'YELLO_h': np.array([0, 204, 255]),
             'GREEN_l': np.array([0, 175, 49]), 'GREEN_h': np.array([0, 177, 51]),
             'DEEPRED_l': np.array([13, 13, 138]), 'DEEPRED_h': np.array([13, 13, 140]), }


def get_line(frame):
    # get mask
    r = cv2.inRange(frame, color_dic['RED_l'], color_dic['RED_h'])
    y = cv2.inRange(frame, color_dic['YELLO_l'], color_dic['YELLO_h'])
    g = cv2.inRange(frame, color_dic['GREEN_l'], color_dic['GREEN_h'])
    dr = cv2.inRange(frame, color_dic['DEEPRED_l'], color_dic['DEEPRED_h'])
    mask = r + y + g + dr
    res = cv2.bitwise_and(frame, frame, mask=mask)
    return res, g, y, r, dr


def run_rgb(hmap, count):
    print(count)
    print(np.max(hmap))
    red_ori = hmap > alpha
    yellow_ori = (hmap > belta) & (hmap <= alpha)
    green_ori = (hmap <= belta) & (hmap > gama)

    red = red_ori[:, :, np.newaxis]
    yellow = yellow_ori[:, :, np.newaxis]
    green = green_ori[:, :, np.newaxis]

    red = np.repeat(red, 3, axis=2)
    yellow = np.repeat(yellow, 3, axis=2)
    green = np.repeat(green, 3, axis=2)

    red = red * color_dic['RED_l']
    yellow = yellow * color_dic['YELLO_l']
    green = green * color_dic['GREEN_l']

    final = red + yellow + green
    final = np.asarray(final, dtype=np.uint8)
    return final, red, yellow, green


def head_end(tuzi_map):
    def calcul_dis(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    gray = np.uint8(tuzi_map)
    ls = cv2.HoughLinesP(gray, 1, np.pi/180, threshold=60, minLineLength=60, maxLineGap=5)
    head_max, end_max = None, None
    if ls is None:
        return head_max, end_max

    head_end = ls[:, 0, :]
    max_dis = 0
    for i in head_end:
        head = tuple(i[0: 2])
        end = tuple(i[2: 4])
        current_dis = calcul_dis(head, end)
        if current_dis > max_dis:
            max_dis = current_dis
            head_max, end_max = head, end
            # tmp = np.asarray(tuzi_map, dtype=np.uint8)
            # cv2.cvtColor(tmp, cv2.COLOR_GRAY2RGB)
            # cv2.circle(tmp, head_max, 5, color=(255, 255, 255))
            # cv2.circle(tmp, end_max, 5, color=(255, 255, 255))
            # import matplotlib.pyplot as plt
            # plt.imshow(tmp)
            # plt.show()
    return head_max, end_max


def no_eages(img):
    img[0: 50, :] = 0
    img[-50:, :] = 0
    img[:, 0: 50] = 0
    img[:, -50:] = 0
    img_without_eage = np.asarray(img, dtype=np.uint8)
    return img_without_eage


def solve(input_map):
    count = 0
    point_paer = []
    input_map = no_eages(input_map)
    tutu = cv2.resize(input_map, (500, 500))
    # cv2.imshow(" ", tutu)
    # cv2.waitKey(0)
    try:
        _, labels = cv2.connectedComponents(input_map, connectivity=8)
        labels_lst = np.reshape(labels, [-1])
        labels_lst = [x for x in range(1, _)]
        for i in labels_lst:
            single_connect = (labels == i)
            if np.sum(single_connect) > 50:
                point = head_end(single_connect)
                if point != (None, None):
                    point_paer.append(list(point))
                count += 1
    except:
        pass
    return point_paer


def la_le_point(points, type, center):
    px = 0.0124 / (1200 - 44)
    py = 0.009 / (1200 - 104)
    zero_point = [center[0] - 600 * px, center[1] - 600 * py]
    lat_points = []
    for point in points:
        lat_point = [zero_point[0] + px * point[0], zero_point[1] + py * (1200 - point[1]), type]
        lat_points.append(list(lat_point))
    return (lat_points)


def report(img, gps_centor):
    res_map, green, yellow, red, _ = get_line(img)
    ans = solve(red)
    ans_y = solve(yellow)
    ans_g = solve(green)
    result = []
    for i in ans_g:
        cv2.circle(res_map, i[0], 5, color=(255, 255, 255))
        cv2.circle(res_map, i[1], 5, color=(255, 255, 255))
        ans_g = la_le_point(i, 'green', gps_centor)
        result.append(ans_g)
    for i in ans:
        cv2.circle(res_map, i[0], 5, color=(255, 255, 255))
        cv2.circle(res_map, i[1], 5, color=(255, 255, 255))
        red = la_le_point(i, 'red', gps_centor)
        result.append(red)
    for i in ans_y:
        cv2.circle(res_map, i[0], 5, color=(255, 0, 255))
        cv2.circle(res_map, i[1], 5, color=(255, 0, 255))
        yellow = la_le_point(i, 'yellow', gps_centor)
        result.append(yellow)
    point_res_map = cv2.resize(res_map, (1024, 1024))
    return result, point_res_map
