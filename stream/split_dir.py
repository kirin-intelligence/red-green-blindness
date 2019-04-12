import os
import shutil
from datetime import datetime

import time


def time_to_string(t):
    return time.strftime("%Y-%m-%d-%H_%M_%S", t)


def string_to_time(t):
    return datetime.strptime(t, "%Y-%m-%d-%H_%M_%S")


def main():
    for r, d, f in os.walk("../input_img"):
        for file in f:
            if file.endswith('png'):
                t = (string_to_time(file[:-4]))
                if 7 <= t.hour < 9:
                    shutil.copy("../input_img/" + file, '/morning')
                    shutil.copy("../input_img/" + file, '/day')

                elif 17 <= t.hour < 19:
                    shutil.copy("../input_img/" + file, '/evening')
                    shutil.copy("../input_img/" + file, '/day')


def spilt_file(dir_name, target_dir):
    with open(dir_name + 'filenames.txt', 'r')as f:
        with open(target_dir + 'morning.txt', 'w')as f_m:
            with open(target_dir + 'evening.txt', 'w')as f_e:
                lines = f.readlines()
                for file in lines:
                    file = file.strip('\n')
                    time_str = file[:len('2019-03-21-15_04_11')]
                    print(time_str)
                    if file.endswith('png'):
                        t = (string_to_time(time_str))
                        if 7 <= t.hour < 9:
                            if os.path.exists(dir_name + file):
                                continue
                            shutil.copy(dir_name + 'images/' + file, target_dir + 'morning')
                            f_m.write(target_dir + 'morning/' + file + '\n')
                            # shutil.copy("total_img/"+file,'day')
                        elif 17 <= t.hour < 19:
                            if os.path.exists(dir_name + file):
                                continue
                            shutil.copy(dir_name + 'images/' + file, target_dir + 'evening')
                            f_e.write(target_dir + 'evening/' + file + '\n')

                            # shutil.copy("total_img/"+file,'day')


day = ['03-25', '03-26', '03-27', '03-28', '03-29']


def spilit_point(p):
    dir_name = '/run/media/kirin/新加卷/server/'
    with open(dir_name + 'filenames.txt', 'r')as f:
        lines = f.readlines()
        for file in lines:
            file = file.strip('\n')
            if p in file:
                for d in day:
                    if d in file:
                        if '-17_' in file or '-18_' in file:
                            print(dir_name + file)
                            shutil.copy(dir_name +"images/"+ file,
                                        '/home/kirin/Python_Code/red-green-blindness/video_maker/evening_xierhuan')


spilit_point('116.35716199999999_39.917876')
# spilit_point('116.35716199999999_39.944875999999994')
# spilit_point('116.35716199999999_39.93587599999999')

# spilit_lng()
