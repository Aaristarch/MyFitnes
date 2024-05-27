from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(444, 180)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_registr = QtWidgets.QLabel(self.centralwidget)
        self.label_registr.setGeometry(QtCore.QRect(50, 60, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_registr.setFont(font)
        self.label_registr.setStyleSheet("background-color: rgb(255, 255, 255,100);\n"
"border: 1px solid rgb(255, 255, 255,100);\n"
"border-radius: 15px")
        self.label_registr.setObjectName("label_registr")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_registr.setText(_translate("MainWindow", "РЕГИСТРАЦИЯ ПРОШЛА УСПЕШНО!"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    RegistCom = Ui_MainWindow()
    RegistCom.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())