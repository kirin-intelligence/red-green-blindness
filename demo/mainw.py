# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1045, 821)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(30, 30))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_3.setGeometry(QtCore.QRect(70, 460, 861, 221))
        self.textBrowser_3.setMinimumSize(QtCore.QSize(641, 0))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(70, 410, 60, 39))
        self.label_7.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(590, 300, 151, 51))
        self.pushButton.setMinimumSize(QtCore.QSize(101, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/play_button_48px_1201205_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(770, 300, 151, 51))
        self.pushButton_2.setMinimumSize(QtCore.QSize(101, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/stop_48px_1229026_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(70, 370, 871, 41))
        self.progressBar.setMinimumSize(QtCore.QSize(641, 0))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(160, 30, 631, 81))
        self.label.setMinimumSize(QtCore.QSize(631, 0))
        self.label.setObjectName("label")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(70, 310, 111, 21))
        self.label_19.setMinimumSize(QtCore.QSize(111, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.textEdit_9 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_9.setGeometry(QtCore.QRect(200, 310, 61, 21))
        self.textEdit_9.setMinimumSize(QtCore.QSize(61, 0))
        self.textEdit_9.setObjectName("textEdit_9")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(70, 220, 71, 41))
        self.label_5.setMinimumSize(QtCore.QSize(71, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.tab)
        self.dateTimeEdit.setGeometry(QtCore.QRect(170, 230, 181, 21))
        self.dateTimeEdit.setMinimumSize(QtCore.QSize(181, 0))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(70, 150, 101, 31))
        self.label_4.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(170, 150, 201, 31))
        self.textEdit.setMinimumSize(QtCore.QSize(201, 0))
        self.textEdit.setObjectName("textEdit")
        self.label_32 = QtWidgets.QLabel(self.tab)
        self.label_32.setGeometry(QtCore.QRect(590, 150, 101, 31))
        self.label_32.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.textEdit_13 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_13.setGeometry(QtCore.QRect(690, 150, 201, 31))
        self.textEdit_13.setMinimumSize(QtCore.QSize(201, 0))
        self.textEdit_13.setObjectName("textEdit_13")
        self.dateTimeEdit_9 = QtWidgets.QDateTimeEdit(self.tab)
        self.dateTimeEdit_9.setGeometry(QtCore.QRect(690, 230, 209, 20))
        self.dateTimeEdit_9.setMinimumSize(QtCore.QSize(209, 0))
        self.dateTimeEdit_9.setObjectName("dateTimeEdit_9")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(590, 220, 71, 41))
        self.label_6.setMinimumSize(QtCore.QSize(71, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/gear_48px_1180534_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon2, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 290, 101, 51))
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_6.setGeometry(QtCore.QRect(79, 459, 851, 241))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(680, 290, 101, 51))
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(79, 419, 60, 39))
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_3.setGeometry(QtCore.QRect(79, 359, 841, 31))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(170, 60, 571, 21))
        self.label_2.setObjectName("label_2")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(170, 90, 571, 21))
        self.label_18.setObjectName("label_18")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_13.setGeometry(QtCore.QRect(800, 290, 101, 51))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/brand_brands_excel_logo_48px_1212964_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon3)
        self.pushButton_13.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(80, 170, 90, 71))
        self.label_17.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(590, 190, 101, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.textEdit_7 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_7.setGeometry(QtCore.QRect(180, 190, 401, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/about_help_smart_watch_35.185520361991px_1225400_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/map_46.16091954023px_1224917_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.gridLayout_3.addWidget(self.textBrowser_10, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, icon4, "")
        self.horizontalLayout_11.addWidget(self.tabWidget)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "交通拥堵分析系统"))
        self.label_7.setText(_translate("mainWindow", "系统日志"))
        self.pushButton.setText(_translate("mainWindow", "开始"))
        self.pushButton_2.setText(_translate("mainWindow", "停止"))
        self.label.setText(_translate("mainWindow", "提示：该页面用于启动数据爬取程序，需要输入指定区域左上角的经纬度与右角的经纬度。间隔时间默认为2分钟"))
        self.label_19.setText(_translate("mainWindow", "间隔时间(分钟)"))
        self.textEdit_9.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2</p></body></html>"))
        self.label_5.setText(_translate("mainWindow", "开始时间"))
        self.label_4.setText(_translate("mainWindow", "左上角经纬度"))
        self.label_32.setText(_translate("mainWindow", "右下角经纬度"))
        self.label_6.setText(_translate("mainWindow", "开始时间"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "数据采集"))
        self.pushButton_5.setText(_translate("mainWindow", "开始生成"))
        self.pushButton_6.setText(_translate("mainWindow", "停止"))
        self.label_21.setText(_translate("mainWindow", "系统日志"))
        self.label_2.setText(_translate("mainWindow", "提示：该页面用于启动数据生成，选择数据所在的文件夹。点击生成，即可显示生成后的拥堵情况文件。"))
        self.label_18.setText(_translate("mainWindow", "生成文件可通过点击生成EXCEl查看或者进入地图展示查看。"))
        self.pushButton_13.setText(_translate("mainWindow", "生成excel"))
        self.label_17.setText(_translate("mainWindow", "数据存储路径"))
        self.pushButton_7.setText(_translate("mainWindow", "选择文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "数据处理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("mainWindow", "地图展示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("mainWindow", "关于我们"))

