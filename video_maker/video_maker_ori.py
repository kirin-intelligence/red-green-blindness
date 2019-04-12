import os
import cv2
import numpy as np
import datetime

path = '/home/kirin/Python_Code/red-green-blindness/video_maker/evening_xierhuan/'
Out_path = '/home/kirin/Python_Code/red-green-blindness/video_maker/OutPut_evening_xierhuan.mp4'
filelist = os.listdir(path)

fps = 24
size = (1200, 1200)

fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
video = cv2.VideoWriter(Out_path, fourcc, fps, size)


def Time_mark(img, str):
    color = (100, 100, 100)
    # time_str = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    time_str = str
    cv2.putText(img, time_str, (1500, 1800), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    return img


filelist.sort()

for item in filelist:
    if item.endswith('.png'):
        name_str = item.split('.')[0]
        item = path + item
        img = cv2.imread(item)
        img = Time_mark(img, name_str)
        for i in range(3):
            video.write(img)

video.release()
cv2.destroyAllWindows()
