from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 359)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 691, 361))
        self.frame.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.name_text = QtWidgets.QLineEdit(self.frame)
        self.name_text.setGeometry(QtCore.QRect(150, 100, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_text.setFont(font)
        self.name_text.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255,100);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(0, 0, 0, 0.1); \n"
"}\n"
"")
        self.name_text.setText("")
        self.name_text.setMaxLength(100)
        self.name_text.setFrame(True)
        self.name_text.setCursorPosition(0)
        self.name_text.setObjectName("name_text")
        self.telef_text = QtWidgets.QLineEdit(self.frame)
        self.telef_text.setGeometry(QtCore.QRect(150, 200, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.telef_text.setFont(font)
        self.telef_text.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255,100);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(0, 0, 0, 0.1); \n"
"}\n"
"")
        self.telef_text.setText("")
        self.telef_text.setMaxLength(12)
        self.telef_text.setCursorPosition(0)
        self.telef_text.setObjectName("telef_text")
        self.label_registr = QtWidgets.QLabel(self.frame)
        self.label_registr.setGeometry(QtCore.QRect(260, 30, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_registr.setFont(font)
        self.label_registr.setStyleSheet("")
        self.label_registr.setObjectName("label_registr")
        self.send = QtWidgets.QPushButton(self.frame)
        self.send.setGeometry(QtCore.QRect(290, 300, 131, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.send.setFont(font)
        self.send.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.send.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,50);\n"
"border: 1px solid  rgb(255, 255, 255,50) ;\n"
"border-radius: 10px;\n"
"color:white\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(62, 166, 240);\n"
"}")
        self.send.setIconSize(QtCore.QSize(30, 30))
        self.send.setFlat(True)
        self.send.setObjectName("send")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name_text.setPlaceholderText(_translate("MainWindow", "Введите Ф.И.О.."))
        self.telef_text.setPlaceholderText(_translate("MainWindow", "Ввведите номер тел.."))
        self.label_registr.setText(_translate("MainWindow", "РЕГИСТРАЦИЯ"))
        self.send.setText(_translate("MainWindow", "ОТПРАВИТЬ"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    RegistOkno = Ui_MainWindow()
    RegistOkno.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())