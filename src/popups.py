from PyQt6.QtWidgets import QMessageBox

def not_found(window, ore):
    msg = QMessageBox(window)
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle("Unknown Ore")
    msg.setText(f"{ore} not found!")
    msg.setInformativeText("Please check the spelling and try again.")
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg.exec()
