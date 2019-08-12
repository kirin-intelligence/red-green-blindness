# import os
#
# left_point = [116.195962, 40.055176]
# right_point = [116.400582, 39.906151]
# x1 = left_point[0]
# y1 = left_point[1]
# x_step = 0.0124
# x_count = -int(((x1 - right_point[0]) // x_step) - 1)
# y_step = 0.009
# y_count = int(((y1 - right_point[1]) // y_step) + 1)
#
# special_point = []
# # special_point = [(0, 0)]
#
# size = 1200
# worktime = [7, 8, 17, 18]
#
# x1 = float(left_point[0])
# y1 = float(left_point[1])
# x2 = float(right_point[0])
# y2 = float(right_point[1])
# x_step = 0.0124
# y_step = 0.009
# x_count = -int(((x1 - x2) // x_step) - 1)
# y_count = int(((y1 - y2) // y_step) + 1)
# import shutil
#
# x_list = [x1 + i * x_step for i in range(x_count)][8:-3]
# y_list = [y1 - i * y_step for i in range(y_count)][8:-3]
# point_lst = [(x, y) for x in x_list for y in y_list]
# # for sp in config.special_point:
# #     point_lst.append(sp)
# t_lst = []
# print((point_lst))
# for p in point_lst:
#     for root, dirs, files in os.walk("C:/Users/tsq/Desktop/work/red-green-blindness/demo/data_ori"):
#         for file in files:
#                 # print(root)
#                 # os.mkdir("../data/"+root)
#                 if f"{p[0]}_{p[1]}"in file:
#                     print(file)
#                     shutil.copy(root +'/'+ file, root.replace('data_ori','data')+'/' + file)
#
#
# #

import os
import os.path

arr_l = ['dll', 'py', 'pyc', 'npz', 'txt','xlsx','xlm','lib']


def dfs_showdir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")

    for item in os.listdir(path):
        flag = True

        newitem = path + '/' + item
        if 'lib' in newitem:
            continue
        if 'platforms' in newitem:
            continue
        if os.path.isdir(newitem):
            print("| " * depth + "+--" + item)
            dfs_showdir(newitem, depth + 1)



if __name__ == '__main__':
    dfs_showdir('C:/Users/tsq/Desktop/work/red-green-blindness/demo/build/transport', 0)
