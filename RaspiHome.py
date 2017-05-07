#
""" """

import sys

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
        # style =
        resources.setStyleSheet(self, './StyleSheet.txt')

    def defineLayout(self):
        self.menuWidge = menuWidge = QWidget()
        self.moduleWidge = moduleWidge = QStackedWidget()

        formlayout = QFormLayout()
        menuWidge.setLayout(formlayout)
        formlayout.addRow(QPushButton("Weather"))

        moduleWidge.addWidget(self.weather)

        splitter = QSplitter()
        splitter.addWidget(menuWidge)
        splitter.addWidget(moduleWidge)

        self.setCentralWidget(splitter)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    home = RaspiHome()
    home.show()
    app.exec_()
