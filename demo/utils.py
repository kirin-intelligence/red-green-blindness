import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl, pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QSize
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QVBoxLayout

from main import APP_HtmlPath

listInfo = []
DATA_XLS='data.xls'
EXCEL_FILE=APP_HtmlPath+os.sep+DATA_XLS

class MapWindow(QDialog):
    rectSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MapWindow, self).__init__(parent)
        self.label = QtWidgets.QLabel(self)
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
