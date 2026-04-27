# Imports
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QPlainTextEdit, QSizePolicy
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        layout = QGridLayout()

        layout.setContentsMargins(100, 100, 100, 100)
        self.setLayout(layout)
        self.input = QPlainTextEdit()
        self.input.setFixedWidth(500)
        self.input.setFixedHeight(300)
        self.input.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)



        submit = QPushButton("Submit")
        submit.clicked.connect(self.calc)

        layout.addWidget(self.input, 1,1, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(submit, 2,1, Qt.AlignmentFlag.AlignCenter)

    def calc(self):
        input_text = self.input.toPlainText()
        print(input_text)

  