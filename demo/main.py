#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-25 12:51:53
# @Author  : Lewis Tian (2471740600@qq.com | lewis.smith.tian@gmail.com)
# @Link    : https://lewistian.github.io/
# @Version : Python3.6
from PyQt5.QtWebEngineWidgets import QWebEngineView
from mainw import Ui_mainWindow
from PyQt5 import QtCore
from  PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QProgressBar
import re
import sys
import os

listInfo = []
cwd = os.getcwd()

class MissevanKit(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MissevanKit, self).__init__(parent)
        self.setupUi(self)
        self.setBrower()
        self.connectSlots()
        if not os.path.exists('sound'):
            os.mkdir('sound')
    def setBrower(self):
        self.webview = QWebEngineView()
        print(cwd + os.sep + "index.html")
        # self.webview.load(QUrl.fromLocalFile())
        self.webview.load(QUrl("http://123.56.19.49/stream/"))
        # self.textBrowser=self.webview
        self.gridLayout_2.addWidget(self.webview)

    def connectSlots(self):

        """connect slots with buttons/
        short cuts/signals
        """
        # home tab
        # self.download.clicked.connect(self.downloadSound)
        # self.download.setShortcut("CTRL+L")

        # self.search.clicked.connect(self.searchInfo)
        # self.search.setShortcut("CTRL+Return")

        # self.toolButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl.fromLocalFile("./sound")))

        # self.clearAll.clicked.connect(self.clearAllDownloaded)

    def searchInfo(self):
        text = self.lineEdit.text()
        if not text:
            return
        try:
            mid = re.findall(r'\d+', text)[-1]
            index = self.comboBox.currentIndex()
            if index == 0:
                pass
            elif index == 1:
                pass
            elif index == 2:
                pass
        except:
            return


import qtmodern.windows
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MissevanKit()
    mw = qtmodern.windows.ModernWindow(win)
    mw.show()
    sys.exit(app.exec_())