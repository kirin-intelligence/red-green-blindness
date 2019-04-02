from report import *
from RGB_color import *
from web.backup.config import *
from redis import StrictRedis, ConnectionPool
from xlr import *

def refresh():
    day = 'morning'
    x_list = [x1 + i * x_step for i in range(x_count)]
    y_list = [y1 - i * y_step for i in range(y_count)]
    for x in x_list:
        for y in y_list[9:]:
            input_dir = '/run/media/kirin/新加卷1/server/'
            target_dir = '/run/media/kirin/新加卷/images/'
            # spilt_file(input_dir, target_dir)
            rgb_img = run_rgb(target_dir, day, [x, y])
            result = report(rgb_img, [x, y])
            img = cv2.imread("out_put.png")
if __name__ == '__main__':
    day = 'evening'
    x_list = [x1 + i * x_step for i in range(x_count)]
    y_list = [y1 - i * y_step for i in range(y_count)]
    print(len(x_list))
    print(len(y_list))
    #  西二环
    # gps = [116.35716199999999,39.917876]
    gps = [[[116.355896, 39.929737, 'red'],[116.356218, 39.922332, 'red']],
            [[116.356229, 39.922184, 'red'],
           [116.356593, 39.91407, 'red']],
            [[116.356593, 39.913976, 'red'],
           [116.356406, 39.909688, 'red']],
            [[116.356395, 39.908544, 'red'],
           [116.356443, 39.9074, 'red']],
            [[116.356481, 39.910577, 'red'],
           [116.355789, 39.907972, 'red']],
            [[116.355692, 39.931699, 'red'],
           [116.355762, 39.929737, 'red']],
            [[116.355767, 39.929338, 'red'],
           [116.355832, 39.927536, 'red']],
            [[116.355842, 39.92738, 'red'],
           [116.355955, 39.92464, 'red']],
            [[116.356046, 39.922727, 'red'],
           [116.356234, 39.918703, 'red']],
            [[116.35654, 39.911869, 'red'],
           [116.356288, 39.910256, 'red']],
            [[116.356497, 39.908754, 'red'],
          [116.35676, 39.913223, 'red']]]
    start=534
    # input_dir = '/run/media/kirin/新加卷1/server/'
    # target_dir = '/run/media/kirin/新加卷/images/'
    # rgb_img = run_rgb(target_dir, day, gps)
    # # result = report(rgb_img, gps)
    # img = cv2.imread("out_put.png")
    start += write_excel(gps, day, start)
    # # write_html(gps_center, result)
    # cv2.imshow('a', img)
    # cv2.waitKey(0)
