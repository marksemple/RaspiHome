#
""" """

import sys

from PyQt5.QtWidgets import QApplication, QPushButton


if __name__ == "__main__":

    app = QApplication(sys.argv)
    button = QPushButton("TestButton")
    button.setFixedSize(150, 150)
    button.show()
    app.exec_()
