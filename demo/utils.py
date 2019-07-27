import json
import xlwt
from PyQt5.QtCore import QUrl, pyqtSlot, QThread, QDateTime, Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QSize
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QDesktopWidget, \
    QApplication, QMainWindow, QMessageBox, QVBoxLayout, QDialog, QLabel
from constant import *
from get_data import *


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
        GLOBAL_CONFIG[THREAD_FLAG] = True
        if not os.path.exists(base_path):
            os.mkdir(base_path)
        x_list = [config.x1 + i * config.x_step for i in range(config.x_count)]
        y_list = [config.y1 - i * config.y_step for i in range(config.y_count)]
        point_lst = [(x, y) for x in x_list for y in y_list]
        for sp in config.special_point:
            point_lst.append(sp)
        t_lst = []
        for p in point_lst:
            t_lst.append(threading.Thread(target=background_worker, args=(p)))
        del x_list
        del y_list
        del point_lst
        gc.collect()
        for index, t in enumerate(t_lst):
            t.setDaemon(True)
            if index % 10 == 0:
                self.sinOut.emit(f"线程id：{index} 启动")
            t.start()
            time.sleep(120 / len(t_lst))
        self.sinOut.emit(f"任务启动成功,运行中......")

        for t in t_lst:
            print(t)
            t.join()


class GenDataThread(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, parent=None):
        super(GenDataThread, self).__init__(parent)
        # 设置工作状态与初始num数值
        self.working = True
        self.num = 0

    def __del__(self):
        # 线程状态改变与线程终止
        self.working = False
        self.wait()

    def run(self):
        GLOBAL_CONFIG[THREAD_FLAG] = True
        GLOBAL_CONFIG[DATA_DIR] = 'data'
        Hotmap_DIR = {}
        total_ans = []
        count_DIR = {}
        for root, dirs, files in os.walk(GLOBAL_CONFIG[DATA_DIR], topdown=False):
            for name in files:
                if not GLOBAL_CONFIG[THREAD_FLAG]:
                    exit()
                try:
                    dir_string = name.split("_")[4] + "_" + name.split("_")[5]
                    dir_string = dir_string[:-4]
                    X = np.load(os.path.join(root, name))
                    if dir_string in Hotmap_DIR.keys():
                        Hotmap_DIR[dir_string] += X['arr_1']
                        count_DIR[dir_string] += X['arr_0']
                    else:
                        Hotmap_DIR[dir_string] = X['arr_1']
                        count_DIR[dir_string] = X['arr_0']
                except:
                    pass
        for k in Hotmap_DIR:
            if not GLOBAL_CONFIG[THREAD_FLAG]:
                exit()
            GPS_float = (float(k.split('_')[0]), float(k.split('_')[1]))
            final, red, yellow, green = util.run_rgb(Hotmap_DIR[k], count_DIR[k])
            ans, point_map = util.report(final, GPS_float, Hotmap_DIR[k])
            new_ans = util.cal_length(ans)
            total_ans.extend(ans)

        # 比例调节！！！！！！！！
        # K是调节参数，k=10大约是一比一，路程为km，时间为小时
        # x[0]起始点,x[1]终点 ,x[2]时间,  ?x[3]路程 ,x[4]当前所在时间点

        # TODO
        # GLOBAL_CONFIG[DATA_CONTAIN_DAYS]
        total_ans.sort(key=lambda x: GLOBAL_CONFIG[TIME_WEIGHT] * x[2] + (1 - GLOBAL_CONFIG[TIME_WEIGHT]) * x[3],
                       reverse=True)
        print(total_ans)
        json_data_arr = []
        GLOBAL_CONFIG[DATA_CONTAIN_DAYS] = 1
        # 开始生成json文件，并且写入excel
        now = QDateTime.currentDateTime().toString(Qt.ISODate)
        now = now.replace(':', '-')
        file_path = GLOBAL_CONFIG[EXCEL_DIR] + os.sep + now + '-data.xls'
        if os.path.isfile(file_path):
            os.remove(file_path)
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('Worksheet')
        worksheet.write(0, 0, label='序号')
        worksheet.write(0, 1, label='起点')
        worksheet.write(0, 2, label='起点经纬度')
        worksheet.write(0, 3, label='终点')
        worksheet.write(0, 4, label='终点经纬度')
        worksheet.write(0, 5, label='长度')
        worksheet.write(0, 6, label='拥堵情况（颜色）')
        worksheet.write(0, 7, label='拥堵时间（小时）')
        for no, point in enumerate(total_ans):
            json_data = {}
            start_point = point[0][:-1]
            end_point = point[1][:-1]
            jam_type = point[0][-1]
            # 乘以数据的天数，转换为小时。
            jam_time = round(float(point[2]) * GLOBAL_CONFIG[DATA_CONTAIN_DAYS] / 60, 1)

            start_place = get_place(start_point)
            end_place = get_place(end_point)

            distance, paths = get_right_steps(start_point, end_point)

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
            json_data_arr.append(json_data)
            worksheet.write(no + 1, 0, label="%s" % no)
            worksheet.write(no + 1, 1, label="%s" % start_place)
            worksheet.write(no + 1, 2, label="%s,%s" % (start_point[0], start_point[1]))
            worksheet.write(no + 1, 3, label="%s" % end_place)
            worksheet.write(no + 1, 4, label="%s,%s" % (end_point[0], end_point[1]))
            worksheet.write(no + 1, 5, label="%s" % distance)
            if type == 'red':
                color = '红色'
            elif type == 'yellow':
                color = '橙黄'
            else:
                color = '黄色'
            worksheet.write(no + 1, 6, label="%s" % color)
            worksheet.write(no + 1, 7, label="%s" % jam_time)
        with open(JSON_FILE_PATH, "w") as json_file:
            # ensure_ascii =
            json.dump(json_data_arr, json_file, )
        workbook.save(file_path)
        os.system(f'start {file_path}')
        # 保存
        self.sinOut.emit(f"EXCEL文件所在路径:{file_path}")
        self.sinOut.emit(SUCCESS)


def get_current_time():
    now = QDateTime.currentDateTime().toString(Qt.ISODate)
    return now


def add_tb_log(textBrowser, value):
    textBrowser.append(f"当前时间：{get_current_time()} ----- {str(value)}")


def get_place(point):
    url = 'https://restapi.amap.com/v3/geocode/regeo?key=2be4c36d53e74e0c585326d62d6fe6' \
          'e3&location=%s,%s&poitype=&radius=1000&extensions=base&batch=false&roadlevel=0' % (point[0], point[1])
    data = json.loads(requests.get(url).text)
    place = (data['regeocode']['formatted_address'])
    return place


def get_driving_data(start_point, end_point):
    # TODO
    # waypoint
    waypoint = ['', '']
    url = f"https://restapi.amap.com/v3/direction/driving?origin={start_point[0]},{start_point[1]}" \
        f"&destination={end_point[0]},{end_point[1]}&strategy=2&waypoints={waypoint[0]},{waypoint[1]}" \
        f"&extension=all&key={GAODE_KEY}"
    data_first = json.loads(requests.get(url).text)['route']['paths'][0]
    return data_first


def get_line_road(start_p, end_p):
    line_url = f'https://restapi.amap.com/v3/distance?origins={start_p[0]},{start_p[1]}&' \
        f'type=0&destination={end_p[0]},{end_p[1]}&key={GAODE_KEY}'
    dis = json.loads(requests.get(line_url).text)['results'][0]['distance']
    polyline = [start_p, end_p]
    return dis, polyline


def get_right_steps(s_point, e_point):
    data_first = get_driving_data(s_point, e_point)
    data_second = get_driving_data(e_point, s_point)
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
