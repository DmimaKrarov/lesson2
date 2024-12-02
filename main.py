import random

from PyQt6 import uic
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6.QtGui import QPainter, QColor

import io
import sys

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>300</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="yellow_button">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>110</y>
      <width>101</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>нарисовать круг</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>300</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.do_paint = False
        self.setGeometry(300, 300, 300, 300)
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
        painter.setPen(QColor(255, 255, 0))
        size = random.randint(0, 50)
        painter.drawEllipse(QPoint(random.randint(50, 250), random.randint(50, 250)), size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())