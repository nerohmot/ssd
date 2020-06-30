# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:53:44 2020

@author: hoeren
"""

import importlib
import os
import platform
import re
import sys
import qdarkstyle
import qtawesome as qta

from PyQt5 import QtCore, QtWidgets, uic, QtGui
from zeroconf import ServiceBrowser, Zeroconf

from client.discover import SpyderListener
from client.toolbar import ToolBar


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

    # get the appropriate .ui file and load it.
        my_ui = __file__.replace('.py', '.ui')
        if not os.path.exists(my_ui):
            raise Exception("'%s' doesn't exist" % my_ui)
        uic.loadUi(my_ui, self)

    # Initialize the main window
        # ToDo: Reenable this, if we figure that we *really* want SpyderMock to be in front of our debugger
        # all the time.
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle(' '.join(re.findall('.[^A-Z]*', os.path.basename(__file__).replace('.py', ''))))

    # setup zeroconf & listener
        self.zeroconf = Zeroconf()
        self.spyderListener = SpyderListener()

    # setup the toolbar
        self.toolbar = ToolBar(self)
        self.addToolBar(self.toolbar)

    # go
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = MainWindow()

    res = app.exec_()

    sys.exit(res)
