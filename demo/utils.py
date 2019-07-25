import os
import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl, pyqtSlot, QThread
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QSize
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QVBoxLayout

CWD = os.getcwd()
APP_ImagePath = CWD + os.sep + 'image'
APP_HtmlPath = CWD + os.sep + 'lib'

Svg_icon_loading = '''<svg width="100%" height="100%" viewBox="0 0 38 38" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient x1="8.042%" y1="0%" x2="65.682%" y2="23.865%" id="a">
            <stop stop-color="#03a9f4" stop-opacity="0" offset="0%"/>
            <stop stop-color="#03a9f4" stop-opacity=".631" offset="63.146%"/>
            <stop stop-color="#03a9f4" offset="100%"/>
        </linearGradient>
    </defs>
    <g fill="none" fill-rule="evenodd">
        <g transform="translate(1 1)">
            <path d="M36 18c0-9.94-8.06-18-18-18" id="Oval-2" stroke="url(#a)" stroke-width="2">
                <animateTransform
                    attributeName="transform"
                    type="rotate"
                    from="0 18 18"
                    to="360 18 18"
                    dur="0.5s"
                    repeatCount="indefinite" />
            </path>
            <circle fill="#03a9f4" cx="36" cy="18" r="4">
                <animateTransform
                    attributeName="transform"
                    type="rotate"
                    from="0 18 18"
                    to="360 18 18"
                    dur="0.5s"
                    repeatCount="indefinite" />
            </circle>
        </g>
    </g>
</svg>'''.encode()

listInfo = []
DATA_XLS = 'data.xls'
EXCEL_FILE = APP_HtmlPath + os.sep + DATA_XLS


class MapWindow(QDialog):
    rectSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MapWindow, self).__init__(parent)
        self.label = QtWidgets.QLabel(self)
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


class MyThread(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)
        # 设置工作状态与初始num数值
        self.working = True
        self.num = 0

    def __del__(self):
        # 线程状态改变与线程终止
        self.working = False
        self.wait()

    def run(self):
        while self.working == True:
            # 获取文本
            self.num += 1
            # 发射信号
            self.sinOut.emit(str(self.num))
            # 线程休眠2秒
            self.sleep(1)
            if self.num == 5:
                self.working = False
