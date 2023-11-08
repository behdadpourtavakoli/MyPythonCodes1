import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

app = QApplication(sys.argv)

window = QMainWindow()

window.setAttribute(Qt.WA_TranslucentBackground, True)
# window.setAttribute(Qt.WA_NoSystemBackground, True)
# window.setWindowFlags(Qt.FramelessWindowHint)

label = QLabel(window)
pixmap = QPixmap('Images/Python3.png')
label.setPixmap(pixmap)
label.setGeometry(10, 10, pixmap.width(), pixmap.height())

window.label = label

window.resize(pixmap.width(),pixmap.height())

window.show()
sys.exit(app.exec_())