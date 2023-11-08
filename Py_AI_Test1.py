'''
///*-=============================================================================================-*
/// Dateiname             : Py_AI_Test1.py (Artificial Intelligence Test by Python)
/// Version               : 1.0.0.0
/// Beginn                : 2023-11-07 (1402/08/16)
/// Letzte Aktualisierung : 2023-11-07 (1402/08/16)
/// Autor                 : Ingenieur Behdad Pourtavakoli
/// Warenzeichen          : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------
/// Copyright© 1380-1402,2001-2023 von B.S.D Group™
/// Alle Rechte vorbehalten.
/// ----------------------------------------------------------------------------------------------
///
/// Beschreibung: Überprüfen und lernen Sie die Python-Programmierung auf den Websites 
///               docs.python.org, www.geeksforgeeks.org und www.w3schools.com
///
///-=============================================================================================-*///
'''

import os, sys, numpy
from PyQt5 import QtCore
from PyQt5 import QtGui
from scipy import *
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

#region Konstanten, Variablen und Deklarationen
'''
///*********************************************************************************************************
///* Konstanten, Variablen und Deklarationen                                                               *
///*********************************************************************************************************
'''

#endregion

#region MyApp Class
'''
///*********************************************************************************************************
///* MyApp Class                                                                                           *
///*********************************************************************************************************
'''

#endregion

#region Handschriftliche Funktionen und Prozeduren
'''
/// *********************************************************************************************************
/// * Handschriftliche Funktionen und Prozeduren                                                            *
/// *********************************************************************************************************
'''

'''
/// about_EN() funktion zur Anzeige von Programminformationen, Versionsnummer und Urheberrecht als Deutsch
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
/// 
'''
def about_DE():
     os.system('cls')
     print("Behdad Software Developers Group™ praesentiert\n")
     
     print("Willkommen bei B.S.D Group™ Produktion\n")
     
     print("Urheberrecht© 1380-1402,2001-2023 von B.S.D Group™")
     print("Alle Rechte vorbehalten.\n")
     
     print("Entwurf und Entwicklung durch Ingenieur Behdad Pourtavakoli\n")
     
     print("®MyFirstPy2.py - B.S.D Group™")
     print("docs.python.org, www.geeksforgeeks.org, www.w3schools.com sind Lehrer...\n")

'''
/// ai_Func_S1()-Funktion zum Ausführen und Testen der nützlichsten Basisfunktionen der künstlichen Intelligenz
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
/// 
'''
def ai_Func_S1():
    speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
    age = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

    print("Dataset: ", speed, "\n")

    x = numpy.mean(speed)
    print("Mean function: ", x, " //* to find the average speed *")

    x = numpy.median(speed)
    print("Median function: ", x, " //* to find the middle value *")
     
    x = stats.mode(speed)
    print("Mode function: ", x, " //* to find the number that appears the most *")
     
    x = numpy.std(speed)
    print("Std function: ", x, " //* to find the standard deviation *")
     
    x = numpy.var(speed)
    print("Var function: ", x, " //* to find the variance *")

    x = numpy.percentile(age, 75)
    print("Percentile function: ", x, " //* to find the percentiles *")

    x = numpy.percentile(age, 90)
    print("Percentile function: ", x, " //* What is the age that 90% of the people are younger than? *")

    print("\n")

'''
/// ai_Func_S2()-Funktion zur Datenverteilung der Künstlichen Intelligenz
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
/// 
'''
def ai_Func_S2():
    x = numpy.random.uniform(0.00, 1.00, 100)
    print("Uniform function: //* Create an array containing 250 random floats between 0 and 5 *\n", x)

    #print("\n")
#endregion

#region Standardfunktionen und -verfahren
'''
///*********************************************************************************************************
///* Standardfunktionen und -verfahren                                                                     *
///*********************************************************************************************************
'''

'''
/// dialog() funktion zur 
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/17
/// 
'''
def dialog():
    mbox = QMessageBox()

    mbox.setText("Your allegiance has been noted")
    mbox.setDetailedText("You are now a disciple and subject of the all-knowing Guru")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #mbox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    mbox.exec_()

'''
/// mainWindow() funktion zur 
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/17
/// 
'''
def mainWindow():
    class MyApp(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            #qWin = QWidget()
            self.setWindowTitle("Artificial Intelligence Test by Python")
            self.setWindowIcon(QtGui.QIcon("Images/Python3.png"))
            width = 850
            height = 500
            self.resize(width, height)
            self.setFixedSize(width, height)
            self.center()


            # Stop here to decide a decision to add text editor and paste A.I function output in 1402/08/18 by Engineer Behdad Pourtavakoli
            label = QLabel(self)
            label.setText("Behold the Guru, Guru99")
            label.move(100, 130)
            label.show()

            btn = QPushButton(self)
            btn.setText('Beheld')
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.move(110, 150)
            btn.show()
            btn.clicked.connect(dialog)

            btn1 = QPushButton("Athos")
            btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn2 = QPushButton("Porthos")
            btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn3 = QPushButton("Aramis")
            btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

            hbox = QHBoxLayout(self)

            hbox.addWidget(btn1)
            hbox.addWidget(btn2)
            hbox.addWidget(btn3)

            self.show()

        def center(self):
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())

    if (__name__ == "__main__"):
        #qApp = QApplication([])
        qApp = QApplication(sys.argv)

        ex = MyApp()
        sys.exit(qApp.exec_())

    ### Subclass QMainWindow to customize your application's main window
    ##class MainWindow(QMainWindow):
    ##    def __init__(self):
    ##        super().__init__()

    ##        self.setWindowTitle("Artificial Intelligence Test by Python")
    ##        self.setFixedSize(QSize(800, 600))

    ##        button = QPushButton("Click")

    ##        # Set the central widget of the Window.
    ##        self.setCentralWidget(button)

    ##app = QApplication(sys.argv)

    ##window = MainWindow()
    ##window.show()

    ##app.exec()

    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.
    #qApp = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    #qWindow = QMainWindow() #QPushButton("Push Me") #QWidget()
    #qWindow.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    #qApp.exec()

#endregion

#region Hauptprogramm
'''
/// Hauptprogramm, enthält Hauptanweisungen und Aufruffunktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
/// 
'''

mainWindow()

about_DE()
ai_Func_S1()
ai_Func_S2()

print("\nEnde des Programms...", end = "")
#endregion
