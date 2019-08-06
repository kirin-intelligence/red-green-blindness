# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(820, 940)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
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
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMinimumSize(QtCore.QSize(631, 0))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_background = QtWidgets.QLabel(self.tab)
        self.label_background.setEnabled(True)
        self.label_background.setMaximumSize(QtCore.QSize(820, 335))
        self.label_background.setStyleSheet("#label_background{\n"
"            border-color: gray;\n"
"                 margin:8px;\n"
"            border-width:1px;\n"
"                     border-radius: 6px;\n"
"                     border-style: solid;}")
        self.label_background.setText("")
        self.label_background.setPixmap(QtGui.QPixmap("image/background.jpg"))
        self.label_background.setScaledContents(True)
        self.label_background.setObjectName("label_background")
        self.horizontalLayout_4.addWidget(self.label_background)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_34 = QtWidgets.QLabel(self.groupBox_4)
        self.label_34.setMinimumSize(QtCore.QSize(140, 0))
        self.label_34.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_11.addWidget(self.label_34)
        self.textEdit_right = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_right.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_right.setMaximumSize(QtCore.QSize(1512412, 35))
        self.textEdit_right.setObjectName("textEdit_right")
        self.horizontalLayout_11.addWidget(self.textEdit_right)
        self.gridLayout_7.addLayout(self.horizontalLayout_11, 3, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton:hover{\n"
"\n"
"background-color:rgb(211, 211, 211)}  \n"
"QPushButton\n"
"                     {text-align : center;\n"
"                     border-color: gray;\n"
"                     padding:8px;\n"
"                     font:bold;\n"
"                     border-width: 1px;\n"
"                     border-radius: 5px;\n"
"                     border-style: outset;\n"
"                     }\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/locate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_7.addWidget(self.pushButton_9, 3, 1, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_10.setSpacing(4)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setMinimumSize(QtCore.QSize(140, 0))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.textEdit_left = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_left.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_left.setMaximumSize(QtCore.QSize(1512412, 35))
        self.textEdit_left.setObjectName("textEdit_left")
        self.horizontalLayout_10.addWidget(self.textEdit_left)
        self.gridLayout_7.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_19 = QtWidgets.QLabel(self.groupBox_6)
        self.label_19.setMinimumSize(QtCore.QSize(0, 0))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_9.addWidget(self.label_19)
        self.textEdit_9 = QtWidgets.QTextEdit(self.groupBox_6)
        self.textEdit_9.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_9.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_9.setObjectName("textEdit_9")
        self.horizontalLayout_9.addWidget(self.textEdit_9)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton:hover{\n"
"\n"
"background-color:rgb(211, 211, 211)}  \n"
"QPushButton\n"
"                     {text-align : center;\n"
"                     border-color: gray;\n"
"                     padding:8px;\n"
"                     font:bold;\n"
"                     border-width: 1px;\n"
"                     border-radius: 5px;\n"
"                     border-style: outset;\n"
"                     }\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_9.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton:hover{\n"
"\n"
"background-color:rgb(211, 211, 211)}  \n"
"QPushButton\n"
"                     {text-align : center;\n"
"                     border-color: gray;\n"
"                     padding:8px;\n"
"                     font:bold;\n"
"                     border-width: 1px;\n"
"                     border-radius: 5px;\n"
"                     border-style: outset;\n"
"                     }\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_9.addWidget(self.pushButton_2)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_9)
        self.gridLayout.addWidget(self.groupBox_6, 4, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("QGroupBox{border:1px ridge gray;margin-top: 1ex;} QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"                           border: 2px solid grey;\n"
"                           border-radius: 5px;\n"
"                           text-align: center;\n"
"                       }\n"
"                       QProgressBar::chunk {\n"
"                           background-color: #37DA7E;\n"
"                           width: 20px;\n"
"                       }")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_7.addWidget(self.progressBar)
        self.gridLayout.addWidget(self.groupBox_3, 5, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout.addWidget(self.radioButton_4)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout.addWidget(self.radioButton_5)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit.setMaximumSize(QtCore.QSize(13123, 40))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.gridLayout.addWidget(self.groupBox_5, 2, 0, 1, 1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/road.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("QPushButton:hover{\n"
"\n"
"background-color:rgb(211, 211, 211)}  \n"
"QPushButton\n"
"                     {text-align : center;\n"
"                     border-color: gray;\n"
"                     padding:8px;\n"
"                     font:bold;\n"
"                     border-width: 1px;\n"
"                     border-radius: 5px;\n"
"                     border-style: outset;\n"
"                     }\n"
"")
        self.pushButton_14.setIcon(icon2)
        self.pushButton_14.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_15.addWidget(self.pushButton_14)
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("QPushButton:hover{\n"
"\n"
"background-color:rgb(211, 211, 211)}  \n"
"QPushButton\n"
"                     {text-align : center;\n"
"                     border-color: gray;\n"
"                     padding:8px;\n"
"                     font:bold;\n"
"                     border-width: 1px;\n"
"                     border-radius: 5px;\n"
"                     border-style: outset;\n"
"                     }\n"
"")
        self.pushButton_13.setIcon(icon3)
        self.pushButton_13.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_15.addWidget(self.pushButton_13)
        self.gridLayout_3.addLayout(self.horizontalLayout_15, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(1)
        self.label_3.setMidLineWidth(0)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 7, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_10.setChecked(False)
        self.radioButton_10.setObjectName("radioButton_10")
        self.horizontalLayout_3.addWidget(self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_11.setObjectName("radioButton_11")
        self.horizontalLayout_3.addWidget(self.radioButton_11)
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_9.setChecked(True)
        self.radioButton_9.setObjectName("radioButton_9")
        self.horizontalLayout_3.addWidget(self.radioButton_9)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_11.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_11.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_25 = QtWidgets.QLabel(self.groupBox_11)
        self.label_25.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_2.addWidget(self.label_25)
        self.textEdit_red = QtWidgets.QTextEdit(self.groupBox_11)
        self.textEdit_red.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textEdit_red.setObjectName("textEdit_red")
        self.horizontalLayout_2.addWidget(self.textEdit_red)
        self.label_26 = QtWidgets.QLabel(self.groupBox_11)
        self.label_26.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_2.addWidget(self.label_26)
        self.textEdit_yellow = QtWidgets.QTextEdit(self.groupBox_11)
        self.textEdit_yellow.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textEdit_yellow.setObjectName("textEdit_yellow")
        self.horizontalLayout_2.addWidget(self.textEdit_yellow)
        self.label_27 = QtWidgets.QLabel(self.groupBox_11)
        self.label_27.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_2.addWidget(self.label_27)
        self.textEdit_green = QtWidgets.QTextEdit(self.groupBox_11)
        self.textEdit_green.setEnabled(True)
        self.textEdit_green.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textEdit_green.setObjectName("textEdit_green")
        self.horizontalLayout_2.addWidget(self.textEdit_green)
        self.gridLayout_3.addWidget(self.groupBox_11, 2, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_8.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_8.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textEdit_7.setObjectName("textEdit_7")
        self.gridLayout_6.addWidget(self.textEdit_7, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton:hover{\n"
"\n"
"background-color:rgb(211, 211, 211)}  \n"
"QPushButton\n"
"                     {text-align : center;\n"
"                     border-color: gray;\n"
"                     padding:8px;\n"
"                     font:bold;\n"
"                     border-width: 1px;\n"
"                     border-radius: 5px;\n"
"                     border-style: outset;\n"
"                     }\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/folder_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_6.addWidget(self.pushButton_7, 0, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_8)
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_8, 3, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setStyleSheet("QGroupBox{border:1px ridge gray;margin-top: 1ex;} QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_9)
        self.label_17.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_16.addWidget(self.label_17)
        self.progressBar_3 = QtWidgets.QProgressBar(self.groupBox_9)
        self.progressBar_3.setStyleSheet("QProgressBar {\n"
"                           border: 2px solid grey;\n"
"                           border-radius: 5px;\n"
"                           text-align: center;\n"
"                       }\n"
"                       QProgressBar::chunk {\n"
"                           background-color: #37DA7E;\n"
"                           width: 20px;\n"
"                       }")
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setTextVisible(True)
        self.progressBar_3.setObjectName("progressBar_3")
        self.horizontalLayout_16.addWidget(self.progressBar_3)
        self.gridLayout_3.addWidget(self.groupBox_9, 6, 0, 1, 1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("image/manger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon6, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("image/mapl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon7, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 0, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 0, 0, 1, 1)
        self.textEdit_timeweight = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_timeweight.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textEdit_timeweight.setObjectName("textEdit_timeweight")
        self.gridLayout_5.addWidget(self.textEdit_timeweight, 0, 1, 1, 1)
        self.textEdit_lengthweight = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_lengthweight.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textEdit_lengthweight.setObjectName("textEdit_lengthweight")
        self.gridLayout_5.addWidget(self.textEdit_lengthweight, 0, 4, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("QPushButton:hover{\n"
"\n"
"background-color:rgb(211, 211, 211)}  \n"
"QPushButton\n"
"                     {text-align : center;\n"
"                     border-color: gray;\n"
"                     padding:8px;\n"
"                     font:bold;\n"
"                     border-width: 1px;\n"
"                     border-radius: 5px;\n"
"                     border-style: outset;\n"
"                     }\n"
"")
        self.pushButton_15.setIcon(icon2)
        self.pushButton_15.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_5.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("QPushButton:hover{\n"
"\n"
"background-color:rgb(211, 211, 211)}  \n"
"QPushButton\n"
"                     {text-align : center;\n"
"                     border-color: gray;\n"
"                     padding:8px;\n"
"                     font:bold;\n"
"                     border-width: 1px;\n"
"                     border-radius: 5px;\n"
"                     border-style: outset;\n"
"                     }\n"
"")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("image/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_16.setIcon(icon8)
        self.pushButton_16.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_5.addWidget(self.pushButton_16)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setLineWidth(1)
        self.label_4.setMidLineWidth(0)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("image/analyse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon9, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "全自动交通拥堵点识别和评价系统"))
        self.label.setText(_translate("mainWindow", "    提示：该页面用于数据采集。1、点击地图选取，框出需要爬取数据的矩形区域。2、设置抓取时间段。其中勾选时间点后输入：7 12 21  空格分隔,代表每天7点，12点，晚上9点进行数据抓取。3、设置时间间隔，默认为120秒。4、点击开始，程序自动后台运行。运行日志存放在log文件夹中。"))
        self.groupBox_4.setTitle(_translate("mainWindow", "矩形区域配置"))
        self.label_34.setText(_translate("mainWindow", " 右上角经纬度"))
        self.pushButton_9.setText(_translate("mainWindow", "地图选点"))
        self.label_12.setText(_translate("mainWindow", " 左下角经纬度"))
        self.label_19.setText(_translate("mainWindow", " 间隔时间(秒)"))
        self.textEdit_9.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">120</p></body></html>"))
        self.pushButton.setText(_translate("mainWindow", "开始"))
        self.pushButton_2.setText(_translate("mainWindow", "停止"))
        self.label_9.setText(_translate("mainWindow", "运行状态："))
        self.groupBox_5.setTitle(_translate("mainWindow", "抓取时间段"))
        self.checkBox.setText(_translate("mainWindow", "仅工作日"))
        self.radioButton_4.setText(_translate("mainWindow", "全天"))
        self.radioButton.setText(_translate("mainWindow", "早高峰"))
        self.radioButton_2.setText(_translate("mainWindow", "晚高峰"))
        self.radioButton_3.setText(_translate("mainWindow", "早晚高峰"))
        self.radioButton_5.setText(_translate("mainWindow", "时间点"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "数据采集"))
        self.pushButton_14.setText(_translate("mainWindow", "生成"))
        self.pushButton_13.setText(_translate("mainWindow", "停止"))
        self.label_3.setText(_translate("mainWindow", "    提示：该页面用于数据处理，1、选择指定道路。2、设置拥堵等级阈值，红点比例0.8代表拥堵超过80%的点为红色拥堵点，橙黄点比例0.5代表拥堵超过50%且不超过80%的点为黄色拥堵点。3、选择采集后数据所在文件夹。5、点击生成，即可生成拥堵情况数据，可进入拥堵点识别或拥堵点评价标签查看分析。"))
        self.groupBox.setTitle(_translate("mainWindow", "指定道路"))
        self.radioButton_10.setText(_translate("mainWindow", "快速路"))
        self.radioButton_11.setText(_translate("mainWindow", "一般路"))
        self.radioButton_9.setText(_translate("mainWindow", "所有路段"))
        self.groupBox_11.setTitle(_translate("mainWindow", "拥堵等级阈值(0-1)"))
        self.label_25.setText(_translate("mainWindow", "红点比例"))
        self.textEdit_red.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.8</p></body></html>"))
        self.label_26.setText(_translate("mainWindow", "橙黄点比例"))
        self.textEdit_yellow.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.5</p></body></html>"))
        self.label_27.setText(_translate("mainWindow", "黄点比例"))
        self.textEdit_green.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.2</p></body></html>"))
        self.pushButton_7.setText(_translate("mainWindow", "选择文件夹"))
        self.label_21.setText(_translate("mainWindow", "数据所在路径"))
        self.label_17.setText(_translate("mainWindow", "完成进度："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "数据处理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("mainWindow", "拥堵点识别"))
        self.groupBox_2.setTitle(_translate("mainWindow", "权重设置"))
        self.label_28.setText(_translate("mainWindow", "拥堵距离权重"))
        self.label_24.setText(_translate("mainWindow", "拥堵时长权重"))
        self.textEdit_timeweight.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.2</p></body></html>"))
        self.textEdit_lengthweight.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.5</p></body></html>"))
        self.pushButton_15.setText(_translate("mainWindow", "生成"))
        self.pushButton_16.setText(_translate("mainWindow", "导出"))
        self.label_4.setText(_translate("mainWindow", "    提示：该页面用于数据处理，1、输入拥堵道路时间和拥堵道路时长的权重（为任意值）。2、点击生成，则显示table。3、点击导出，按照table中的顺序生成excel表格。"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("mainWindow", "拥堵点评价"))

