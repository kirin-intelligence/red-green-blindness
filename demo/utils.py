import datetime
import json
import threading
import time

import gc
import xlwings as xw
from PyQt5.QtCore import QUrl, pyqtSlot, QThread, QDateTime, Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QSize
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
# from PyQtWebEngine
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QDesktopWidget, \
    QApplication, QMainWindow, QMessageBox, QVBoxLayout, QDialog, QLabel
from constant import *
from urllib.request import urlopen

from gen_data_util import background_worker, run_rgb, report, cal_length, np


class MapWindow(QDialog):
    rectSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MapWindow, self).__init__(parent)
        self.label = QLabel(self)
        self.setWindowTitle("交通拥堵分析系统")
        self.resize(QSize(1400, 900))
        layout = QVBoxLayout(self)
        self.webview = QWebEngineView(self)
        self.channel = QWebChannel(self)
        # 把自身对象传递进去
        self.channel.registerObject('Bridge', self)
        # 设置交互接口
        self.webview.page().setWebChannel(self.channel)
        layout.addWidget(self.webview)
        self.webview.load(
            QUrl.fromLocalFile(APP_HtmlPath + os.sep + "choose_rect.html"))
        self.show()

    @pyqtSlot(str)
    @pyqtSlot(QUrl)
    def getRect(self, rect):
        leftbottom = rect.split(' ')[0]
        righttop = rect.split(' ')[1]
        self.rectSignal.emit(rect)  # 发射信号
        self.close()


class CollectThread(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, parent=None):
        super(CollectThread, self).__init__(parent)
        # 设置工作状态与初始num数值
        self.working = True
        self.num = 0

    def __del__(self):
        # 线程状态改变与线程终止
        self.working = False
        self.wait()

    def run(self):
        try:
            GLOBAL_CONFIG[THREAD_FLAG] = True
            # TODO
            GLOBAL_CONFIG[DATA_DIR] = 'data/'
            # 左下角
            x1 = float(GLOBAL_CONFIG[LEFT_POINT][0])
            y1 = float(GLOBAL_CONFIG[LEFT_POINT][1])
            x2 = float(GLOBAL_CONFIG[RIGHT_POINT][0])
            y2 = float(GLOBAL_CONFIG[RIGHT_POINT][1])
            x_step = 0.0124
            y_step = 0.009
            x_count = -int(((x1 - x2) // x_step) - 1)
            y_count = int(((y1 - y2) // y_step) + 1)

            x_list = [x1 + i * x_step for i in range(x_count)]
            y_list = [y1 - i * y_step for i in range(y_count)]
            print(x_list, y_list)
            point_lst = [(x, y) for x in x_list for y in y_list]
            # for sp in config.special_point:
            #     point_lst.append(sp)
            t_lst = []
            for p in point_lst:
                t_lst.append(threading.Thread(target=background_worker, args=(p)))
            self.sinOut.emit(f"启动线程数目：{GLOBAL_CONFIG[SPACING_TIME] / len(t_lst)}")

            del x_list
            del y_list
            del point_lst
            gc.collect()
            for index, t in enumerate(t_lst):
                t.setDaemon(True)
                if index % 10 == 0:
                    self.sinOut.emit(f"线程id：{index} 启动")
                t.start()
                time.sleep(GLOBAL_CONFIG[SPACING_TIME] / len(t_lst))
            self.sinOut.emit(f"任务启动成功,运行中......")

            for t in t_lst:
                t.join()
        except Exception as e:
            self.sinOut.emit(f"生成错误，请检查：{e}")


class GenDataThread(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, parent=None):
        super(GenDataThread, self).__init__(parent)
        # 设置工作状态与初始num数值
        self.working = True
        self.num = 0
        self.Hotmap_DIR = {}
        self.total_ans = []
        self.count_DIR = {}
        self.datetime_list = []

    def __del__(self):
        # 线程状态改变与线程终止
        self.working = False
        self.wait()

    def gen_data(self):
        for root, dirs, files in os.walk(GLOBAL_CONFIG[DATA_DIR], topdown=False):
            # if (current_time >= date_begin_time) and (current_time <= date_end_time):
            try:
                if '_' in root:
                    date_time = root.split('\\')[-1]
                    current_time = datetime.datetime(int(date_time.split("_")[0]), int(date_time.split("_")[1]),
                                                     int(date_time.split("_")[2]),
                                                     int(date_time.split("_")[3]))
                    self.datetime_list.append(current_time)

                self.sinOut.emit(f"当前正在处理目录为：{root}的数据")

                for name in files:
                    if name.endswith("npz"):
                        if not GLOBAL_CONFIG[THREAD_FLAG]:
                            exit()
                        try:
                            # 添加时间
                            dir_string = name.split("_")[4] + "_" + name.split("_")[5]
                            dir_string = dir_string[:-4]
                            X = np.load(os.path.join(root, name))
                            if dir_string in self.Hotmap_DIR.keys():
                                self.Hotmap_DIR[dir_string] += X['arr_1']
                                self.count_DIR[dir_string] += X['arr_0']
                            else:
                                self.Hotmap_DIR[dir_string] = X['arr_1']
                                self.count_DIR[dir_string] = X['arr_0']
                        except:
                            pass
            except Exception as e:
                self.sinOut.emit(f"出现错误，请检查配置是否正确{str(e)}")

            # x[0]起始点,x[1]终点 ,x[2]时间,  ?x[3]路程 ,x[4]当前所在时间点，x[5]中点

    def analyse_map(self):
        for k in self.Hotmap_DIR:
            if not GLOBAL_CONFIG[THREAD_FLAG]:
                exit()
            GPS_float = (float(k.split('_')[0]), float(k.split('_')[1]))
            final, red, yellow, green = run_rgb(self.Hotmap_DIR[k], self.count_DIR[k])
            ans, point_map = report(final, GPS_float, self.Hotmap_DIR[k])
            new_ans = cal_length(ans)
            self.total_ans.extend(new_ans)
        self.total_ans.sort(key=lambda x: GLOBAL_CONFIG[TIME_WEIGHT] * x[2] + (1 - GLOBAL_CONFIG[TIME_WEIGHT]) * x[3],
                            reverse=True)
        print(self.total_ans)

        self.datetime_list = sorted(self.datetime_list, key=lambda x: x.timestamp())
        data_contant_day = self.datetime_list[-1] - self.datetime_list[0]
        self.sinOut.emit(f"数据生成完成，一共包含：{data_contant_day.days}天，每天时间点为： {GLOBAL_CONFIG[WORK_TIME]} ")

    def write_to_excel(self):
        json_data_arr = []
        # 开始生成json文件，并且写入excel
        now = QDateTime.currentDateTime().toString(Qt.ISODate)
        now = now.replace(':', '-')
        file_path = GLOBAL_CONFIG[EXCEL_DIR] + os.sep + now + '-data.xlsx'
        self.sinOut.emit(f"开始写入EXCEL文件:{file_path}...")
        rows_data = []
        for no, point in enumerate(self.total_ans):

            json_data = {}
            start_point = point[0][:-1]
            end_point = point[1][:-1]
            jam_type = point[0][-1]
            mid_point = point[4]
            # 乘以数据的天数，转换为小时。
            jam_time = round(float(point[2]) / 60.0, 1)
            start_place = get_place(start_point)
            end_place = get_place(end_point)
            if no % 100 == 0:
                self.sinOut.emit(f"当前写入：{start_place}...")
            distance, paths = get_right_steps(start_point, end_point, mid_point)
            json_data[JSON_NO] = no
            json_data[JSON_DISTANCE] = distance
            json_data[JSON_JAM_TIME] = jam_time
            json_data[JSON_START_POINT] = start_point
            json_data[JSON_START_PLACE] = start_place
            json_data[JSON_END_POINT] = end_point
            json_data[JSON_END_PLACE] = end_place
            json_data[JSON_PATHS] = paths
            # TODO
            json_data[JSON_DAY] = 'evening'
            json_data[JSON_TYPE] = jam_type
            # for template in JSON_TEMPLATE:
            #     assert (json_data[template])

            if jam_type == 'red':
                color = '红色'
            elif jam_type == 'yellow':
                color = '橙黄'
            else:
                color = '黄色'
            row_data = [no, start_place, str(start_point).replace('[', '').replace(']', ''), end_place,
                        str(end_point).replace('[', '').replace(']', ''), distance,
                        color, jam_time]

            rows_data.append(row_data)
            json_data_arr.append(json_data)
        with open(JSON_FILE_PATH, "w") as json_file:
            # ensure_ascii =
            json.dump(json_data_arr, json_file)
        workbook = xw.Book()
        worksheet = workbook.sheets[0]
        title_row = [['序号', '起点', '起点经纬度', '终点', '终点经纬度', '长度', '拥堵情况（颜色）', '拥堵时间（小时）']]
        worksheet.range('A1').value = title_row
        worksheet.range('A2').value = rows_data
        workbook.save(file_path)
        # workbook.close()
        # os.system(f'start {file_path}')
        # 保存
        self.sinOut.emit(f"EXCEL文件所在路径:{file_path}")
        self.sinOut.emit(SUCCESS)

    def run(self):
        GLOBAL_CONFIG[THREAD_FLAG] = True
        try:
            self.gen_data()
            self.analyse_map()
            self.write_to_excel()
        except Exception as e:
            self.sinOut.emit(f"生产错误，请查验：{e}")

        # except Exception as e:
        #     print(e)
        #     self.sinOut.emit(f"系统内存不足，请减少数据内容"
        #                      f"{str(e)}")
        #     self.sinOut.emit(ERROR)


def get_current_time():
    now = QDateTime.currentDateTime().toString(Qt.ISODate)
    return now


def add_tb_log(textBrowser, value):
    textBrowser.append(f"当前时间：{get_current_time()} ----- {str(value)}")


def get_place(point):
    url = 'https://restapi.amap.com/v3/geocode/regeo?key=2be4c36d53e74e0c585326d62d6fe6' \
          'e3&location=%s,%s&poitype=&radius=1000&extensions=base&batch=false&roadlevel=0' % (point[0], point[1])
    data = json.loads(urlopen(url).read())
    place = (data['regeocode']['formatted_address'])
    return place


def get_driving_data(start_point, end_point, mid_point):
    # TODO
    # waypoint

    url = f"https://restapi.amap.com/v3/direction/driving?origin={start_point[0]},{start_point[1]}" \
        f"&destination={end_point[0]},{end_point[1]}&strategy=2&waypoints={mid_point[0]},{mid_point[1]}" \
        f"&extension=all&key={GAODE_KEY}"
    data_first = json.loads(urlopen(url).read())['route']['paths'][0]
    return data_first


def get_line_road(start_p, end_p):
    line_url = f'https://restapi.amap.com/v3/distance?origins={start_p[0]},{start_p[1]}&' \
        f'type=0&destination={end_p[0]},{end_p[1]}&key={GAODE_KEY}'
    dis = json.loads(urlopen(line_url).read())['results'][0]['distance']
    polyline = [start_p, end_p]
    return dis, polyline


def get_right_steps(s_point, e_point, mid_point):
    data_first = get_driving_data(s_point, e_point, mid_point)
    data_second = get_driving_data(e_point, s_point, mid_point)
    dis_first = int(data_first['distance'])
    dis_second = int(data_second['distance'])
    if dis_first < dis_second:
        right_steps = data_first['steps']
        right_dis = dis_first
    else:
        # TODO
        # 判断去掉右转,
        # 途径点
        right_steps = data_second['steps']
        right_dis = dis_second

    new_polylines = []
    if right_dis > 700:
        return get_line_road(s_point, e_point)
    # elif "左转" in str(right_steps) or "右转" in str(right_steps):
    #     return get_line_road(s_point, e_point)
    for step in right_steps:
        polylines = step['polyline']
        polylines = polylines.split(';')
        for point in polylines:
            point = point.split(',')
            new_point = [float(p) for p in point]
            new_polylines.append(new_point)
    return right_dis, new_polylines


def is_weekendday():
    dayOfWeek = datetime.datetime.now().weekday()
    if dayOfWeek < 5:
        return False
    return True
