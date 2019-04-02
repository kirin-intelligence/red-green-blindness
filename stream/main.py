from report import *
from RGB_color import *
from web.backup.config import *
from redis import StrictRedis, ConnectionPool


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


pool = ConnectionPool(host='123.56.19.49', password='wscjxky123', port=6379, db=5)
redis = StrictRedis(connection_pool=pool)
if __name__ == '__main__':
    day = 'evening'
    x_list = [x1 + i * x_step for i in range(x_count)]
    y_list = [y1 - i * y_step for i in range(y_count)]
    print(len(x_list))
    print(len(y_list))
    #  西二环
    # gps = [116.35716199999999,39.917876]
    # input_dir = '/run/media/kirin/新加卷1/server/'
    # target_dir = '/run/media/kirin/新加卷/images/'
    # rgb_img = run_rgb(target_dir, day, gps)
    # # result = report(rgb_img, gps)
    # img = cv2.imread("out_put.png")
    # # start += write_excel(result, day, start)
    # # write_html(gps_center, result)
    # cv2.imshow('a', img)
    # cv2.waitKey(0)
