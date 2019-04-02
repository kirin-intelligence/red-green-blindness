import os
from util import *
import cv2
from web.backup.config import *
from web.backup.xlr import write_excel

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
    x_list = [x1 + i * x_step for i in range(x_count)]
    y_list = [y1 - i * y_step for i in range(y_count)]
    print(len(x_list))
    print(len(y_list))
    start = 0
    for x in x_list:
        for y in y_list:
            hmap, c, GPS_float = way_of_read('%s_%s' % (x, y))
            final, red, yellow, green = run_rgb(hmap, c)
            ans, point_map = report(final, GPS_float)
            print(ans)
            start += write_excel(ans, 'morning', start)

            cv2.imshow(" ", point_map)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
