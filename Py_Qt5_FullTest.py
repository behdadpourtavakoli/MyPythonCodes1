## # Example 3 - PyQt5 – How to stop resizing of window | setFixedSize() method
## # importing the required libraries
## from PyQt5.QtCore import *
## from PyQt5.QtGui import *
## from PyQt5.QtWidgets import *
## import sys
## 
## class Window(QMainWindow):
## 	def __init__(self):
## 		super().__init__()
## 
## 		# set the title
## 		self.setWindowTitle("Python")
## 
## 		width = 500
## 		height = 400
## 		# setting the fixed size of window
## 		self.setFixedSize(width, height)
## 
## 		# creating a label widget
## 		self.label_1 = QLabel("Fixed size window", self)
## 
## 		# moving position
## 		self.label_1.move(100, 100)
## 
## 		# setting up the border
## 		self.label_1.setStyleSheet("border :3px solid black;")
## 
## 		# resizing label
## 		self.label_1.resize(120, 80)
## 
## 		# show all the widgets
## 		self.show()
## 
## 
## # create pyqt5 app
## App = QApplication(sys.argv)
## 
## # create the instance of our Window
## window = Window()
## 
## # start the app
## sys.exit(App.exec())
## exit(0)

# Example 2 - Example window center
import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QtGui.QIcon("Images/Python3.png"))
        self.setWindowTitle("PyQt5 customized window...")
        width = 540
        height = 540
        #self.setStyleSheet("background-color: transparent;")
        self.resize(width, height)
        self.setFixedSize(width, height)
        self.center()

        # creating label
        #self.label = QLabel(self)
        self.label = QLabel(self) 
        
        # loading image
        self.pixmap = QPixmap("Images/Panda1.png")
        
        # adding image to label
        self.label.setPixmap(self.pixmap)
        #self.label.setWindowOpacity(0.5) 

        # Optional, resize label to image size
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        self.label.adjustSize()
        self.label.setGeometry(10, 5, width, height)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

exit(0)


# Example 1 - PyQt5 - Hello World
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(100,100,200,50)
    app.center

    #intWidth = 200 # Width
    #intHeight = 50 # Height
    #screen_width = app.winfo_screenwidth()  # Width of the screen
    #screen_height = app.winfo_screenheight() # Height of the screen
    ## Calculate Starting X and Y coordinates for Window
    #inyPosX = (screen_width / 2) - (intWidth / 2)
    #intPosY = (screen_height / 2) - (intHeight / 2)
    #w.geometry("%dx%d+%d+%d" % (intWidth, intHeight, inyPosX, intPosY))
   
    b.move(50,20)
    w.setWindowTitle("PyQt5")
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
   window()
