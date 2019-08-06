import os
import numpy as np
import util
import datetime
from main_road import *
from gen_json import  *
begin_time = (2019, 6, 29, 8)
end_time = (2019, 6, 29, 17)

date_begin_time = datetime.datetime(begin_time[0], begin_time[1], begin_time[2], begin_time[3])
date_end_time = datetime.datetime(end_time[0], end_time[1], end_time[2], end_time[3])

days_count = (date_end_time - date_begin_time).days + 1

days_lst = []
hours_lst = []


if __name__ == '__main__':
    Hotmap_DIR = {}
    count_DIR = {}
    is_main_road = True

    for root, dirs, files in os.walk("data/", topdown=False):
        for name in files:
            current_time = datetime.datetime(int(name.split("_")[0]), int(name.split("_")[1]), int(name.split("_")[2]), int(name.split("_")[3]))
            # if (current_time >= date_begin_time) and (current_time <= date_end_time):
            # 如果这个点在主干道里进入循环，否则pass
            if is_main_road(point):
                try:
                    hours_lst.append(current_time)
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
                else:
                    pass
    total_ans = []
    for k in Hotmap_DIR:
        GPS_float = (float(k.split('_')[0]), float(k.split('_')[1]))
        final, red, yellow, green = util.run_rgb(Hotmap_DIR[k], count_DIR[k])
        ans, point_map = util.report(final, GPS_float, Hotmap_DIR[k])
        new_ans = util.cal_length(ans)
        total_ans.extend(ans)

    # 判断是否为主干道路
    is_main_road = True
    if is_main_road:
        total_ans = reflush_main_road(total_ans)


    # 比例调节！！！！！！！！
    # K是调节参数，k=10大约是一比一，路程为km，时间为小时
    K = 0.8

    total_ans.sort(key=lambda x: K*x[2]+(1-K)*x[3], reverse=True)
    print(total_ans)
    write_to_json(total_ans)

    print()
    print("TOTAL_DAYS:{}, TOTAL_HOURS:{}".format(days_count, len(set(hours_lst))))
