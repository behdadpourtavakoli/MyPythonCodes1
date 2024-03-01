#region Copyright
'''
///*-==================================================================================================-*
/// Dateiname             : Py_AI_Test1.py (Artificial Intelligence Test by Python)
/// Version               : 1.0.0.0
/// Beginn                : 2023-11-07 (1402/08/16)
/// Letzte Aktualisierung : 2023-11-10 (1402/08/19)
/// Autor                 : Ingenieur Behdad Pourtavakoli
/// Warenzeichen          : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------------
/// Copyright© 1380-1402,2001-2024 von B.S.D Group™
/// Alle Rechte vorbehalten.
/// ----------------------------------------------------------------------------------------------------
///
/// Beschreibung: Überprüfen und lernen Sie die Python-Programmierung auf den Websites 
///               docs.python.org, www.geeksforgeeks.org und www.w3schools.com, www.w3resource.com,
///               stackoverflow.com, pythonbasics.org, doc-snapshots.qt.io, www.pythonguis.com,
///               copyprogramming.com, www.pythonguis.com, python-forum.io, superfastpython.com,
///               codeloop.org, python-course.eu
///-===================================================================================================-*///
'''
#endregion

#region Important header files
'''
///*********************************************************************************************************
///* Important header files                                                                                *
///*********************************************************************************************************
'''
import os, numpy, sys
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from numpy.random.mtrand import _rand
#from scipy import *
from scipy import stats
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
#endregion

#region Konstanten, Variablen und Deklarationen
'''
///*********************************************************************************************************
///* Konstanten, Variablen und Deklarationen                                                               *
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
'''
def about_DE():
    os.system('cls')
    print("Behdad Software Developers Group™ praesentiert\n")

    print("Willkommen bei B.S.D Group™ Produktion\n")

    print("Urheberrecht© 1380-1402,2001-2024 von B.S.D Group™")
    print("Alle Rechte vorbehalten.\n")

    print("Entwurf und Entwicklung durch Ingenieur Behdad Pourtavakoli\n")

    print("®Py_AI_Test1.py - B.S.D Group™")
    print("Überprüfen und lernen Sie die Python-Programmierung auf den Websites")
    print(" docs.python.org, www.geeksforgeeks.org und www.w3schools.com, www.w3resource.com,")
    print(" stackoverflow.com, pythonbasics.org, doc-snapshots.qt.io, www.pythonguis.com,")
    print(" copyprogramming.com, www.pythonguis.com, python-forum.io, superfastpython.com,")
    print(" codeloop.org, python-course.eu sind Lehrer...\n")

'''
/// mainWindow() funktion zur 
/// MyApp() class to 
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/17
'''
def mainWindow():
    class MyApp(QWidget):
        def __init__(self):
            super().__init__()
            self.initGUI()

        def initGUI(self):
            #qWin = QWidget()
            self.setWindowTitle("Artificial Intelligence Test by Python")
            self.setWindowIcon(QtGui.QIcon("Images/Python3.png"))
            width = 850
            height = 500
            self.resize(width, height)
            self.setFixedSize(width, height)
            self.center()

            # Create first TextEdit where we will enter a number.
            txtTextEdit1 = QTextEdit(self)
            txtTextEdit1.setGeometry(5, 25, 840, 435)
            txtTextEdit1.setReadOnly(True)

            # Stop here to decide a decision to add text editor and paste A.I function output in 1402/08/18 by Engineer Behdad Pourtavakoli
            strTemp = prepareData()
            txtTextEdit1.setText(strTemp)

            lblTitle = QLabel(self)
            lblTitle.setText("Artificial Intelligence Machine Learning functions by Python")
            lblTitle.move(5, 5)

            btnAbout = QPushButton(self)
            btnAbout.setText('About...')
            btnAbout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btnAbout.move(5, 470)
            btnAbout.clicked.connect(dlgAbout)

            btnPlot = QPushButton(self)
            btnPlot.setText('Plot')
            btnPlot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btnPlot.move(85, 470)
            btnPlot.clicked.connect(dlgPlot)

            btnRefresh = QPushButton(self)
            btnRefresh.setText('Refresh')
            btnRefresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btnRefresh.move(165, 470)
            btnRefresh.clicked.connect(dlgRefresh)

            btnExit = QPushButton(self)
            btnExit.setText('Exit')
            btnExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btnExit.move(245, 470)
            btnExit.clicked.connect(dlgExit)

            lblTitle.show()
            btnAbout.show()
            btnExit.show()

            self.show()

        def center(self):
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())

        '''
        /// closeEvent() Funktion wird ausgeführt, wenn das Hauptformular geschlossen werden möchte.
        /// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/19
        '''
        def closeEvent(self, event):
            qMBox = QMessageBox()
            qMBox.setWindowIcon(QtGui.QIcon("Images/Python3.png"))
            qMBox.setWindowTitle("Exit request")
            qMBox.setText("Do you want to exit?")
            qMBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            qMBox.setDetailedText("You are trying to close app and exit.")
            qMBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            qMBoxResult = qMBox.exec()

            # Ask for confirmation before closing
            #confirmation = QMessageBox.question(self, "Exit request", "Do you want to exit?", QMessageBox.Yes | QMessageBox.No)

            if (qMBoxResult == QMessageBox.Ok):
                event.accept()  # Close the app
            else:
                event.ignore()  # Don't close the app

    if (__name__ == "__main__"):
        qApp = QApplication([])
        ex = MyApp()
        ex.show()
        qApp.exec_()
        #sys.exit(qApp.exec_())
        #print(ex, "\n", x)
        sysEOP()

'''
/// PrepareData()-Funktion zum Ausführen und Testen der nützlichsten Basisfunktionen der künstlichen Intelligenz
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/18
/// www.w3schools.com/python/numpy/default.asp ist Lehrer...
///  - Machine Learning - Mean Median Mode
///  - 
///  - 
///  - 
///  - 
///  - 
///  - 
'''
def prepareData():
    speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
    age = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
    myArr = [1, 2, 3, 4, 5]

    strTemp = ""
    strTemp = "Dataset: " + str(speed) + "\n\n"

    x = numpy.mean(speed)
    strTemp += "Mean function: " + str(x) + "\t //* to find the average speed *\n"

    x = numpy.median(speed)
    strTemp += "Median function: " + str(x) + "\t\t //* to find the middle value *\n"

    x = stats.mode(speed)
    strTemp += "Mode function: " + str(x) + "\t //* to find the number that appears the most *\n"

    x = numpy.std(speed)
    strTemp += "Std function: " + str(x) + "\t //* to find the standard deviation *\n\n"

    x = numpy.var(speed)
    strTemp += "Var function: " + str(x) + "\t //* to find the variance *\n\n"

    strTemp += "Ageset: " + str(age) + "\n\n"

    x = numpy.percentile(age, 75)
    strTemp += "Percentile function: " + str(x) + "\t\t //* to find the percentiles *\n"

    x = numpy.percentile(age, 90)
    strTemp += "Percentile function: " + str(x) + "\t\t //* What is the age that 90% of the people are younger than? *\n\n"

    #matplotlib.use('Agg')

    x = numpy.random.uniform(0.00, 1.00, 100)
    strTemp += "Uniform function: \t\t//* Create an array containing 100 random floats between 0 and 1 *\n" + str(x) + "\n\n"
    #plt.hist(x, 5)
    #plt.show()

    x = numpy.random.uniform(0.00, 5.0, 250)
    strTemp += "Uniform function: \t\t//* Create an array containing 250 random floats between 0 and 5 *\n" + str(x) + "\n\n"
    #plt.hist(x, 5)
    #plt.show()

    x = np.array(myArr)
    strTemp += "NumPy array: " + str(x) + " - " + str(type(x)) + "\n"
    x = np.array(age)
    strTemp += "NumPy array: " + str(x) + " - " + str(type(age)) + "\n"
    x = np.array(speed)
    strTemp += "NumPy array: " + str(x) + " - " + str(type(speed)) + "\n\n"



    return(strTemp)

'''
/// dlgAbout() funktion zur 
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/18
'''
def dlgAbout():
    frmAbout2 = Tk()

    frmAbout2.title("About...")
    frmAbout2.resizable(False, False)
    frmAbout2.iconphoto(False, PhotoImage(file="Images/Python3.png"))

    intWidth = 450 # Width
    intHeight = 240 # Height

    screen_width = frmAbout2.winfo_screenwidth()  # Width of the screen
    screen_height = frmAbout2.winfo_screenheight() # Height of the screen

    # Calculate Starting X and Y coordinates for Window
    inyPosX = (screen_width / 2) - (intWidth / 2)
    intPosY = (screen_height / 2) - (intHeight / 2)

    frmAbout2.attributes('-topmost', True)
    frmAbout2.geometry("%dx%d+%d+%d" % (intWidth, intHeight, inyPosX, intPosY))

    strTitle =  "Behdad Software Developers Group™ Presents\n\n"
    strTitle += "Welcome to the B.S.D Group™ Production\n\n"
    strTitle += "Copyright© 1380-1402,2001-2024 by B.S.D Group™\n"
    strTitle += "All rights reserved.\n\n"
    strTitle += "Design and develop by Engineer Behdad Pourtavakoli\n\n"
    strTitle += "®Py_AI_Test1.py (Python Project) - B.S.D Group™\n"

    lblTitle1 = Label(frmAbout2, text = strTitle).pack(pady = 15)

    cmdButton1 = Button(frmAbout2, text = "OK", command = frmAbout2.destroy, cursor="hand2", height=1, width=10)
    cmdButton1.focus_set()
    cmdButton1.pack()

    frmFrame1 = Frame(frmAbout2)
    frmFrame1.place(x=10, y=10)

    # Load and display an image 
    imageX = Image.open("Images/Python3.png")
    img_resized = imageX.resize((50, 50)) # new width & height
    imageX = ImageTk.PhotoImage(img_resized)

    # Create a label to display the image
    image_label = Label(frmFrame1, image=imageX).pack()

    frmAbout2.mainloop()

'''
/// dlgExit() funktion zur 
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/17
'''
def dlgExit():
    qMBox = QMessageBox()
    qMBox.setWindowIcon(QtGui.QIcon("Images/Python3.png"))
    qMBox.setWindowTitle("Exit request")
    qMBox.setText("Do you want to exit?")
    qMBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    qMBox.setDetailedText("You are trying to close app and exit.")
    qMBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    qMBoxResult = qMBox.exec()
    if (qMBoxResult == QMessageBox.Ok):
        sysEOP()

'''
/// dlgPlot() funktion zur 
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/19
'''
def dlgPlot():
    try:
        x = numpy.random.uniform(0.00, 1.00, 100)
        plt.cla()
        plt.clf()
        plt.hist(x, 5)
        plt.show()

        x = numpy.random.uniform(0.00, 5.0, 250)
        plt.cla()
        plt.clf()
        plt.hist(x, 5)
        plt.show()
    except:
        print("Something wrong.")
    #else:
    #    print(xT1)
    #    print(xT2)

'''
/// dlgRefresh() funktion zur 
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/20
'''
def dlgRefresh():
    #strTemp = prepareData()
    #global txtTextEdit1
    #txtTextEdit1.setText(strTemp)    
    return()

#endregion

#region Standardfunktionen und -verfahren
'''
///*********************************************************************************************************
///* Standardfunktionen und -verfahren                                                                     *
///*********************************************************************************************************
'''

'''
/// sysEOP() funktion um die Anwendung zu schließen und etwas zu tun.
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/19
'''
def sysEOP():
    about_DE()
    print("\nEnde des Programms...", end = "")
    exit(0)

#endregion

#region Hauptprogramm
'''
/// Hauptprogramm, enthält Hauptanweisungen und Aufruffunktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/08/16
/// 
'''
mainWindow()
#endregion
