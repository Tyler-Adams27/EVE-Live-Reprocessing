# Imports
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QSizePolicy
from ui import MainWindow
from css import global_style
import sys

width = 800
height = 600

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(global_style)
    window = MainWindow("EVE Repro")
    window.show()
    window.setBaseSize(width, height)
    sys.exit(app.exec())




print("Hello, world!")