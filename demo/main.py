import os

# os.system("pyuic5 -o  mainw.py  main.ui")

import shutil
from PyQt5.QtWidgets import QFileDialog, QInputDialog
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtSvg import QSvgWidget
from qtpy.QtCore import QStandardPaths
from PyQt5.QtCore import  QDateTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
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
        self.tabWidget.setCurrentIndex(0)

    def center(self):  # 实现窗体在屏幕中央
        screen = QDesktopWidget().screenGeometry()  # QDesktopWidget为一个类，调用screenGeometry函数获得屏幕的尺寸
        size = self.geometry()  # 同上
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def setTab1(self):
        self.pushButton.clicked.connect(self.start_collect)
        self.pushButton_2.clicked.connect(lambda: self.slotAdd(-1))

        self.pushButton_9.clicked.connect(self.set_choose_rect_brower)
        self.pushButton_4.clicked.connect(lambda: self.set_browser_collapse(self.textBrowser_3))
        self.set_date_time()

    def start_collect(self):
        self.collect_thread = MyThread()
        self.collect_thread.sinOut.connect(self.slotAdd)
        self.collect_thread.start()
        self.pushButton.setEnabled(False)

    def slotAdd(self, progress):
        # 向列表控件中添加条目
        progress = int(progress)
        print(progress)
        if progress == 5:
            print("finish")
            self.pushButton.setEnabled(True)
            self.textBrowser_3.clear()

        elif progress == -1:
            self.collect_thread.terminate()
            self.pushButton.setEnabled(True)
            self.progressBar.setValue(0)
            self.textBrowser_3.clear()
        else:
            self.textBrowser_3.append(str(progress))
            self.progressBar.setValue(progress)

    def set_date_time(self):
        datetime = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(datetime)
        self.dateTimeEdit_9.setDateTime(datetime.addDays(7))

        print(datetime.toString())

    def set_choose_rect_brower(self):
        map_win = MapWindow(self)
        map_win.rectSignal.connect(self.getRect)
        map_win.exec_()

    def set_browser_collapse(self, browser):
        if browser.isVisible():
            browser.setVisible(False)
        else:
            browser.setVisible(True)

    def getRect(self, rect):
        print(rect)
        if rect:
            leftb = rect.split(' ')[0]
            rightt = rect.split(' ')[1]
            self.textEdit_left.setText(leftb)
            self.textEdit_right.setText(rightt)

    def setTab2(self):
        self.pushButton_14.clicked.connect(self.downloadExcel)
        self.pushButton_7.clicked.connect(self.choose_data_dir)
        self.pushButton_8.clicked.connect(lambda: self.set_browser_collapse(self.textBrowser_6))
        self.pushButton_choose_road.clicked.connect(self.choose_road_dialog)

    def choose_road_dialog(self):
        road_datas = ["全部", "道路"]
        # 1为默认选中选项目，True/False  列表框是否可编辑。
        road, ok = QInputDialog.getItem(self, "选择指定道路", "'全部'代表所有道路\n\n请选择道路:", road_datas, 1, True)
        print(road)
        if road:
            if road == road_datas[0]:
                pass

    def downloadExcel(self):
        dir = QFileDialog.getExistingDirectory(self, "EXCEL文件保存到",
                                               QStandardPaths.writableLocation(QStandardPaths.DesktopLocation))
        target_file = dir + os.sep + DATA_XLS
        if dir:
            try:
                if os.path.isfile(target_file):
                    os.remove(target_file)
                shutil.copy(EXCEL_FILE, target_file)
                print(dir)
                self.echo("文件已保存。")
            except Exception as e:
                print(e)

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
        print('ok')

    def setBrower(self):
        self.webview = QWebEngineView()
        html_path = APP_HtmlPath + os.sep + "index.html"
        print(html_path)
        self.webview.load(QUrl.fromLocalFile(html_path))
        # self.webview.load(QUrl("http://123.56.19.49/stream/"))
        # self.textBrowser=self.webview
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    APP_DirPath = app.applicationDirPath()
    # APP_ImagePath = APP_DirPath + os.sep + 'image'
    # APP_HtmlPath = APP_DirPath + os.sep + 'lib'
    win = MissevanKit()
    mw = qtmodern.windows.ModernWindow(win)
    mw.show()
    sys.exit(app.exec_())
