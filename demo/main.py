import os
import sys
from PyQt5.QtWidgets import QTableWidgetItem
# os.system("pyuic5 -o  mainw.py  main.ui")
from PyQt5.QtSvg import QSvgWidget
from mainw import Ui_mainWindow
from utils import *
import qtmodern.windows


class MissevanKit(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MissevanKit, self).__init__(parent)
        self.setupUi(self)
        # self.set_style()
        self.center()
        self.setTab1()
        self.setTab2()
        self.setTab3()
        self.setTab4()
        self.gen_data_thread = None
        self.collect_thread = None
        self.tab_1_log = gen_date_filename(APP_LogPath, "数据采集日志.txt")
        self.tab_2_log = gen_date_filename(APP_LogPath, "数据处理日志.txt")

    # self.tabWidget.setCurrentIndex(0)

    def center(self):  # 实现窗体在屏幕中央
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()  # 同上
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 4)

    def setTab1(self):
        self.pushButton.clicked.connect(self.start_collect)
        self.pushButton_2.clicked.connect(lambda: self.collect_progress(STOP))
        self.pushButton_9.clicked.connect(self.set_choose_rect_brower)
        # self.pushButton_4.clicked.connect(lambda: self.set_browser_collapse(self.textBrowser_3))

    def gen_tab1_config(self):
        # worktime
        # 是否只是工作日抓取
        GLOBAL_CONFIG[ONLY_WORK_DAY] = False
        if self.checkBox.isChecked():
            GLOBAL_CONFIG[ONLY_WORK_DAY] = True
        if self.radioButton_5.isChecked():
            if self.textEdit.toPlainText():
                try:
                    GLOBAL_CONFIG[WORK_TIME] = [int(i) for i in self.textEdit.toPlainText().split()]
                except:
                    self.echo_error('抓取的时间点输入格式不对，24小时制，用空格分隔')
                    return False
            else:
                self.echo_error('抓取的时间点（小时）为空，请检查')
                return False
        elif self.radioButton_4.isChecked():
            GLOBAL_CONFIG[WORK_TIME] = [i for i in range(24)]
        elif self.radioButton_3.isChecked():
            GLOBAL_CONFIG[WORK_TIME] = [i for i in range(7, 9)] + [i for i in range(17, 19)]
        elif self.radioButton_2.isChecked():
            GLOBAL_CONFIG[WORK_TIME] = [i for i in range(17, 19)]
        elif self.radioButton.isChecked():
            GLOBAL_CONFIG[WORK_TIME] = [i for i in range(7, 9)]

        if self.textEdit_left.toPlainText():
            # 左下角换到左上角
            left_p = self.textEdit_left.toPlainText().split(',')
            right_p = self.textEdit_right.toPlainText().split(',')
            GLOBAL_CONFIG[LEFT_POINT] = [left_p[0], right_p[1]]
            GLOBAL_CONFIG[RIGHT_POINT] = [right_p[0], left_p[1]]
        else:
            self.echo_error('矩形区域为空，请检查')
            return False

        if self.textEdit_9.toPlainText():
            try:
                spacing_time = int(self.textEdit_9.toPlainText())
                if spacing_time < 0:
                    self.echo_error('间隔时间不能小于0，请重新输入')
                    return False
                GLOBAL_CONFIG[SPACING_TIME] = spacing_time
            except:
                self.echo_error('间隔时间输入错误，请检查')

        else:
            self.echo_error('间隔时间为空，请检查')
            return False
        return True

    def start_collect(self):
        if self.gen_tab1_config():
            write_to_log(self.tab_1_log, "程序开始运行...")
            write_to_log(self.tab_1_log, GLOBAL_CONFIG)
            # 初始化
            if self.collect_thread:
                self.collect_thread.terminate()
                self.collect_thread = None
            self.collect_thread = CollectThread()
            self.collect_thread.sinOut.connect(self.collect_progress)
            self.collect_thread.start()
            # 循环滚动
            self.progressBar.setMaximum(0)
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(True)

    def collect_progress(self, flag):
        # 向列表控件中添加条目
        if flag == STOP:
            write_to_log(self.tab_1_log, "用户终止程序")
            self.collect_thread.terminate()
            GLOBAL_CONFIG[THREAD_FLAG] = False
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)
            self.progressBar.setMaximum(100)
        elif flag == ERROR:
            write_to_log(self.tab_1_log, "系统发生错误，请检查")
            self.collect_thread.terminate()
            GLOBAL_CONFIG[THREAD_FLAG] = False
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)

            self.progressBar.setMaximum(100)
        else:
            write_to_log(self.tab_1_log, flag)

    def set_date_time(self):
        # datetime = Qcommon_roadDateTime.currentDateTime()
        pass

    def set_choose_rect_brower(self):
        map_win = MapWindow(self)
        map_win.rectSignal.connect(self.getRect)
        map_win.exec_()

    def set_browser_collapse(self, browser):
        if browser.isVisible():
            browser.setVisible(False)
            browser.clear()
        else:
            browser.setVisible(True)

    def getRect(self, rect):
        if rect:
            leftb = rect.split(' ')[0]
            right = rect.split(' ')[1]

            self.textEdit_left.setText(leftb)
            self.textEdit_right.setText(right)

    def setTab2(self):
        self.pushButton_14.clicked.connect(self.start_gen_data)
        self.pushButton_7.clicked.connect(self.choose_data_dir)
        # self.pushButton_choose_road.clicked.connect(self.choose_road_dialog)
        self.pushButton_13.clicked.connect(lambda: self.gen_data_progress(STOP))
        # self.textEdit_red.selectionChanged.connect(self.change_green_threshold)

    def change_green_threshold(self):
        try:
            red = float(self.textEdit_red.toPlainText())
            yellow = float(self.textEdit_yellow.toPlainText())
            green = float(self.textEdit_green.toPlainText())
            if is_float(red) and is_float(yellow) and is_float(green):
                if not red > yellow > green:
                    self.echo_error("输入错误，拥堵比例关系应该是红点大于橙黄点大于黄色")
                    return False
                GLOBAL_CONFIG[RED_THRESHOLD] = red
                GLOBAL_CONFIG[YELLOW_THRESHOLD] = yellow
                GLOBAL_CONFIG[GREEN_THRESHOLD] = green
                return True
            else:
                self.echo_error("输入错误 ，需要为(0-1)的小数")
                return False

        except:
            self.echo_error("输入错误，需要为(0-1)的小数")
            return False

    def gen_tab2_config(self):
        if not self.change_green_threshold():
            return False

        if self.radioButton_9.isChecked():
            GLOBAL_CONFIG[GEN_ROAD_TYPE] = ALL_ROAD
        elif self.radioButton_10.isChecked():
            GLOBAL_CONFIG[GEN_ROAD_TYPE] = FAST_ROAD
        elif self.radioButton_11.isChecked():
            GLOBAL_CONFIG[GEN_ROAD_TYPE] = COMMON_ROAD
        data_dir = self.textEdit_7.toPlainText()
        if data_dir:
            flag = False
            for roots, dirs, files in os.walk(data_dir):
                for f in files:
                    if f.endswith('npz'):
                        flag = True
            if not flag:
                self.echo_error('数据所在路径中没有所需要的数据文件，请检查')
                return False
            if data_dir.endswith(os.sep):
                GLOBAL_CONFIG[DATA_DIR] = data_dir
            else:
                GLOBAL_CONFIG[DATA_DIR] = data_dir + os.sep
        else:
            self.echo_error('数据所在路径不能为空，请检查')
            return False

        return True

    def choose_road_dialog(self):
        road, ok = QInputDialog.getItem(self, "选择指定道路", "'全部'代表所有道路\n\n请选择道路:", ROAD_DATAS, 1, True)
        if ok:
            if road:
                self.textEdit_11.setText(road)
                if road == ROAD_DATAS[0]:
                    pass

    def start_gen_data(self):
        if self.gen_tab2_config():
            print(GLOBAL_CONFIG)
            write_to_log(self.tab_2_log, "程序开始运行...")
            write_to_log(self.tab_2_log, GLOBAL_CONFIG)
            self.pushButton_14.setEnabled(False)
            self.pushButton_13.setEnabled(True)
            if self.gen_data_thread:
                self.gen_data_thread.terminate()
                self.gen_data_thread = None
            self.progressBar_3.setValue(0)
            self.gen_data_thread = GenDataThread()
            self.gen_data_thread.sinOut.connect(self.gen_data_progress)
            self.gen_data_thread.start()

    def gen_data_progress(self, flag):
        if flag == STOP:
            write_to_log(self.tab_2_log, "用户终止程序")
            self.gen_data_thread.terminate()
            GLOBAL_CONFIG[THREAD_FLAG] = False
            self.pushButton_14.setEnabled(True)
            self.pushButton_13.setEnabled(False)

            self.progressBar_3.setValue(0)

        elif flag == ERROR:
            write_to_log(self.tab_2_log, "系统崩溃，请查明原因")
            self.echo("系统崩溃，请查明原因")
            self.gen_data_thread.terminate()
            GLOBAL_CONFIG[THREAD_FLAG] = False
            self.pushButton_14.setEnabled(True)
            self.pushButton_13.setEnabled(False)
            self.progressBar_3.setValue(0)

        elif flag == SUCCESS:
            write_to_log(self.tab_2_log, "数据生成完成，可进入识别或评价标签进行处理")
            self.echo("数据生成完成，可进入识别或评价标签进行处理")
            self.webview.reload()
            GLOBAL_CONFIG[THREAD_FLAG] = False
            self.pushButton_14.setEnabled(True)
            self.pushButton_13.setEnabled(False)

            self.progressBar_3.setValue(100)

        else:
            try:
                flag = int(flag)
                self.progressBar_3.setValue(flag)
            except:
                write_to_log(self.tab_2_log, flag)

    def choose_data_dir(self):
        dir = QFileDialog.getExistingDirectory(self, "选择数据文件夹",
                                               APP_DirPath)
        if dir:
            self.textEdit_7.setText(dir)

    def setTab3(self):
        self.setLoading()
        self.setBrower()

    def setLoading(self):
        self.loadWidget = QSvgWidget()
        self.loadWidget.setMaximumSize(QSize(60, 60))
        self.loadWidget.load(Svg_icon_loading)
        self.gridLayout_2.addWidget(self.loadWidget)
        self.loadWidget.setVisible(False)

    def setLoadStarted(self):
        self.loadWidget.setVisible(True)
        print('开始')

    def setLoadFinished(self, ):
        self.webview.setVisible(True)
        self.loadWidget.setVisible(False)

    def setBrower(self):
        self.webview = QWebEngineView()
        html_path = APP_HtmlPath + os.sep + "index.html"
        self.webview.load(QUrl.fromLocalFile(html_path))
        self.gridLayout_2.addWidget(self.webview)
        self.webview.setVisible(False)
        self.webview.page().loadStarted.connect(self.setLoadStarted)
        self.webview.page().loadFinished.connect(self.setLoadFinished)

    def setTab4(self):
        self.pushButton_16.clicked.connect(self.export_excel)
        self.pushButton_15.clicked.connect(self.gen_table)

    def gen_table(self):

        time_weight = self.textEdit_timeweight.toPlainText()
        if time_weight:
            time_weight = float(time_weight)
        else:
            self.echo_error('拥堵时长权重不能为空，请检查')
            return False
        length_weight = self.textEdit_lengthweight.toPlainText()
        if length_weight:
            length_weight = float(length_weight)
        else:
            self.echo_error('拥堵距离权重不能为空，请检查')
            return False
        # 表格处理要完全清除
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setStyleSheet("background-color: gray")
        self.tableWidget.setSelectionBehavior(1)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1)
        self.tableWidget.setShowGrid(True)

        file = open(JSON_FILE_PATH, 'r', encoding='utf-8')
        json_datas = json.load(file)
        time_max = max([float(x['jam_time']) for x in json_datas])
        length_max = max([float(x['distance']) for x in json_datas])
        json_datas.sort(
            key=lambda x: time_weight * float(x['jam_time']) / time_max + length_weight
                          * float(x['distance']) / length_max, reverse=True)
        self.tableWidget.setColumnCount(len(TITLE_ROW))
        self.tableWidget.setRowCount(len(json_datas))
        self.tableWidget.setHorizontalHeaderLabels(TITLE_ROW)
        for row_index, json_data in enumerate(json_datas):
            no = json_data[JSON_NO]
            distance = json_data[JSON_DISTANCE]
            jam_time = json_data[JSON_JAM_TIME]
            start_point = json_data[JSON_START_POINT]
            start_place = json_data[JSON_START_PLACE]
            end_point = json_data[JSON_END_POINT]
            end_place = json_data[JSON_END_PLACE]
            # TODO
            date_type = json_data[JSON_DAY]
            jam_type = json_data[JSON_TYPE]
            if jam_type == 'red':
                color = '红色'
            elif jam_type == 'yellow':
                color = '橙黄'
            else:
                color = '黄色'
            if date_type == 'morning':
                day = '早高峰'
            else:
                day = '晚高峰'
            row_data = [no, day, start_place, str(start_point).replace('[', '').replace(']', ''),
                        end_place, str(end_point).replace('[', '').replace(']', ''), float(distance), color, jam_time]
            for col_index, item in enumerate(row_data):
                qitem = QTableWidgetItem()
                qitem.setTextAlignment(Qt.AlignCenter)
                # set data好，不然text排序只按字符串排
                qitem.setData(0, item)
                self.tableWidget.setItem(row_index, col_index, qitem)

    def export_excel(self):

        dir = QFileDialog.getExistingDirectory(self, "EXCEL文件保存到")
        if dir:
            file_path = gen_date_filename(dir, '-拥堵分析.xlsx')
            workbook = xw.Book()
            worksheet = workbook.sheets[0]
            rows = self.tableWidget.rowCount()
            cols = self.tableWidget.columnCount()
            rows_data = []
            for row in range(rows):
                row_data = []
                for col in range(cols):
                    data = self.tableWidget.item(row, col).text()
                    row_data.append(data)
                rows_data.append(row_data)
            worksheet.range('A1').value = EXCEL_TITLE_ROW
            worksheet.range('A2').value = rows_data
            workbook.save(file_path)
            workbook.close()
            self.echo(f"导出完成，EXCEL文件所在路径:\n{file_path}")
        else:
            self.echo_error("EXCEL文件存储路径不能为空")
            return False

    def echo(self, value):
        '''显示对话框返回值'''
        box = QMessageBox(self)
        box.information(self, "操作成功", "{}\n".format(value),
                        QMessageBox.Ok)

    def echo_error(self, value):
        box = QMessageBox(self)
        box.warning(self, "错误", "{}\n".format(value),
                    QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    APP_DirPath = app.applicationDirPath()
    # APP_ImagePath = APP_DirPath + os.sep + 'image'
    # APP_HtmlPath = APP_DirPath + os.sep + 'lib'
    win = MissevanKit()
    mw = qtmodern.windows.ModernWindow(win)
    mw.show()
    sys.exit(app.exec_())
