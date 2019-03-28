import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = '/home/kirin/Python_Code/red-green-blindness/cluster/point_data/morning/'

filelist = os.listdir(path)

point_lst = []
count = 0

for item in filelist:
    name_str = item.split('.')[0]
    item = path + item
    data = open(item).read()
    data = eval(data)
    for i in data:
        for j in i:
            for k in range(j[2] * j[2]):
                point_lst.append(j[0:2])
                count += 1
    break

point_lst = np.asarray(point_lst)

max_0 = np.max(point_lst[:, 0])
max_1 = np.max(point_lst[:, 1])
min_0 = np.min(point_lst[:, 0])
min_1 = np.min(point_lst[:, 1])

x = np.asarray(point_lst[:, 0])
y = np.asarray(point_lst[:, 1])
# a = np.square(np.asarray(point_lst[:, 2])) * 0.001
x = (x - min_0) / (max_0 - min_0)
y = (y - min_1) / (max_1 - min_1)

X = np.asarray([x, y])
X = np.reshape(X, [-1, 2])


plt.scatter(x, y, c='red', alpha=0.1)

fig = plt.gcf()
fig.set_size_inches(24, 20)
fig.savefig("map.png", transparent=True)
plt.show()
