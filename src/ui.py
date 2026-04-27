# Imports
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QPlainTextEdit, QSizePolicy, QDoubleSpinBox
from PyQt6.QtCore import Qt

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

        self.percent_label = QLabel("Enter your reprocessing percentage below:")

        layout.addWidget(self.percent_label)
        layout.addWidget(self.percent)
        layout.addWidget(self.input)
        layout.addWidget(submit)


    def calc(self):
        input_text = self.input.toPlainText()
        percentage_input = self.percent.value()
        print(input_text)

  