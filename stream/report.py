import cv2
import numpy as np
import matplotlib.pyplot as plt
color_dic = {'RED_l': np.array([0, 0, 220]), 'RED_h': np.array([0, 0, 222]),
             'YELLO_l': np.array([0, 202, 253]), 'YELLO_h': np.array([0, 204, 255]),
             'GREEN_l': np.array([0, 175, 49]), 'GREEN_h': np.array([0, 177, 51]),
             'DEEPRED_l': np.array([13, 13, 138]), 'DEEPRED_h': np.array([13, 13, 140]), }
def report(img,gps_centor):
    # img = cv2.imread(img_path)
    res_map, yellow, red = get_line(img)
    ans = solve(red)
    ans_y = solve(yellow)
    result=[]
    for i,j in zip(ans,ans_y):
        red = la_le_point(i, 0,gps_centor)

        yellow = la_le_point(i, 1,gps_centor)
        result.append(red)
        result.append(yellow)
    print(result)

    #
    # for i in ans:
    #     cv2.circle(res_map, i[0], 5, color=(255, 255, 255))
    #     cv2.circle(res_map, i[1], 5, color=(255, 255, 255))
    #
    # for i in ans_y:
    #     cv2.circle(res_map, i[0], 5, color=(255, 0, 255))
    #     cv2.circle(res_map, i[1], 5, color=(255, 0, 255))

    res_map = cv2.resize(res_map, (1200, 1200))

    cv2.imwrite("out_put.png", res_map)



def get_line(frame):
    # get mask
    r = cv2.inRange(frame, color_dic['RED_l'], color_dic['RED_h'])
    y = cv2.inRange(frame, color_dic['YELLO_l'], color_dic['YELLO_h'])
    mask = r + y
    res = cv2.bitwise_and(frame, frame, mask=mask)
    return res, y, r


def head_end(tuzi_map):
    # plt.imshow(tuzi_map)
    # plt.show()

    gray = np.uint8(tuzi_map)
    ls = cv2.HoughLinesP(gray, 1, np.pi / 60, 30, minLineLength=20, maxLineGap=40)

    head, end = None, None

    if ls is None:
        return head, end

    head_end = ls[:, 0, :]
    # print(head_end)

    for i in head_end:
        # cv2.circle(test_img, tuple(i[0: 2]), 5, color=(0, 0, 255))
        # cv2.circle(test_img, tuple(i[2: 4]), 5, color=(0, 0, 255))
        head = tuple(i[0: 2])
        end = tuple(i[2: 4])
        break

    return head, end

def la_le_point(points,type, center):
    px = 0.0124 / (1200 - 44)
    py = 0.009 / (1200 - 104)
    zero_point = [center[0] - 600 * px, center[1] - 600 * py]
    lat_points=[]
    for point in points:
        lat_point=[zero_point[0] + px * point[0], zero_point[1] + py * (1200 - point[1]),type]
        lat_points.append(list(lat_point))
    return (lat_points)
def solve(input_map):
    _, labels = cv2.connectedComponents(input_map, connectivity=8)

    labels_lst = np.reshape(labels, [-1])
    labels_lst = list(set(labels_lst))
    labels_lst.remove(0)

    count = 0

    point_paer = []

    for i in labels_lst:
        single_connect = (labels == i)
        if np.sum(single_connect) > 50:
            point = head_end(single_connect)
            if point != (None, None):
                point_paer.append(list(point))
            count += 1
    return point_paer


