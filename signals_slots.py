# signal_slots.copy()

"""Signals and slots example"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget
)

def greet():
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText("Hello, World!!!")


app = QApplication([])
window = QWidget()
window.setWindowTitle("Signals and Slots")
layout = QVBoxLayout()

