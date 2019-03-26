import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("/home/kirin/Python_Code/red-green-blindness/report_statement/final.png")

color_dic = {'RED_l': np.array([0, 0, 220]), 'RED_h': np.array([0, 0, 222]),
             'YELLO_l': np.array([0, 202, 253]), 'YELLO_h': np.array([0, 204, 255]),
             'GREEN_l': np.array([0, 175, 49]), 'GREEN_h': np.array([0, 177, 51]),
             'DEEPRED_l': np.array([13, 13, 138]), 'DEEPRED_h': np.array([13, 13, 140]), }


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


def solve(input_map):
    _, labels = cv2.connectedComponents(input_map, connectivity=8)

    labels_lst = np.reshape(labels, [-1])
    labels_lst = list(set(labels_lst))
    labels_lst.remove(0)

    print(len(labels_lst))

    count = 0

    point_paer = []

    for i in labels_lst:
        single_connect = (labels == i)
        if np.sum(single_connect) > 50:
            point = head_end(single_connect)
            if point != (None, None):
                point_paer.append(point)
            count += 1

    print(count)
    return point_paer


res_map, yellow, red = get_line(img)

ans = solve(red)
ans_y = solve(yellow)

for i in ans:
    cv2.circle(res_map, i[0], 5, color=(255, 255, 255))
    cv2.circle(res_map, i[1], 5, color=(255, 255, 255))

for i in ans_y:
    cv2.circle(res_map, i[0], 5, color=(255, 0, 255))
    cv2.circle(res_map, i[1], 5, color=(255, 0, 255))

res_map = cv2.resize(res_map, (1024, 1024))

cv2.imwrite("out_put.png", res_map)

