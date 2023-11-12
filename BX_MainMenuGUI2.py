import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QMainWindow, 
                                QLabel, QLineEdit, QTableWidget, QTableWidgetItem, 
                                QGridLayout, QVBoxLayout, QSizePolicy, QSpacerItem, 
                                QMessageBox,QSpinBox, QComboBox, QTableView,QStyledItemDelegate)
from PyQt5.QtCore import Qt, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont
 
import sqlite3
 
class Ui_MainMenu(QMainWindow):
    def __init__(self, parent = None):
        super(Ui_MainMenu, self).__init__(parent)
        self.setObjectName("MainMenu")
        self.resize(808, 594)
        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TitleLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Android Insomnia")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setStyleSheet("color: rgb(0, 255, 0);")
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayout.addWidget(self.TitleLabel)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Runlion")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setStyleSheet("color: rgb(255, 170, 0);")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Runlion")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("color: rgb(0, 0, 255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout.addWidget(self.textBrowser_2)
        self.OnlineButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lethal Injector")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OnlineButton.setFont(font)
        self.OnlineButton.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.OnlineButton.setObjectName("OnlineButton")
        self.verticalLayout.addWidget(self.OnlineButton)
        self.OfflineButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lethal Injector")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OfflineButton.setFont(font)
        self.OfflineButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.OfflineButton.setObjectName("OfflineButton")
        self.verticalLayout.addWidget(self.OfflineButton)
        self.SettingsButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lethal Injector")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SettingsButton.setFont(font)
        self.SettingsButton.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.SettingsButton.setObjectName("SettingsButton")
        self.verticalLayout.addWidget(self.SettingsButton)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
 
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
 
         
#----------------------------------------------------------------------------------------------------
#                                      Button Actions
#----------------------------------------------------------------------------------------------------
        #------------------------------------------
        #               Online Mode Button
        #------------------------------------------
        #When the Online Mode button is clicked -> OnlineClicked Function
        OnlineButton = self.OnlineButton
        OnlineButton.clicked.connect(self.OnlineClicked)
        #------------------------------------------
 
#----------------------------------
#       Online Mode Function
#----------------------------------
    def OnlineClicked(self):
        #Print in terminal for testing:
        print("Online Mode Engaged")
        self.close() #Close this screen
        #Run Baxter
        from BAXTER_V5 import BAXTER
        BAXTER()
#----------------------------------
 
#----------------------------------------------------------------------------------------------------
#                                      Retranslate Ui
#----------------------------------------------------------------------------------------------------
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "BAXTER Menu"))
        self.TitleLabel.setText(_translate("MainWindow", "B.A.X.T.E.R A.I System"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Runlion\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Reminders:</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Runlion\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Todo:</p></body></html>"))
        self.OnlineButton.setText(_translate("MainWindow", "Online Mode"))
        self.OfflineButton.setText(_translate("MainWindow", "Offline Mode"))
        self.SettingsButton.setText(_translate("MainWindow", "Settings"))
 
 
#----------------------------------------------------------------------------------------------------
#                                       Run this Program
#----------------------------------------------------------------------------------------------------
def main():
    app = QApplication(sys.argv)
    win = Ui_MainMenu()
    win.show()
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
#----------------------------------------------------------------------------------------------------
