import os
import cv2
import numpy as np
import datetime

path = '/home/kirin/Python_Code/red-green-blindness/video_maker/morning/'
Out_path = '/home/kirin/Python_Code/red-green-blindness/video_maker/output_video/OutPut_aft.mp4'
filelist = os.listdir(path)

fps = 24
size = (4096, 2048)

color_dic = {'RED_l': np.array([0, 0, 220]), 'RED_h': np.array([0, 0, 222]),
             'YELLO_l': np.array([0, 202, 253]), 'YELLO_h': np.array([0, 204, 255]),
             'GREEN_l': np.array([0, 175, 49]), 'GREEN_h': np.array([0, 177, 51]),
             'DEEPRED_l': np.array([13, 13, 138]), 'DEEPRED_h': np.array([13, 13, 140]), }


def Time_mark(img, str):
    color = (100, 100, 100)
    # time_str = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    time_str = str
    cv2.putText(img, time_str, (1500, 1800), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 2)
    return img


def get_line(frame):
    # get mask
    r = cv2.inRange(frame, color_dic['RED_l'], color_dic['RED_h'])
    y = cv2.inRange(frame, color_dic['YELLO_l'], color_dic['YELLO_h'])
    g = cv2.inRange(frame, color_dic['GREEN_l'], color_dic['GREEN_h'])
    dr = cv2.inRange(frame, color_dic['DEEPRED_l'], color_dic['DEEPRED_h'])
    mask = r + y + g + dr
    # mask = g
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # return res, g, y, r, dr
    return res


fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
video = cv2.VideoWriter(Out_path, fourcc, fps, size)

filelist.sort()

for index, item in enumerate(filelist):
    try:
        if item.endswith('.png'):
            name_str = item.split('.')[0]
            item = path + item
            img = cv2.imread(item)
            aft_img = get_line(img)
            img = np.hstack([aft_img, img])
            img = Time_mark(img, name_str)
            print(item)
            for i in range(2):
                video.write(img)
    except:
        print('erro!')
        pass

video.release()
cv2.destroyAllWindows()
