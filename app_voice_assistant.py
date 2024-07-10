from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import QSize, Qt
import sys # Только для доступа к аргументам командной строки

# Приложению нужен один (и только один) экземпляр QApplication.
# Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
# Если не будете использовать аргументы командной строки, QApplication([]) тоже работает
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(800, 700))
        self.setWindowTitle("Голосовой помощник")
        self.setMinimumSize(100, 100)
        self.setMaximumSize(1200,800)

        self.text_input = QtWidgets.QLineEdit()
        self.text_output = QtWidgets.QTextEdit()
        self.button = QtWidgets.QPushButton('Голос')


        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.text_input,  1, 0)
        layout.addWidget(self.text_output, 0, 0, 1, 2)
        layout.addWidget(self.button, 1, 1)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.button.clicked.connect(self.on_button_clicked)
        self.text_input.returnPressed.connect(self.text_inputed)
        #Кнопка
    def on_button_clicked(self):
        print('Нажата кнопка')
        #здесь должна быть функция запуска ввода голоса
    def text_inputed(self):
        print('Введен текст')
        #Здесь должна быть функция для ввода текста


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()
