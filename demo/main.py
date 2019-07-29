import os
import sys

os.system("pyuic5 -o  mainw.py  main.ui")
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
        self.gen_data_thread = None
        self.collect_thread = None
        # self.tabWidget.setCurrentIndex(0)

    def center(self):  # 实现窗体在屏幕中央
        screen = QDesktopWidget().screenGeometry()  # QDesktopWidget为一个类，调用screenGeometry函数获得屏幕的尺寸
        size = self.geometry()  # 同上
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def setTab1(self):
        self.pushButton.clicked.connect(self.start_collect)
        self.pushButton_2.clicked.connect(lambda: self.collect_progress(STOP))
        self.pushButton_9.clicked.connect(self.set_choose_rect_brower)
        self.pushButton_4.clicked.connect(lambda: self.set_browser_collapse(self.textBrowser_3))

    def gen_tab1_config(self):
        # worktime
        # 是否只是工作日抓取
        GLOBAL_CONFIG[ONLY_WORK_DAY] = False
        if self.checkBox.isChecked():
            GLOBAL_CONFIG[ONLY_WORK_DAY] = True
        if self.radioButton_5.isChecked():
            if self.textEdit_right_2.toPlainText():
                GLOBAL_CONFIG[WORK_TIME] = [int(i) for i in self.textEdit_right_2.toPlainText().split()]
            else:
                self.echo_error('抓取的时间点（小时）为空，请检查')
                return False
        elif self.radioButton_4.isChecked():
            GLOBAL_CONFIG[WORK_TIME] = [i for i in range(24)]
        elif self.radioButton_3.isChecked():
            GLOBAL_CONFIG[WORK_TIME] = [i for i in range(7, 10)] + [i for i in range(17, 20)]
        elif self.radioButton_2.isChecked():
            GLOBAL_CONFIG[WORK_TIME] = [i for i in range(17, 20)]
        elif self.radioButton.isChecked():
            GLOBAL_CONFIG[WORK_TIME] = [i for i in range(7, 10)]
        else:
            self.echo_error('抓取的时间点（小时）为空，请检查')
            return False

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
            GLOBAL_CONFIG[SPACING_TIME] = int(self.textEdit_9.toPlainText())
        else:
            self.echo_error('间隔时间为空，请检查')
            return False
        return True

    def start_collect(self):
        if self.gen_tab1_config():
            print(GLOBAL_CONFIG)

            add_tb_log(self.textBrowser_3, "程序开始运行...")
            add_tb_log(self.textBrowser_3, GLOBAL_CONFIG)
            # 初始化
            if self.collect_thread:
                self.collect_thread.terminate()
                self.collect_thread=None
            self.collect_thread = CollectThread()
            self.collect_thread.sinOut.connect(self.collect_progress)
            self.collect_thread.start()
            # 循环滚动
            self.progressBar.setMaximum(0)
            self.pushButton.setEnabled(False)

    def collect_progress(self, flag):
        # 向列表控件中添加条目
        if flag == STOP:
            add_tb_log(self.textBrowser_3, "用户终止程序")
            self.collect_thread.terminate()
            GLOBAL_CONFIG[THREAD_FLAG] = False
            self.pushButton.setEnabled(True)
            self.progressBar.setMaximum(100)
        elif flag == ERROR:
            add_tb_log(self.textBrowser_3, "系统发生错误，请检查")
            self.collect_thread.terminate()
            GLOBAL_CONFIG[THREAD_FLAG] = False
            self.pushButton.setEnabled(True)
            self.progressBar.setMaximum(100)
        else:
            add_tb_log(self.textBrowser_3, flag)

    def set_date_time(self):
        # datetime = QDateTime.currentDateTime()
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
        print(rect)
        if rect:
            leftb = rect.split(' ')[0]
            right = rect.split(' ')[1]

            self.textEdit_left.setText(leftb)
            self.textEdit_right.setText(right)

    def setTab2(self):
        self.pushButton_14.clicked.connect(self.start_gen_data)
        self.pushButton_7.clicked.connect(self.choose_data_dir)
        self.pushButton_8.clicked.connect(lambda: self.set_browser_collapse(self.textBrowser_6))
        self.pushButton_choose_road.clicked.connect(self.choose_road_dialog)
        self.pushButton_13.clicked.connect(lambda: self.gen_data_progress(STOP))

    def gen_tab2_config(self):
        choose_road = self.textEdit_11.toPlainText()
        if choose_road:
            GLOBAL_CONFIG[CHOOSE_ROAD] = choose_road
            # else:
            #     self.echo_error('输入的道路不存在，请检查')
            #     return False
        else:
            self.echo_error('道路选择不能为空，请检查')
            return False
        time_weight = self.textEdit_timeweight.toPlainText()
        if time_weight:
            time_weight = float(time_weight)
            if 0 < time_weight < 1:
                GLOBAL_CONFIG[TIME_WEIGHT] = float(time_weight)
            else:
                self.echo_error('拥堵时长权重值为大于0且小于1的小数，请检查')
                return False
        else:
            self.echo_error('拥堵时长权重不能为空，请检查')
            return False
        data_dir = self.textEdit_7.toPlainText()
        if data_dir:
            GLOBAL_CONFIG[DATA_DIR] = data_dir
        else:
            self.echo_error('数据所在路径不能为空，请检查')
            return False
        dir = QFileDialog.getExistingDirectory(self, "EXCEL文件保存到",
                                               )
        if dir:
            GLOBAL_CONFIG[EXCEL_DIR] = dir
        else:
            self.echo_error("excel存储路径不能为空")
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
            add_tb_log(self.textBrowser_6, "程序开始运行...")
            add_tb_log(self.textBrowser_6, GLOBAL_CONFIG)

            # else:

            self.progressBar_3.setMaximum(0)
            self.pushButton_14.setEnabled(False)
            if self.gen_data_thread:
                self.gen_data_thread.terminate()
                self.gen_data_thread=None

            self.gen_data_thread = GenDataThread()
            self.gen_data_thread.sinOut.connect(self.gen_data_progress)
            self.gen_data_thread.start()

    def gen_data_progress(self, flag):
        if flag == STOP:
            add_tb_log(self.textBrowser_6, "用户终止程序")
            self.gen_data_thread.terminate()
            GLOBAL_CONFIG[THREAD_FLAG] = False
            self.pushButton_14.setEnabled(True)
            self.progressBar_3.setMaximum(100)
        if flag == ERROR:
            add_tb_log(self.textBrowser_6, "系统崩溃，请查明原因")
            self.echo("系统崩溃，请查明原因")
            self.gen_data_thread.terminate()
            GLOBAL_CONFIG[THREAD_FLAG] = False
            self.pushButton_14.setEnabled(True)
            self.progressBar_3.setMaximum(100)
        elif flag == SUCCESS:
            add_tb_log(self.textBrowser_6, "excel数据文件生成完成,可进入地图展示模块查看")
            self.echo("excel数据文件生成完成,可进入地图展示模块查看")
            self.webview.reload()
            GLOBAL_CONFIG[THREAD_FLAG] = False
            self.pushButton_14.setEnabled(True)
            self.progressBar_3.setMaximum(100)
        else:
            add_tb_log(self.textBrowser_6, flag)
            # self.echo("excel数据文件生成成功")

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
        print(html_path)
        self.webview.load(QUrl.fromLocalFile(html_path))
        self.gridLayout_2.addWidget(self.webview)
        self.webview.setVisible(False)
        self.webview.page().loadStarted.connect(self.setLoadStarted)
        self.webview.page().loadFinished.connect(self.setLoadFinished)

    def echo(self, value):
        '''显示对话框返回值'''
        box = QMessageBox(self)
        box.information(self, "操作成功", "{}\n".format(value),
                        QMessageBox.Ok)
        # box.setIcon(("D:/pycharmproject/red-green-blindness/demo/image/success_48px_1129030_easyicon.net.png"))

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
