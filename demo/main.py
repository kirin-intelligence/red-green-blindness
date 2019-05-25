#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-25 12:51:53
# @Author  : Lewis Tian (2471740600@qq.com | lewis.smith.tian@gmail.com)
# @Link    : https://lewistian.github.io/
# @Version : Python3.6
import shutil

from PyQt5.QtCore import QSize, pyqtSlot
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QListWidgetItem,QFileDialog,QDial,QDialog,QBoxLayout,QButtonGroup,QPushButton,QInputDialog
from PyQt5.QtWidgets import QDesktopWidget
from mainw import Ui_mainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QProgressBar
import re
import sys
import os

from res_rc import Svg_icon_loading

listInfo = []
cwd = os.getcwd()



class MissevanKit(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MissevanKit, self).__init__(parent)
        self.setupUi(self)
        self.setTab1()
        self.setLoading()
        self.setBrower()
        self.connectSlots()
        # self.loadWidget.load(Svg_icon_loading)

    def echo(self, value):
        '''显示对话框返回值'''
        QMessageBox.information(self, "操作成功", "{}\n".format(value),
                                QMessageBox.Yes)
        # pass

    def downloadExcel(self):
        dir= QFileDialog.getExistingDirectory(self,"EXCEL文件保存到","C:/",)
        shutil.copy('res_rc.py',dir)
        print(dir)
        self.echo("文件已保存。")


    def setTab1(self):
        self.pushButton_13.clicked.connect(self.downloadExcel)

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
        html_path = "D:/pycharmproject/red-green-blindness/stream/index.html"
        print(html_path)
        self.webview.load(QUrl.fromLocalFile(html_path))
        # self.webview.load(QUrl("http://123.56.19.49/stream/"))
        # self.textBrowser=self.webview
        self.gridLayout_2.addWidget(self.webview)
        self.webview.setVisible(False)
        self.webview.page().loadStarted.connect(self.setLoadStarted)
        self.webview.page().loadFinished.connect(self.setLoadFinished)

    def connectSlots(self):
        pass
        # home tab
        # self.download.clicked.connect(self.downloadSound)
        # self.download.setShortcut("CTRL+L")

        # self.search.clicked.connect(self.searchInfo)
        # self.search.setShortcut("CTRL+Return")

        # self.toolButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl.fromLocalFile("./sound")))

        # self.clearAll.clicked.connect(self.clearAllDownloaded)


import qtmodern.windows

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MissevanKit()
    mw = qtmodern.windows.ModernWindow(win)
    mw.show()
    sys.exit(app.exec_())
