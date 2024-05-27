from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 679)
        MainWindow.setStyleSheet("background-color: rgb(85, 85, 85);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(30, 0, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.time.setFont(font)
        self.time.setStyleSheet(" color:#ffffff;\n"
"")
        self.time.setText("")
        self.time.setObjectName("time")
        self.label_charging = QtWidgets.QLabel(self.centralwidget)
        self.label_charging.setGeometry(QtCore.QRect(950, 0, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_charging.setFont(font)
        self.label_charging.setStyleSheet(" color:#ffffff;")
        self.label_charging.setText("")
        self.label_charging.setScaledContents(True)
        self.label_charging.setObjectName("label_charging")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, 29, 1021, 651))
        self.widget.setStyleSheet("background-color: rgb(104, 104, 104);")
        self.widget.setObjectName("widget")
        self.label_div = QtWidgets.QLabel(self.widget)
        self.label_div.setGeometry(QtCore.QRect(60, 60, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_div.setFont(font)
        self.label_div.setStyleSheet("")
        self.label_div.setObjectName("label_div")
        self.pushButton_20 = QtWidgets.QPushButton(self.widget)
        self.pushButton_20.setGeometry(QtCore.QRect(60, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,50);\n"
"border: 1px solid  rgb(255, 255, 255,50) ;\n"
"border-radius: 12px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 170, 255);\n"
"}")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.widget)
        self.pushButton_21.setGeometry(QtCore.QRect(190, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,50);\n"
"border: 1px solid  rgb(255, 255, 255,50) ;\n"
"border-radius: 12px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 170, 255);\n"
"}")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.widget)
        self.pushButton_22.setGeometry(QtCore.QRect(330, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,50);\n"
"border: 1px solid  rgb(255, 255, 255,50) ;\n"
"border-radius: 12px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 170, 255);\n"
"}")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.widget)
        self.pushButton_23.setGeometry(QtCore.QRect(470, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,50);\n"
"border: 1px solid  rgb(255, 255, 255,50) ;\n"
"border-radius: 12px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 170, 255);\n"
"}")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.widget)
        self.pushButton_24.setGeometry(QtCore.QRect(610, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,50);\n"
"border: 1px solid  rgb(255, 255, 255,50) ;\n"
"border-radius: 12px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.widget)
        self.pushButton_25.setGeometry(QtCore.QRect(750, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,50);\n"
"border: 1px solid  rgb(255, 255, 255,50) ;\n"
"border-radius: 12px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 170, 255);\n"
"}")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.widget)
        self.pushButton_26.setGeometry(QtCore.QRect(880, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,50);\n"
"border: 1px solid  rgb(255, 255, 255,50) ;\n"
"border-radius: 12px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(170, 170, 255);\n"
"}")
        self.pushButton_26.setObjectName("pushButton_26")
        self.label_pn = QtWidgets.QLabel(self.widget)
        self.label_pn.setGeometry(QtCore.QRect(70, 160, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_pn.setFont(font)
        self.label_pn.setStyleSheet("")
        self.label_pn.setObjectName("label_pn")
        self.label_vt = QtWidgets.QLabel(self.widget)
        self.label_vt.setGeometry(QtCore.QRect(200, 160, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_vt.setFont(font)
        self.label_vt.setStyleSheet("")
        self.label_vt.setObjectName("label_vt")
        self.label_sr = QtWidgets.QLabel(self.widget)
        self.label_sr.setGeometry(QtCore.QRect(340, 160, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_sr.setFont(font)
        self.label_sr.setStyleSheet("")
        self.label_sr.setObjectName("label_sr")
        self.label_cht = QtWidgets.QLabel(self.widget)
        self.label_cht.setGeometry(QtCore.QRect(480, 160, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_cht.setFont(font)
        self.label_cht.setStyleSheet("")
        self.label_cht.setObjectName("label_cht")
        self.label_pt = QtWidgets.QLabel(self.widget)
        self.label_pt.setGeometry(QtCore.QRect(620, 160, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_pt.setFont(font)
        self.label_pt.setStyleSheet("")
        self.label_pt.setObjectName("label_pt")
        self.label_sb = QtWidgets.QLabel(self.widget)
        self.label_sb.setGeometry(QtCore.QRect(760, 160, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_sb.setFont(font)
        self.label_sb.setStyleSheet("")
        self.label_sb.setObjectName("label_sb")
        self.label_vs = QtWidgets.QLabel(self.widget)
        self.label_vs.setGeometry(QtCore.QRect(890, 160, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_vs.setFont(font)
        self.label_vs.setStyleSheet("")
        self.label_vs.setObjectName("label_vs")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(40, 220, 931, 401))
        self.widget_2.setObjectName("widget_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_2)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 931, 401))
        self.stackedWidget.setAccessibleDescription("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame_1 = QtWidgets.QFrame(self.page)
        self.frame_1.setGeometry(QtCore.QRect(0, 0, 931, 401))
        self.frame_1.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"border-radius: 12px\n"
"")
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.widget_3 = QtWidgets.QWidget(self.frame_1)
        self.widget_3.setGeometry(QtCore.QRect(60, 30, 801, 101))
        self.widget_3.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser.setGeometry(QtCore.QRect(180, 10, 481, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.pn_1 = QtWidgets.QPushButton(self.widget_3)
        self.pn_1.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pn_1.setFont(font)
        self.pn_1.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.pn_1.setObjectName("pn_1")
        self.widget_4 = QtWidgets.QWidget(self.frame_1)
        self.widget_4.setGeometry(QtCore.QRect(60, 160, 801, 101))
        self.widget_4.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_4.setObjectName("widget_4")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"")
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget_4)
        self.textBrowser_2.setGeometry(QtCore.QRect(180, 10, 481, 81))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pn_2 = QtWidgets.QPushButton(self.widget_4)
        self.pn_2.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pn_2.setFont(font)
        self.pn_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.pn_2.setObjectName("pn_2")
        self.widget_5 = QtWidgets.QWidget(self.frame_1)
        self.widget_5.setGeometry(QtCore.QRect(60, 280, 801, 101))
        self.widget_5.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_5.setObjectName("widget_5")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_3.setObjectName("label_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.widget_5)
        self.textBrowser_3.setGeometry(QtCore.QRect(170, 10, 481, 81))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pn_3 = QtWidgets.QPushButton(self.widget_5)
        self.pn_3.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pn_3.setFont(font)
        self.pn_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.pn_3.setObjectName("pn_3")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_2 = QtWidgets.QFrame(self.page_2)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 931, 401))
        self.frame_2.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"border-radius: 12px\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.widget_6 = QtWidgets.QWidget(self.frame_2)
        self.widget_6.setGeometry(QtCore.QRect(60, 30, 801, 101))
        self.widget_6.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_6.setObjectName("widget_6")
        self.label_4 = QtWidgets.QLabel(self.widget_6)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_4.setObjectName("label_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.widget_6)
        self.textBrowser_4.setGeometry(QtCore.QRect(180, 10, 481, 81))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.vt_1 = QtWidgets.QPushButton(self.widget_6)
        self.vt_1.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vt_1.setFont(font)
        self.vt_1.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.vt_1.setObjectName("vt_1")
        self.widget_7 = QtWidgets.QWidget(self.frame_2)
        self.widget_7.setGeometry(QtCore.QRect(60, 160, 801, 101))
        self.widget_7.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_7.setObjectName("widget_7")
        self.label_5 = QtWidgets.QLabel(self.widget_7)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_5.setObjectName("label_5")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.widget_7)
        self.textBrowser_5.setGeometry(QtCore.QRect(180, 10, 481, 81))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.vt_2 = QtWidgets.QPushButton(self.widget_7)
        self.vt_2.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vt_2.setFont(font)
        self.vt_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.vt_2.setObjectName("vt_2")
        self.widget_8 = QtWidgets.QWidget(self.frame_2)
        self.widget_8.setGeometry(QtCore.QRect(60, 280, 801, 101))
        self.widget_8.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_8.setObjectName("widget_8")
        self.label_6 = QtWidgets.QLabel(self.widget_8)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_6.setObjectName("label_6")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.widget_8)
        self.textBrowser_6.setGeometry(QtCore.QRect(170, 10, 481, 81))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.vt_3 = QtWidgets.QPushButton(self.widget_8)
        self.vt_3.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vt_3.setFont(font)
        self.vt_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.vt_3.setObjectName("vt_3")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.frame_3 = QtWidgets.QFrame(self.page_3)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 931, 401))
        self.frame_3.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"border-radius: 12px\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.widget_10 = QtWidgets.QWidget(self.frame_3)
        self.widget_10.setGeometry(QtCore.QRect(70, 70, 801, 101))
        self.widget_10.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_10.setObjectName("widget_10")
        self.label_8 = QtWidgets.QLabel(self.widget_10)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_8.setObjectName("label_8")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.widget_10)
        self.textBrowser_8.setGeometry(QtCore.QRect(180, 10, 481, 81))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.sr_1 = QtWidgets.QPushButton(self.widget_10)
        self.sr_1.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sr_1.setFont(font)
        self.sr_1.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.sr_1.setObjectName("sr_1")
        self.widget_11 = QtWidgets.QWidget(self.frame_3)
        self.widget_11.setGeometry(QtCore.QRect(70, 230, 801, 101))
        self.widget_11.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_11.setObjectName("widget_11")
        self.label_9 = QtWidgets.QLabel(self.widget_11)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_9.setObjectName("label_9")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.widget_11)
        self.textBrowser_9.setGeometry(QtCore.QRect(170, 10, 481, 81))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.sr_2 = QtWidgets.QPushButton(self.widget_11)
        self.sr_2.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sr_2.setFont(font)
        self.sr_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.sr_2.setObjectName("sr_2")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.frame_4 = QtWidgets.QFrame(self.page_4)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 931, 401))
        self.frame_4.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"border-radius: 12px\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.widget_12 = QtWidgets.QWidget(self.frame_4)
        self.widget_12.setGeometry(QtCore.QRect(60, 30, 801, 101))
        self.widget_12.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_12.setObjectName("widget_12")
        self.label_10 = QtWidgets.QLabel(self.widget_12)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_10.setObjectName("label_10")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.widget_12)
        self.textBrowser_10.setGeometry(QtCore.QRect(180, 10, 481, 81))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.cht_1 = QtWidgets.QPushButton(self.widget_12)
        self.cht_1.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cht_1.setFont(font)
        self.cht_1.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.cht_1.setObjectName("cht_1")
        self.widget_13 = QtWidgets.QWidget(self.frame_4)
        self.widget_13.setGeometry(QtCore.QRect(60, 160, 801, 101))
        self.widget_13.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_13.setObjectName("widget_13")
        self.label_11 = QtWidgets.QLabel(self.widget_13)
        self.label_11.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_11.setObjectName("label_11")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.widget_13)
        self.textBrowser_11.setGeometry(QtCore.QRect(180, 10, 481, 81))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.cht_2 = QtWidgets.QPushButton(self.widget_13)
        self.cht_2.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cht_2.setFont(font)
        self.cht_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.cht_2.setObjectName("cht_2")
        self.widget_14 = QtWidgets.QWidget(self.frame_4)
        self.widget_14.setGeometry(QtCore.QRect(60, 280, 801, 101))
        self.widget_14.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_14.setObjectName("widget_14")
        self.label_12 = QtWidgets.QLabel(self.widget_14)
        self.label_12.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_12.setObjectName("label_12")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.widget_14)
        self.textBrowser_12.setGeometry(QtCore.QRect(170, 10, 481, 81))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.cht_3 = QtWidgets.QPushButton(self.widget_14)
        self.cht_3.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cht_3.setFont(font)
        self.cht_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.cht_3.setObjectName("cht_3")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.frame_5 = QtWidgets.QFrame(self.page_5)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 931, 401))
        self.frame_5.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"border-radius: 12px\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.widget_15 = QtWidgets.QWidget(self.frame_5)
        self.widget_15.setGeometry(QtCore.QRect(60, 30, 801, 101))
        self.widget_15.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_15.setObjectName("widget_15")
        self.label_13 = QtWidgets.QLabel(self.widget_15)
        self.label_13.setGeometry(QtCore.QRect(20, 20, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_13.setObjectName("label_13")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.widget_15)
        self.textBrowser_13.setGeometry(QtCore.QRect(180, 10, 481, 81))
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.pt_1 = QtWidgets.QPushButton(self.widget_15)
        self.pt_1.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pt_1.setFont(font)
        self.pt_1.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.pt_1.setObjectName("pt_1")
        self.widget_16 = QtWidgets.QWidget(self.frame_5)
        self.widget_16.setGeometry(QtCore.QRect(60, 160, 801, 101))
        self.widget_16.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_16.setObjectName("widget_16")
        self.label_14 = QtWidgets.QLabel(self.widget_16)
        self.label_14.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_14.setObjectName("label_14")
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.widget_16)
        self.textBrowser_14.setGeometry(QtCore.QRect(180, 10, 481, 81))
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.pt_2 = QtWidgets.QPushButton(self.widget_16)
        self.pt_2.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pt_2.setFont(font)
        self.pt_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.pt_2.setObjectName("pt_2")
        self.widget_17 = QtWidgets.QWidget(self.frame_5)
        self.widget_17.setGeometry(QtCore.QRect(60, 280, 801, 101))
        self.widget_17.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_17.setObjectName("widget_17")
        self.label_15 = QtWidgets.QLabel(self.widget_17)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_15.setObjectName("label_15")
        self.textBrowser_15 = QtWidgets.QTextBrowser(self.widget_17)
        self.textBrowser_15.setGeometry(QtCore.QRect(170, 10, 481, 81))
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.pt_3 = QtWidgets.QPushButton(self.widget_17)
        self.pt_3.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pt_3.setFont(font)
        self.pt_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.pt_3.setObjectName("pt_3")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.frame_6 = QtWidgets.QFrame(self.page_6)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 931, 401))
        self.frame_6.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"border-radius: 12px\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.widget_19 = QtWidgets.QWidget(self.frame_6)
        self.widget_19.setGeometry(QtCore.QRect(60, 60, 801, 101))
        self.widget_19.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_19.setObjectName("widget_19")
        self.label_17 = QtWidgets.QLabel(self.widget_19)
        self.label_17.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_17.setObjectName("label_17")
        self.textBrowser_17 = QtWidgets.QTextBrowser(self.widget_19)
        self.textBrowser_17.setGeometry(QtCore.QRect(180, 10, 481, 81))
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.sb_1 = QtWidgets.QPushButton(self.widget_19)
        self.sb_1.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sb_1.setFont(font)
        self.sb_1.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.sb_1.setObjectName("sb_1")
        self.widget_20 = QtWidgets.QWidget(self.frame_6)
        self.widget_20.setGeometry(QtCore.QRect(60, 220, 801, 101))
        self.widget_20.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_20.setObjectName("widget_20")
        self.label_18 = QtWidgets.QLabel(self.widget_20)
        self.label_18.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_18.setObjectName("label_18")
        self.textBrowser_18 = QtWidgets.QTextBrowser(self.widget_20)
        self.textBrowser_18.setGeometry(QtCore.QRect(170, 10, 481, 81))
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.sb_2 = QtWidgets.QPushButton(self.widget_20)
        self.sb_2.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sb_2.setFont(font)
        self.sb_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.sb_2.setObjectName("sb_2")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.frame_7 = QtWidgets.QFrame(self.page_7)
        self.frame_7.setGeometry(QtCore.QRect(0, 0, 931, 401))
        self.frame_7.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"border-radius: 12px\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.widget_22 = QtWidgets.QWidget(self.frame_7)
        self.widget_22.setGeometry(QtCore.QRect(70, 60, 801, 101))
        self.widget_22.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_22.setObjectName("widget_22")
        self.label_20 = QtWidgets.QLabel(self.widget_22)
        self.label_20.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_20.setObjectName("label_20")
        self.textBrowser_20 = QtWidgets.QTextBrowser(self.widget_22)
        self.textBrowser_20.setGeometry(QtCore.QRect(180, 10, 481, 81))
        self.textBrowser_20.setObjectName("textBrowser_20")
        self.vs_1 = QtWidgets.QPushButton(self.widget_22)
        self.vs_1.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vs_1.setFont(font)
        self.vs_1.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.vs_1.setObjectName("vs_1")
        self.widget_23 = QtWidgets.QWidget(self.frame_7)
        self.widget_23.setGeometry(QtCore.QRect(70, 210, 801, 101))
        self.widget_23.setStyleSheet("background-color: rgb(213, 210, 255);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"")
        self.widget_23.setObjectName("widget_23")
        self.label_21 = QtWidgets.QLabel(self.widget_23)
        self.label_21.setGeometry(QtCore.QRect(20, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_21.setObjectName("label_21")
        self.textBrowser_21 = QtWidgets.QTextBrowser(self.widget_23)
        self.textBrowser_21.setGeometry(QtCore.QRect(170, 10, 481, 81))
        self.textBrowser_21.setObjectName("textBrowser_21")
        self.vs_2 = QtWidgets.QPushButton(self.widget_23)
        self.vs_2.setGeometry(QtCore.QRect(670, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vs_2.setFont(font)
        self.vs_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(168, 161, 175);\n"
"}")
        self.vs_2.setObjectName("vs_2")
        self.stackedWidget.addWidget(self.page_7)
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1021, 51))
        self.frame.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_name = QtWidgets.QLabel(self.frame)
        self.label_name.setGeometry(QtCore.QRect(110, 0, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("color:rgb(0, 0, 0)")
        self.label_name.setObjectName("label_name")
        self.label_month = QtWidgets.QLabel(self.widget)
        self.label_month.setGeometry(QtCore.QRect(670, 70, 91, 31))
        self.label_month.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"border-radius: 12px\n"
"")
        self.label_month.setObjectName("label_month")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_div.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Делай как Алинка, будешь как Малинка!</span></p></body></html>"))
        self.pushButton_20.setText(_translate("MainWindow", "20"))
        self.pushButton_21.setText(_translate("MainWindow", "21"))
        self.pushButton_22.setText(_translate("MainWindow", "22"))
        self.pushButton_23.setText(_translate("MainWindow", "23"))
        self.pushButton_24.setText(_translate("MainWindow", "24"))
        self.pushButton_25.setText(_translate("MainWindow", "25"))
        self.pushButton_26.setText(_translate("MainWindow", "26"))
        self.label_pn.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:normal; color:#ffffff;\">ПН</span></p></body></html>"))
        self.label_vt.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:normal; color:#ffffff;\">ВТ</span></p></body></html>"))
        self.label_sr.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:normal; color:#ffffff;\">СР</span></p></body></html>"))
        self.label_cht.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:normal; color:#ffffff;\">ЧТ</span></p></body></html>"))
        self.label_pt.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:normal; color:#ffffff;\">ПТ</span></p></body></html>"))
        self.label_sb.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:normal; color:#ffffff;\">СБ</span></p></body></html>"))
        self.label_vs.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:normal; color:#ffffff;\">ВС</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "08:00 - 09:00"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">STRETCHING</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Малый зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Мария</span></p></body></html>"))
        self.pn_1.setText(_translate("MainWindow", "Записаться"))
        self.label_2.setText(_translate("MainWindow", "18:00 - 19:00"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">STRETCHING</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Малый зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Карина</span></p></body></html>"))
        self.pn_2.setText(_translate("MainWindow", "Записаться"))
        self.label_3.setText(_translate("MainWindow", "19:00 - 20:00"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">PILATES</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Малый зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Альбина</span></p></body></html>"))
        self.pn_3.setText(_translate("MainWindow", "Записаться"))
        self.label_4.setText(_translate("MainWindow", "08:00 - 09:00"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">INTERVAL</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Большой зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Олег</span></p></body></html>"))
        self.vt_1.setText(_translate("MainWindow", "Записаться"))
        self.label_5.setText(_translate("MainWindow", "18:00 - 19:00"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">YOGA</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Зеркальный зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Екатерина</span></p></body></html>"))
        self.vt_2.setText(_translate("MainWindow", "Записаться"))
        self.label_6.setText(_translate("MainWindow", "19:00 - 20:00"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">YOGA</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Зеркальный зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Арсений</span></p></body></html>"))
        self.vt_3.setText(_translate("MainWindow", "Записаться"))
        self.label_8.setText(_translate("MainWindow", "09:00 - 10:00"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">PILATES</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Малый зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Альбина</span></p></body></html>"))
        self.sr_1.setText(_translate("MainWindow", "Записаться"))
        self.label_9.setText(_translate("MainWindow", "19:00 - 20:00"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">YOGA</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Зеркальный зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Арсений</span></p></body></html>"))
        self.sr_2.setText(_translate("MainWindow", "Записаться"))
        self.label_10.setText(_translate("MainWindow", "11:00 - 12:00"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">YOGA</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Зеркальный зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Альбина</span></p></body></html>"))
        self.cht_1.setText(_translate("MainWindow", "Записаться"))
        self.label_11.setText(_translate("MainWindow", "18:00 - 19:00"))
        self.textBrowser_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">ABS</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Большой зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Станислав</span></p></body></html>"))
        self.cht_2.setText(_translate("MainWindow", "Записаться"))
        self.label_12.setText(_translate("MainWindow", "19:00 - 20:00"))
        self.textBrowser_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">PILATES</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Малый зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Альбина</span></p></body></html>"))
        self.cht_3.setText(_translate("MainWindow", "Записаться"))
        self.label_13.setText(_translate("MainWindow", "8:00 - 9:00"))
        self.textBrowser_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">STRETCHING</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Малый зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Мария</span></p></body></html>"))
        self.pt_1.setText(_translate("MainWindow", "Записаться"))
        self.label_14.setText(_translate("MainWindow", "18:00 - 19:00"))
        self.textBrowser_14.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">TRX</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Большой зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Алексей</span></p></body></html>"))
        self.pt_2.setText(_translate("MainWindow", "Записаться"))
        self.label_15.setText(_translate("MainWindow", "19:00 - 20:00"))
        self.textBrowser_15.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">VOGUE DANCE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Зеркальный зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Кристина</span></p></body></html>"))
        self.pt_3.setText(_translate("MainWindow", "Записаться"))
        self.label_17.setText(_translate("MainWindow", "09:00 - 10:00"))
        self.textBrowser_17.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">INTERVAL</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Большой зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Олег</span></p></body></html>"))
        self.sb_1.setText(_translate("MainWindow", "Записаться"))
        self.label_18.setText(_translate("MainWindow", "10:00 - 11:00"))
        self.textBrowser_18.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">ABS</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Большой зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Альбина</span></p></body></html>"))
        self.sb_2.setText(_translate("MainWindow", "Записаться"))
        self.label_20.setText(_translate("MainWindow", "08:00 - 09:00"))
        self.textBrowser_20.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">STRETCHING</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Малый зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Карина</span></p></body></html>"))
        self.vs_1.setText(_translate("MainWindow", "Записаться"))
        self.label_21.setText(_translate("MainWindow", "18:00 - 19:00"))
        self.textBrowser_21.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">PILATES</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Малый зал</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Тренер: Альбина</span></p></body></html>"))
        self.vs_2.setText(_translate("MainWindow", "Записаться"))
        self.label_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">ФитПресс</span></p></body></html>"))
        self.label_month.setWhatsThis(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">May</span></p></body></html>"))
        self.label_month.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">MAY</span><br/></p></body></html>"))
