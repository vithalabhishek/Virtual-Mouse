# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 11:29:21 2018
@author: Abhishek
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

class project(QDialog):
    def __init__(self):
        super(project,self).__init__()
        loadUi('Project.ui',self)
        self.setWindowTitle('Virtual Mouse PyQt5 GUI')
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.L.setText('Welcome :'+self.lineEdit.text())
app=QApplication(sys.argv)
widget=project()
widget.show()
sys.exit(app.exec_())
