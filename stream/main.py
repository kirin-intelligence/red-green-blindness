from report import *
from RGB_color import *
from split_dir import *

if __name__ == '__main__':
    day = 'evening'
    gps_centor=[116.394362,39.93587599999999]
    input_dir = '/run/media/kirin/新加卷/server/'
    target_dir = '/run/media/kirin/新加卷1/images/'
    # spilt_file(input_dir,target_dir)
    print(day)
    rgb_img = run_rgb(target_dir, day,gps_centor)
    result = report(rgb_img,gps_centor)
    # cv2.imshow('a', rgb_img)
    # cv2.waitKey(0)
