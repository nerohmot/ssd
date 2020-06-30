# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:18:33 2020

@author: hoeren
"""

import qtawesome as qta

from PyQt5 import QtWidgets, QtCore


class ToolBar(QtWidgets.QToolBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.setMovable(False)
        self.parent = parent
        self.active_host = ''

        host_label = QtWidgets.QLabel("Host:")
        host_label.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.addWidget(host_label)

        self.host_combo = QtWidgets.QComboBox()
        self.hosts = self.parent.spyderListener.get_hosts()

        # self.host_combo.addItems([''] + self.testers.report())
        # self.host_combo.setCurrentText('')
        width = self.host_combo.minimumSizeHint().width()
        self.host_combo.setMinimumWidth(width)
        self.addWidget(self.host_combo)

        self.refresh_testers = QtWidgets.QAction(qta.icon('mdi.refresh', color='orange'), "Refresh Testers", self)
        self.refresh_testers.setStatusTip("Refresh the tester list")
        self.refresh_testers.setCheckable(False)
        self.addAction(self.refresh_testers)

        self.run_action = QtWidgets.QAction(qta.icon('mdi.play-circle-outline', color='orange'), "Run", self)
        self.run_action.setStatusTip("Run active module")
        self.run_action.setCheckable(False)
        self.addAction(self.run_action)

    def get_host_dict(self):
        return self.parent.spyderListener.get_hosts()

    def get_host_list(self):
        """This method obtains the most recent list of Spyder Hosts."""




    @QtCore.pyqtSlot(str)
    def _tester_changed(self, selected_tester):
        self.active_tester = selected_tester

    def on_run(self):
        print("run button pressed")

    def info_pressed(self):
        print("info button pressed")

    def setting_pressed(self):
        pass

