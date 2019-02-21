import matplotlib.pyplot as plt
import numpy as np
import cv2

filename = 'data/test'

g_with_line = cv2.imread(filename + '1.png')

# color_dic = {'RED_l': [221, 0, 0], 'RED_h': [0, 0, 0],
#              'YELLO_l': [254, 203, 0], 'YELLO_h': [0, 0, 0],
#              'GREEN_l': [50, 176, 0], 'GREEN_h': [0, 0, 0]}

# color_dic = {'RED_l': np.array([220, 0, 0]), 'RED_h': np.array([222, 0, 0]),
#              'YELLO_l': np.array([253, 202, 0]), 'YELLO_h': np.array([255, 204, 0]),
#              'GREEN_l': np.array([49, 175, 0]), 'GREEN_h': np.array([51, 177, 0])}

color_dic = {'RED_l': np.array([0, 0, 220]), 'RED_h': np.array([0, 0, 222]),
             'YELLO_l': np.array([0, 202, 253]), 'YELLO_h': np.array([0, 204, 255]),
             'GREEN_l': np.array([0, 175, 49]), 'GREEN_h': np.array([0, 177, 51])}


def get_line(frame):
    # get mask
    r = cv2.inRange(frame, color_dic['RED_l'], color_dic['RED_h'])
    y = cv2.inRange(frame, color_dic['YELLO_l'], color_dic['YELLO_h'])
    g = cv2.inRange(frame, color_dic['GREEN_l'], color_dic['GREEN_h'])
    mask = r + y + g

    res = cv2.bitwise_and(frame, frame, mask=mask)
    # cv2.imshow('Result', res)
    # cv2.waitKey(0)
    return res


g_line = get_line(g_with_line)
