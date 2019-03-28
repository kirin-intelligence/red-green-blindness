import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

alpha=0.15
belta=0.11
day='morning'
path = '/home/kirin/Python_Code/red-green-blindness/video_maker/final/'+day+'/'

Out_path = '/home/kirin/Python_Code/red-green-blindness/video_maker/output_video/OutPut_aft.mp4'
filelist = os.listdir(path)

input_dir='/run/media/kirin/新加卷1/images/'
path=input_dir
filelist = []
with open(input_dir+day+'.txt','r')as f:
    ls=f.readlines()
    for l in ls:
        l=l.strip('\n')
        # if l[len('2019-03-21-15_04_11_'):-len('.png')] =='116.394362_39.93587599999999':
        filelist.append(input_dir+day+'/'+l)

print(filelist)
a=Image.open(filelist[0])
a.show()
exit()
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
    return mask, g, y, r, dr
    # return res


filelist.sort()

hot_map = 0
count = 0
for index, item in enumerate(filelist):
    try:
        if item.endswith('.png'):
            name_str = item.split('.')[0]
            # item = path + item
            img = cv2.imread(item)

            aft_img, g, y, r, dr = get_line(img)
            hot_map += 0 * np.sign(g) + 0 * np.sign(y) + 2 * np.sign(r) + 2 * np.sign(dr)
            count += 1
            print(item)
    except Exception as e:
        print(e)
        print('erro!')
        pass

hot_map += 1 * np.sign(g) + 1 * np.sign(y) + 1 * np.sign(r) + 1 * np.sign(dr)

total_time = count * 2

map = hot_map / total_time


# np.save("data.npy", map)

print(count)

# map = np.load("data.npy")

print(np.max(map))


red = map > alpha
yellow = (map > belta) & (map <= alpha)
green = (map <= belta) & (map > 0)

red = red[:, :, np.newaxis]
yellow = yellow[:, :, np.newaxis]
green = green[:, :, np.newaxis]

red = np.repeat(red, 3, axis=2)
yellow = np.repeat(yellow, 3, axis=2)
green = np.repeat(green, 3, axis=2)

red = red * color_dic['RED_l']
yellow = yellow * color_dic['YELLO_l']
green = green * color_dic['GREEN_l']

final = red + yellow + green

cv2.imwrite(day+"_final.png", final)
