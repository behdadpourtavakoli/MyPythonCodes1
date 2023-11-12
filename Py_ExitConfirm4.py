import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Close Confirmation")
        self.setGeometry(100, 100, 400, 200)  # (x, y, width, height)

    def closeEvent(self, event):
        # Ask for confirmation before closing
        confirmation = QMessageBox.question(self, "Confirmation", "Are you sure you want to close the application?", QMessageBox.Yes | QMessageBox.No)

        if confirmation == QMessageBox.Yes:
            event.accept()  # Close the app
        else:
            event.ignore()  # Don't close the app

def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
