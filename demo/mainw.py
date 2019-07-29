# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(900, 900)
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
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/play_button_48px_1201205_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/stop_48px_1229026_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_9.addWidget(self.pushButton_2)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_9)
        self.gridLayout.addWidget(self.groupBox_6, 3, 0, 1, 1)
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
        self.gridLayout_7.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/map_46.16091954023px_1224917_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_7.addWidget(self.pushButton_9, 1, 1, 1, 1)
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
        self.gridLayout_7.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout.addWidget(self.radioButton_5)
        self.textEdit_right_2 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_right_2.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_right_2.setMaximumSize(QtCore.QSize(1512412, 35))
        self.textEdit_right_2.setObjectName("textEdit_right_2")
        self.horizontalLayout.addWidget(self.textEdit_right_2)
        self.gridLayout.addWidget(self.groupBox_5, 2, 0, 1, 1)
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
        self.gridLayout.addWidget(self.groupBox_3, 4, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet("QGroupBox{border:1px ridge gray;margin-top: 1ex;} QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_7.setObjectName("groupBox_7")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_7)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton:hover{\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../chrmoedownload/play_button_48px_1201205_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_4)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_7)
        self.textBrowser_3.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.textBrowser_3)
        self.gridLayout.addWidget(self.groupBox_7, 5, 0, 1, 1)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/Highway_48px_1109853_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("image/brand_brands_excel_logo_48px_1212964_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon6)
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
        self.pushButton_13.setIcon(icon2)
        self.pushButton_13.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_15.addWidget(self.pushButton_13)
        self.gridLayout_5.addLayout(self.horizontalLayout_15, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_2)
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("image/folder_48px_1219812_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon7)
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
        self.gridLayout_5.addWidget(self.groupBox_8, 3, 0, 1, 1)
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
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setObjectName("progressBar_3")
        self.horizontalLayout_16.addWidget(self.progressBar_3)
        self.gridLayout_5.addWidget(self.groupBox_9, 5, 0, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setStyleSheet("QGroupBox{border:1px ridge gray;margin-top: 1ex;} QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_8.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_8.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton:hover{\n"
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
        self.pushButton_8.setIcon(icon4)
        self.pushButton_8.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_4.addWidget(self.pushButton_8)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.groupBox_10)
        self.textBrowser_6.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.verticalLayout_4.addWidget(self.textBrowser_6)
        self.gridLayout_5.addWidget(self.groupBox_10, 6, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_13.addWidget(self.label_24)
        self.textEdit_timeweight = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_timeweight.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textEdit_timeweight.setObjectName("textEdit_timeweight")
        self.horizontalLayout_13.addWidget(self.textEdit_timeweight)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.gridLayout_5.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_8.addWidget(self.label_22)
        self.textEdit_11 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_11.setEnabled(False)
        self.textEdit_11.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textEdit_11.setObjectName("textEdit_11")
        self.horizontalLayout_8.addWidget(self.textEdit_11)
        self.pushButton_choose_road = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_choose_road.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_choose_road.setFont(font)
        self.pushButton_choose_road.setStyleSheet("QPushButton:hover{\n"
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
        icon8.addPixmap(QtGui.QPixmap("image/road_48px_1232324_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_choose_road.setIcon(icon8)
        self.pushButton_choose_road.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_choose_road.setObjectName("pushButton_choose_road")
        self.horizontalLayout_8.addWidget(self.pushButton_choose_road)
        self.gridLayout_5.addWidget(self.groupBox, 1, 0, 1, 1)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("image/gear_48px_1180534_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon9, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("image/map_64px_1228276_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon10, "")
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
        mainWindow.setWindowTitle(_translate("mainWindow", "交通拥堵分析系统"))
        self.label.setText(_translate("mainWindow", "    提示：该页面用于启动数据爬取程序，需要输入指定区域左下角的经纬度与右上角的经纬度，也可以直接使用地图选点选择矩形框。默认爬取间隔时间为120秒,时间点3 23（用空格分隔）代表抓取当天凌晨3点和23点的数据"))
        self.label_19.setText(_translate("mainWindow", " 间隔时间(秒)"))
        self.textEdit_9.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">120</p></body></html>"))
        self.pushButton.setText(_translate("mainWindow", "开始"))
        self.pushButton_2.setText(_translate("mainWindow", "停止"))
        self.groupBox_4.setTitle(_translate("mainWindow", "矩形区域配置"))
        self.label_12.setText(_translate("mainWindow", " 左下角经纬度"))
        self.pushButton_9.setText(_translate("mainWindow", "地图选点"))
        self.label_34.setText(_translate("mainWindow", " 右上角经纬度"))
        self.groupBox_5.setTitle(_translate("mainWindow", "抓取的时间点（小时）"))
        self.checkBox.setText(_translate("mainWindow", "仅工作日"))
        self.radioButton.setText(_translate("mainWindow", "早高峰"))
        self.radioButton_2.setText(_translate("mainWindow", "晚高峰"))
        self.radioButton_3.setText(_translate("mainWindow", "早+晚高峰"))
        self.radioButton_4.setText(_translate("mainWindow", "全天"))
        self.radioButton_5.setText(_translate("mainWindow", "时间点"))
        self.textEdit_right_2.setPlaceholderText(_translate("mainWindow", "2 3 4 5 23 24"))
        self.label_9.setText(_translate("mainWindow", "运行状态："))
        self.groupBox_7.setTitle(_translate("mainWindow", "日志"))
        self.pushButton_4.setText(_translate("mainWindow", "系统日志(点击收缩并清空)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "数据采集"))
        self.pushButton_14.setText(_translate("mainWindow", "生成"))
        self.pushButton_13.setText(_translate("mainWindow", "停止"))
        self.label_3.setText(_translate("mainWindow", "    提示：该页面用于启动数据生成，选择指定道路，配置拥堵时长权重（默认为0.2）后点击生成，即可生产拥堵情况excel表格，也可进入地图展示标签查看。"))
        self.pushButton_7.setText(_translate("mainWindow", "选择文件夹"))
        self.label_21.setText(_translate("mainWindow", "数据所在路径"))
        self.label_17.setText(_translate("mainWindow", "进度："))
        self.groupBox_10.setTitle(_translate("mainWindow", "日志"))
        self.pushButton_8.setText(_translate("mainWindow", "系统日志(点击收缩并清空)"))
        self.groupBox_2.setTitle(_translate("mainWindow", "权重设置"))
        self.label_24.setText(_translate("mainWindow", "拥堵时长权重（0-1）"))
        self.textEdit_timeweight.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.2</p></body></html>"))
        self.label_22.setText(_translate("mainWindow", "指定道路"))
        self.textEdit_11.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">全部</p></body></html>"))
        self.pushButton_choose_road.setText(_translate("mainWindow", "选择道路"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "数据处理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("mainWindow", "地图展示"))

