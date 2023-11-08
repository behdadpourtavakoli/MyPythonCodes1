from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class FramelessWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Create custom title bar
        self.title_bar = QWidget(self)
        self.title_bar.setGeometry(0, 0, 400, 30)
        self.title_bar.setStyleSheet('background-color: #303030;')

        # Add title label
        self.title_label = QLabel('My Frameless Window', self.title_bar)
        self.title_label.move(10, 5)
        self.title_label.setStyleSheet('color: white;')

        # Add close button
        self.close_button = QPushButton('X', self.title_bar)
        self.close_button.setGeometry(370, 5, 20, 20)
        self.close_button.setStyleSheet('background-color: none; color: white; border: none;')
        self.close_button.clicked.connect(self.close)

        # Add content
        self.content = QLabel('Codeloop', self)
        self.content.move(50, 50)

        self.setGeometry(300, 300, 400, 200)

    def paintEvent(self, event):
        # Draw custom border
        painter = QPainter(self)
        painter.setPen(QColor(0, 0, 0, 0))
        painter.setBrush(QColor(255, 255, 255, 50))
        painter.drawRoundedRect(0, 0, self.width() - 1, self.height() - 1, 10, 10)


if __name__ == '__main__':
    app = QApplication([])
    win = FramelessWindow()
    win.show()
    app.exec_()
