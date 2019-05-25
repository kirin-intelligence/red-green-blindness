#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-25 12:51:53
# @Author  : Lewis Tian (2471740600@qq.com | lewis.smith.tian@gmail.com)
# @Link    : https://lewistian.github.io/
# @Version : Python3.6
import shutil

from PyQt5.QtCore import QSize, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QListWidgetItem, QFileDialog, QDial, QDialog, QBoxLayout, QButtonGroup, QPushButton, \
    QInputDialog
from PyQt5.QtWidgets import QDesktopWidget
from qtpy.QtCore import QStandardPaths

from mainw import Ui_mainWindow, APP_HtmlPath
from utils import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QProgressBar
import re
import sys
import os

from res_rc import Svg_icon_loading


class MissevanKit(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MissevanKit, self).__init__(parent)
        self.setupUi(self)

        self.setTab1()
        self.setTab2()
        self.setTab3()

    def setTab3(self):
        self.setLoading()
        self.setBrower()

    def setTab1(self):
        self.pushButton_3.clicked.connect(self.set_choose_rect_brower)

    def setTab2(self):
        self.pushButton_13.clicked.connect(self.downloadExcel)
        self.pushButton_7.clicked.connect(self.choose_data_dir)

    def choose_data_dir(self):
        dir = QFileDialog.getExistingDirectory(self, "选择数据文件夹",
                                               APPlicationDirPath)
        if dir:
            self.textEdit_7.setText(dir)

    def set_choose_rect_brower(self):
        map_win = MapWindow(self)
        map_win.rectSignal.connect(self.getRect)
        map_win.exec_()

    def getRect(self, rect):
        print(rect)
        if rect:
            leftb = rect.split(' ')[0]
            rightt = rect.split(' ')[1]
            self.textEdit.setText(leftb)
            self.textEdit_13.setText(rightt)

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
        self.loadWidget.setVisible(False)
        self.webview.setVisible(True)
        print('ok')

    def setBrower(self):
        self.webview = QWebEngineView()
        html_path = APP_HtmlPath+os.sep+"index.html"
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
        box.show()

    def downloadExcel(self):
        dir = QFileDialog.getExistingDirectory(self, "EXCEL文件保存到",
                                               QStandardPaths.writableLocation(QStandardPaths.DesktopLocation))
        target_file = dir + os.sep + 'res_rc.py'
        if dir:
            try:
                if os.path.isfile(target_file):
                    os.remove(target_file)
                shutil.copy('res_rc.py', target_file)
                print(dir)
                self.echo("文件已保存。")
            except Exception as e:
                print(e)


import qtmodern.windows
if __name__ == "__main__":

    app = QApplication(sys.argv)
    APP_DirPath = app.applicationDirPath()
    # APP_ImagePath = APP_DirPath + os.sep + 'image'
    # APP_HtmlPath = APP_DirPath + os.sep + 'lib'
    win = MissevanKit()
    mw = qtmodern.windows.ModernWindow(win)
    mw.show()
    sys.exit(app.exec_())
