# main.py
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import QSize, Qt, QObject, QThread, pyqtSignal
import example as ex

class Worker(QObject):
    finished = pyqtSignal()

    def run(self):
        for recognized_text, response in ex.recognition():
            self.recognized.emit(recognized_text, response)

class TextWorker(QObject):
    finished = pyqtSignal(str)

    def __init__(self, text):
        super().__init__()
        self.text = text

    def run(self):
        output = ex.execute_command(self.text)
        self.finished.emit(output)

class VoiceWorker(QObject):
    recognized = pyqtSignal(str, str)
    stop_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._is_running = True
        self.stop_signal.connect(self.stop)

    def run(self):
        for recognized_text, response in ex.recognition():
            if not self._is_running:
                break
            self.recognized.emit(recognized_text, response)

    def stop(self):
        self._is_running = False


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
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
        self.user_input_line_edit.setFixedSize(325, 50)
        self.user_input_line_edit.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.dialog_text_browser, 0, 0, 2, 4)
        layout.addWidget(self.button, 2, 3, 1, 1)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        if hasattr(self, 'voice_thread') and self.voice_thread.isRunning():
            self.voice_worker.stop_signal.emit()
            self.voice_thread.quit()
            self.voice_thread.wait()

        self.voice_thread = QThread()
        self.voice_worker = VoiceWorker()
        self.voice_worker.moveToThread(self.voice_thread)
        self.voice_thread.started.connect(self.voice_worker.run)
        self.voice_worker.recognized.connect(self.update_text_browser_voice)
        self.voice_thread.finished.connect(self.voice_worker.deleteLater)
        self.voice_thread.finished.connect(self.voice_thread.deleteLater)
        self.voice_thread.start()

    def update_text_browser_voice(self, recognized_text, output):
        self.dialog_text_browser.append("<p style='text-align: right; color: #acb78e; font-size: 15px;'>{}</p>".format(recognized_text))
        self.dialog_text_browser.append("<p style='text-align: left; color: #6b8e23; font-size: 20px;'>{}</p>".format(output))

    def text_inputed(self):
        
        user_text = self.user_input_line_edit.text()
        self.user_input_line_edit.clear()

        self.text_thread = QThread()
        self.text_worker = TextWorker(user_text)
        self.text_worker.moveToThread(self.text_thread)
        self.text_thread.started.connect(self.text_worker.run)
        self.text_worker.finished.connect(self.text_thread.quit)
        self.text_worker.finished.connect(self.text_worker.deleteLater)
        self.text_worker.finished.connect(lambda output: self.update_text_browser(output, user_text))
        self.text_thread.finished.connect(self.text_thread.deleteLater)
        self.text_thread.start()

    def update_text_browser(self, output, user_text):
        self.dialog_text_browser.append("<p style='text-align: right; color: #acb78e; font-size: 15px;'>{}</p>".format(user_text))
        self.dialog_text_browser.append("<p style='text-align: left; color: #6b8e23; font-size: 20px;'>{}</p>".format(output))
        


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()