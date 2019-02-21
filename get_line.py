import numpy as np
import cv2

filename = 'data/data2.png'

img = cv2.imread(filename)

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
    # mask = g

    res = cv2.bitwise_and(frame, frame, mask=mask)
    return res, g, y, r, dr


def find_point(res, g, y, r, dr):
    # point -> List: OpenCv 的点坐标是反着的 (y, x)
    dst = cv2.cornerHarris(g, 7, 9, 0.04)
    dst = cv2.dilate(dst, None)
    g[dst < 0.01 * dst.max()] = 0

    dst = cv2.cornerHarris(y, 7, 9, 0.04)
    dst = cv2.dilate(dst, None)
    y[dst < 0.01 * dst.max()] = 0

    dst = cv2.cornerHarris(r, 7, 9, 0.04)
    dst = cv2.dilate(dst, None)
    r[dst < 0.01 * dst.max()] = 0

    dst = cv2.cornerHarris(dr, 7, 9, 0.04)
    dst = cv2.dilate(dst, None)
    dr[dst < 0.01 * dst.max()] = 0

    def have(pix):
        if np.sum(pix) > 0:
            return 1
        else:
            return 0
    point = []

    step = 10
    l_step = res.shape[0] // step
    w_step = res.shape[1] // step
    for i in range(l_step):
        for j in range(w_step):
            status = have(g[step * i:step * (i + 1), step * j:step * (j + 1)]) + have(
                y[step * i:step * (i + 1), step * j:step * (j + 1)]) + have(
                r[step * i:step * (i + 1), step * j:step * (j + 1)]) + have(
                dr[step * i:step * (i + 1), step * j:step * (j + 1)])
            if status >= 2:
                point.append([int(step * (j + 0.5)), int(step * (i + 0.5))])

    for p in point:
        cv2.circle(res, tuple(p), 5, (255, 255, 255), 1)


    # cv2.imshow('Result1', res)
    # cv2.imshow('Result2', g)

    # cv2.waitKey(0)
    # if cv2.waitKey(0) & 0xff == 27:
    #     cv2.destroyAllWindows()
    return point


line_graph, g_graph, y_graph, r_graph, dr_graph = get_line(img)
point_in_img = find_point(line_graph, g_graph, y_graph, r_graph, dr_graph)
