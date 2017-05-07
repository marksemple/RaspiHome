#
""" RaspiHome -- a basic home-console application to show weather etc"""

import sys

from PyQt5.QtCore import (Qt,)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QStackedWidget, QFormLayout, QSplitter,
                             QPushButton)

import resources
from weatherModule import weatherWidget


class RaspiHome(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.weather = weatherWidget(parent=self)
        self.defineLayout()
        resources.setStyleSheet(self, './StyleSheet.txt')
        self.setWindowFlags(Qt.FramelessWindowHint)

    def defineLayout(self):
        self.menuWidge = menuWidge = QWidget()
        self.moduleWidge = moduleWidge = QStackedWidget()

        self.weatherBttn = QPushButton("Weather")
        self.closeBttn = QPushButton("Exit")

        self.weatherBttn.clicked.connect(lambda: print("weather"))
        self.closeBttn.clicked.connect(self.close)

        formlayout = QFormLayout()
        menuWidge.setLayout(formlayout)
        formlayout.addRow(self.weatherBttn)
        formlayout.addRow(self.closeBttn)

        moduleWidge.addWidget(self.weather)

        splitter = QSplitter()
        splitter.addWidget(menuWidge)
        splitter.addWidget(moduleWidge)

        self.setCentralWidget(splitter)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    home = RaspiHome()
    home.showFullScreen()
    app.exec_()
