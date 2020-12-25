from MainUi import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QCursor, QMovie
# from PyQt5.QtCore import Qt
from PyQt5.QtCore import Qt
import sys
import os
import resource_rc


class Main(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗体无边框
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # 设置背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.m_flag = False

        self.m_Position = 0
        self.setupUi(self)
        if os.path.exists("gif.gif"):
            self.gif = QMovie("gif.gif")
        else:
            self.gif = QMovie(":/gif/Christmas.gif")
        self.giflabel.setMovie(self.gif)
        self.giflabel.setScaledContents(True)
        self.gif.start()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Main()
    w.show()
    sys.exit(app.exec_())
