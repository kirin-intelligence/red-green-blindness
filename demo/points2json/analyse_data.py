import os
import numpy as np
import util
from util import Threshold_Time

if __name__ == '__main__':
    Hotmap_DIR = {}
    count_DIR = {}
    for root, dirs, files in os.walk("data/", topdown=False):
        for name in files:
            try:
                dir_string = name.split("_")[4] + "_" + name.split("_")[5]
                dir_string = dir_string[:-4]
                X = np.load(os.path.join(root, name))
                if dir_string in Hotmap_DIR.keys():
                    Hotmap_DIR[dir_string] += X['arr_1']
                    count_DIR[dir_string] += X['arr_0']
                else:
                    Hotmap_DIR[dir_string] = X['arr_1']
                    count_DIR[dir_string] = X['arr_0']
            except:
                pass
    total_ans = []
    for k in Hotmap_DIR:
        GPS_float = (float(k.split('_')[0]), float(k.split('_')[1]))
        final, red, yellow, green = util.run_rgb(Hotmap_DIR[k], count_DIR[k])
        ans, point_map = util.report(final, GPS_float, Hotmap_DIR[k])
        new_ans = util.cal_length(ans)
        total_ans.extend(ans)

    # 比例调节！！！！！！！！
    # K是调节参数，k=10大约是一比一，路程为km，时间为小时
    # x[0]起始点,x[1]终点 ,x[2]时间,x[3]路程
    total_ans.sort(key=lambda x: Threshold_Time * x[2] + (1 - Threshold_Time) * x[3], reverse=True)
    print(total_ans)