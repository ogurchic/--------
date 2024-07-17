# main.py
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import QSize, Qt, QObject, QThread, pyqtSignal

# Зачем импортировать Sys???
import sys  # Только для доступа к аргументам командной строки
import example as ex

class Worker(QObject):
    finished = pyqtSignal()

    def run(self):
        ex.recognition()
        self.finished.emit()

# Приложению нужен один (и только один) экземпляр QApplication.
# Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
# Если не будете использовать аргументы командной строки, QApplication([]) тоже работает
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #Нужно будет получить доступ к разрешению экрана пользователя и ввести зависимости размеров от него
        self.setFixedSize(QSize(400, 600))
        self.setWindowTitle("Голосовой помощник")
        
        self.dialog_text_browser = QtWidgets.QTextBrowser()
        self.user_input_line_edit = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton()
        self.button.setFixedSize(50, 50)
        self.button.setIconSize(QSize(50, 50))
        self.button.setIcon(QtGui.QIcon('button_icon.png'))  #Нужно вставить путь к кнопке

        self.user_input_line_edit.returnPressed.connect(self.text_inputed)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.user_input_line_edit, 2, 0, 1, 3)
        self.user_input_line_edit.setFixedSize(400, 50)
        self.user_input_line_edit.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.dialog_text_browser, 0, 0, 2, 4)
        layout.addWidget(self.button, 2, 3, 1, 1)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.button.clicked.connect(self.on_button_clicked)


    def on_button_clicked(self):
        # здесь должна быть функция запуска ввода голоса
        # worker = Worker(ex.recognition)
        # QThreadPool.globalInstance().start(worker)
        #threading.Thread(target=ex.recognition).start()
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()


    def text_inputed(self):
        user_text = self.user_input_line_edit.text()
        self.user_input_line_edit.clear()
        # Здесь должна быть функция для обработки введенного текста
        output = ex.execute_command(user_text)
        print(user_text)
        print(output)

        self.dialog_text_browser.append("<p style='text-align: left; color: blue;'>{}</p>".format(user_text))
        self.dialog_text_browser.append("<p style='text-align: right; color: red;'>{}</p>".format(output))
        #Пока что есть проблемы с выравниванием текста, потому что остаётся выравнивание из предыдущей строки

app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()