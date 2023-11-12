#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os
import datetime
import inspect
import csv
import codecs
import pymssql
from PyQt5 import QtGui, QtCore, Qt
#import mainwindow
#import _winreg only on Microsoft platforms
import platform
winos = True

if os.name == 'nt' and platform.system() == 'Windows':
    import _winreg
    #other stuff needed under Windows
    import _mssql
    import decimal
    import uuid
    winos = True
else:
    winos = False

#other global variables
liccode = False
closemain = False

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        super(MainWindow, self).__init__(parent)
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        # some stuff and widgets to visualize in the main window

        #connettors to menù functions; leave only the closing one
        self.ui.actionChiudi.triggered.connect(self.close)

    #override of closeEvent - there I think, it's better to work to separate
    #closeEvent for mainwindow from general closeEvent. But how?
    def closeEvent(self, event):
        global closemain
        #make evaluation test to decide how to work. Close directly or no?
        if self.csvViewer.rowCount() > 0 and not closemain:
            #print event
            #show a warning
            Error = QtGui.QMessageBox()
            Error.setIcon(QtGui.QMessageBox.Question)
            Error.setWindowTitle('WARNING !!')
            Error.setInformativeText(u"Are you sure to leave?")
            Error.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            ret = Error.exec_()
            if ret == QtGui.QMessageBox.Ok:
                closemain = True
                event.accept()
            else:
                event.ignore()
        else:
            #close directly
            event.accept()

#start application and create main
app = QtGui.QApplication(sys.argv)
my_mainWindow = MainWindow()
my_mainWindow.show()
sys.exit(app.exec_())
