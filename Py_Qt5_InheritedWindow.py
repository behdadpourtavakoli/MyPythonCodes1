import sys
from PyQt5 import *
from PyQt5.QtWidgets import *

class PlotWindow(QMainWindow): #Matplotlib embeded + 2 buttons

    def __init__(self, parent):
        super(QMainWindow, self).__init__(parent)
        self.width = 1000
        self.height = 540
        self.setGeometry(10, 10, self.width, self.height)

        self.show()

class DynamicPlotWindow(PlotWindow):

    def __init__(self, parent):
        super(PlotWindow, self).__init__(parent)
        self.btn = QPushButton("Test") # -> Not visible
        self.btn.resize(120,30)
        self.btn.move(600,800)

        self.show()

if (__name__ == "__main__"):
    qApp = QApplication([])
    #qApp = QApplication(sys.argv)

    ex = PlotWindow() #<- Error here 1402/08/19 (2023/11/10)
    sys.exit(qApp.exec_())
