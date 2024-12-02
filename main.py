import random

from PyQt6 import uic
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt6.QtGui import QPainter, QColor

import io
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 300, 300)

        self.yellow_button = QPushButton(self)
        self.yellow_button.setText('нарисовать круг')
        self.yellow_button.setGeometry(150, 150, 100, 35)
        self.yellow_button.clicked.connect(self.run)

    def run(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter(self)
            painter.begin(self)
            self.draw_sirc(painter)

    def draw_sirc(self, painter):
        painter.setPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        size = random.randint(0, 50)
        painter.drawEllipse(QPoint(random.randint(50, 250), random.randint(50, 250)), size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())