from PySide6.QtWidgets import QApplication
from mainWindow import mainWindow
import sys


def main():
    app = QApplication([])
    window = mainWindow()
    window.resize(640, 480)
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
