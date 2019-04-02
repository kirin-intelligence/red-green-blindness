import os
import datetime
from util import *


def reflush_ori():
    file_dir = "original_data/"
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            os.remove(os.path.join(root, file))
    print("Reflush ORI Data Finish!")


def reflush_pre():
    file_dir = "preusage_data/"
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            os.remove(os.path.join(root, file))
    print("Reflush PRE Data Finish!")


def get_whichday(date):
    split_time = date.split("-")
    whatday = datetime.datetime(int(split_time[0]), int(split_time[1]), int(split_time[2])).strftime("%A")
    return whatday


def build_Tree(sourse_LIST):
    print("Begin Build Tree...")
    file_lst = open(sourse_LIST).readlines()
    sourse_len = len(file_lst)
    count = 0
    for filename in file_lst:
        filename = filename.strip()
        file_DATA = (filename.split("/")[-1]).split("_")
        file_date = file_DATA[0]
        weekday = get_whichday(file_date)
        target = "original_data/" + weekday + "/" + file_date
        with open(target, 'a', encoding='utf-8') as f:
            f.writelines(filename + '\n')
        count += 1
        print("wait... {}%".format(100 * count / sourse_len))
    print("Build Tree Finish!")


def build_predata():
    def get_tempimg(img_path):
        img = cv2.imread(img_path)
        mask, g, y, r, dr = get_line(img)
        hot_map = 0.001 * np.sign(g) + 0.001 * np.sign(y) + 2 * np.sign(r) + 2 * np.sign(dr)
        return hot_map

    def build_single_file(inputfile_name, file_root):
        count_dir = {}
        data_dir = {}
        with open(os.path.join(file_root, inputfile_name), 'r', encoding='utf-8') as f:
            files = f.readlines()
            print("{} len : {}".format(inputfile_name, len(files)))
            files.sort(key=lambda x: x.split('_')[4])
            files.sort(key=lambda x: x.split('_')[3])
            for filename in files:
                try:
                    filename = filename.strip()
                    tmp_img = get_tempimg(filename)
                    feature = ((filename[:-4].split("/")[-1])).split('_')
                    key_str = feature[3] + "_" + feature[4]
                    if key_str in data_dir.keys():
                        data_dir[key_str] += tmp_img
                        count_dir[key_str] += 1
                    else:
                        data_dir[key_str] = tmp_img
                        count_dir[key_str] = 1
                except:
                    pass

        clock_time = inputfile_name.split('-')[-1]
        target_root = file_root.replace("original", "preusage")
        for key in data_dir.keys():
            file_target = os.path.join(target_root, str(clock_time) + "_" + key) + '.npy'
            data_dir[key][0, 0] = count_dir[key]
            if os.path.exists(file_target):
                X = np.load(file_target)
                np.save(file_target, data_dir[key] + X)
            else:
                np.save(file_target, data_dir[key])

    file_dir = "original_data/"
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            build_single_file(file, root)
            print("{} is finish!".format(file))
    print("Build Predata Finish!")


evening = "/run/media/kirin/新加卷/images/evening.txt"
morning = "/run/media/kirin/新加卷/images/morning.txt"

if __name__ == '__main__':
    reflush_ori()
    reflush_pre()
    build_Tree(evening)
    build_Tree(morning)
    build_predata()
    pass
