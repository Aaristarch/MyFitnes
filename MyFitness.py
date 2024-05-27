import subprocess
import interface
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, QTimer
import psutil
import sys


class MyProject(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Фиксируем размер виджета
        self.setFixedSize(self.size())

        # Создание таймера для обновления отображения времени
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

        self.pushButton_20.clicked.connect(self.monday)
        self.pushButton_21.clicked.connect(self.tuesday)
        self.pushButton_22.clicked.connect(self.wednesday)
        self.pushButton_23.clicked.connect(self.thursday)
        self.pushButton_24.clicked.connect(self.friday)
        self.pushButton_25.clicked.connect(self.saturday)
        self.pushButton_26.clicked.connect(self.sunday)

        self.pn_1.clicked.connect(self. available)
        self.pn_2.clicked.connect(self.available)
        self.pn_3.clicked.connect(self.no_entry)

        self.vt_1.clicked.connect(self.no_entry)
        self.vt_2.clicked.connect(self.available)
        self.vt_3.clicked.connect(self.available)

        self.sr_1.clicked.connect(self.no_entry)
        self.sr_2.clicked.connect(self.no_entry)

        self.cht_1.clicked.connect(self.available)
        self.cht_2.clicked.connect(self.available)
        self.cht_3.clicked.connect(self.available)

        self.pt_1.clicked.connect(self.available)
        self.pt_2.clicked.connect(self.no_entry)
        self.pt_3.clicked.connect(self.no_entry)

        self.sb_1.clicked.connect(self.no_entry)
        self.sb_2.clicked.connect(self.no_entry)

        self.vs_1.clicked.connect(self.available)
        self.vs_2.clicked.connect(self.no_entry)

    def update(self):
        """ Этот метод обновляет метку self.time текущим временем
        в формате "чч:мм" и вызывает метод self.charging().
        Метод _time вызывается каждый раз, когда истекает
        таймер, созданный в предыдущем фрагменте кода """

        self.time.setText((QDateTime.currentDateTime().toString("hh:mm")))
        self.charging()

    def charging(self):
        """ Этот метод обновляет отображение уровня заряда батареи """

        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            self.label_charging.setText(f"{percent}%")

    def monday(self):
        ''' Этот метод отображает страницу расписания занятий пн '''

        self.stackedWidget.setCurrentIndex(0)

    def tuesday(self):
        ''' Этот метод отображает страницу расписания занятий вт '''

        self.stackedWidget.setCurrentIndex(1)

    def wednesday(self):
        ''' Этот метод отображает страницу расписания занятий ср '''

        self.stackedWidget.setCurrentIndex(2)

    def thursday(self):
        ''' Этот метод отображает страницу расписания занятий чт '''

        self.stackedWidget.setCurrentIndex(3)

    def friday(self):
        ''' Этот метод отображает страницу расписания занятий пт '''

        self.stackedWidget.setCurrentIndex(4)

    def saturday(self):
        ''' Этот метод отображает страницу расписания занятий сб '''

        self.stackedWidget.setCurrentIndex(5)

    def sunday(self):
        ''' Этот метод отображает страницу расписания занятий вс '''

        self.stackedWidget.setCurrentIndex(6)

    def available(self):
        ''' Этот метод открывает модуль regist.py'''

        subprocess.Popen(["python", "regist.py"])

    def no_entry(self):
        ''' Этот метод открывает модуль regist_over.py'''

        subprocess.Popen(["python", "regist_over.py"])

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    FITNESS = MyProject()
    FITNESS.show()
    sys.exit(app.exec_())
