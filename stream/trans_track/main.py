import os
from util import *
import cv2
from config import *
from xlr import write_excel

time_lst = ['07', '08']
# [116.356362, 39.92162, 'red'], [116.356013, 39.929951, 'red']


def way_of_read(GPS_C):
    file_dir = "preusage_data/"
    # GPS_C = '116.35716199999999_39.917876'
    check_lst = []
    for time in time_lst:
        time_str = str(time) + "_" + GPS_C + ".npy"
        check_lst.append(time_str)
    X = 0
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if file in check_lst:
                hot_map = np.load(os.path.join(root, file))
                X += hot_map
    count = X[0, 0]
    X[0, 0] = 0
    total_time = count * 2
    X = X / total_time
    GPS_f = [float(x) for x in GPS_C.split('_')]
    return X, count, GPS_f


if __name__ == '__main__':
    # x_list = [x1 + i * x_step for i in range(x_count)]
    # y_list = [y1 - i * y_step for i in range(y_count)]
    # print(len(x_list))
    # print(len(y_list))
    # start = 0
    # for x in x_list:
    #     for y in y_list:
    #         hmap, c, GPS_float = way_of_read('%s_%s' % (x, y))
    #         final, red, yellow, green = run_rgb(hmap, c)
    #         ans, point_map = report(final, GPS_float)
    #         print(ans)
    #         start += write_excel(ans, 'morning', start)
    #
    #         cv2.imshow(" ", point_map)
    #         cv2.waitKey(0)
    #         cv2.destroyAllWindows()
    gps = [[[116.355896, 39.929737, 'red'], [116.356218, 39.922332, 'red']],
           [[116.356229, 39.922184, 'red'],
            [116.356593, 39.91407, 'red']],
           [[116.356593, 39.913976, 'red'],
            [116.356406, 39.909688, 'red']],
           [[116.356395, 39.908544, 'red'],
            [116.356443, 39.9074, 'red']],
           [[116.356481, 39.910577, 'red'],
            [116.355789, 39.907972, 'red']],
           [[116.355692, 39.931699, 'red'],
            [116.355762, 39.929737, 'red']],
           [[116.355767, 39.929338, 'red'],
            [116.355832, 39.927536, 'red']],
           [[116.355842, 39.92738, 'red'],
            [116.355955, 39.92464, 'red']],
           [[116.356046, 39.922727, 'red'],
            [116.356234, 39.918703, 'red']],
           [[116.35654, 39.911869, 'red'],
            [116.356288, 39.910256, 'red']],
           [[116.356497, 39.908754, 'red'],
            [116.35676, 39.913223, 'red']]]
    start = 1136
    start = write_excel(gps, 'morning', start)
    print(start)