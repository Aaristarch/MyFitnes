import subprocess
import sys
from PyQt5.QtWidgets import QMessageBox
import okno_regist
from PyQt5 import QtWidgets


class REGIST(QtWidgets.QMainWindow, okno_regist.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Фиксируем размер виджета
        self.setFixedSize(self.size())
        self.send.clicked.connect(self.send_regist)

    def send_regist(self):
        name = self.name_text.text()
        phone = self.telef_text.text()

        # Проверка на пустые поля
        if not name or not phone:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля.")
            return

            # Проверка имени на корректность (только буквы)
        if not name.isalpha():
            QMessageBox.warning(self, "Ошибка", "Введите корректное имя (только буквы).")
            return

        # Проверка телефонного номера на цифры
        if not phone.isdigit():
            QMessageBox.warning(self, "Ошибка", "Введите корректный номер телефона.")
            return

        # Если данные верны, открываем файл
        subprocess.Popen(["python", "regist_completed.py"])


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    recording = REGIST()
    recording.show()
    sys.exit(app.exec_())