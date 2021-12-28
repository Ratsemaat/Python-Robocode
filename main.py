#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt5.QtWidgets import QApplication

sys.path.append(os.getcwd() + "/Objects")
sys.path.append(os.getcwd() + "/robotImages")
sys.path.append(os.getcwd() + "/Robots")

interface = "CLI"

if interface == "CLI":
    sys.path.append(os.getcwd() + "/CLI")
    from game import MainWindow
elif interface == "GUI":
   from window import MainWindow
   sys.path.append(os.getcwd() + "/GUI")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Python-Robocode")
    myapp = MainWindow()
    if interface=="GUI": myapp.show()
    sys.exit(app.exec_())
