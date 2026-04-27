# Imports
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QPlainTextEdit, QSizePolicy, QDoubleSpinBox
from PyQt6.QtCore import Qt
from ores import *
from popups import*

class MainWindow(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        layout = QGridLayout()
        self.setLayout(layout)
        self.input = QPlainTextEdit()
        self.input.setProperty("class", "text-input")

        submit = QPushButton("Submit")
        submit.clicked.connect(self.calc)
        submit.setProperty("class", "submit-btn")

        self.percent = QDoubleSpinBox()
        self.percent.setRange(0.0, 100.0)
        self.percent.setSingleStep(0.01)
        self.percent.setSuffix("%")
        self.percent.setFixedWidth(100)




        layout.addWidget(self.percent)
        layout.addWidget(self.input)
        layout.addWidget(submit)


    def calc(self):
        input_text = self.input.toPlainText()
        percentage_input = self.percent.value()

        if input_text not in ORES:
            not_found(self,input_text)



        print(input_text)

  