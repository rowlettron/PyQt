# HelloWorld.py

"""Simple Hello World example with PyQt6."""

import sys

# 1.  Import QApplication and all required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# 2.  Create an instance of QApplication
app = QApplication([])

# 3.  Create GUI for application
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60,30)

# 4.  Show the applications GUI
window.show()

# 5.  Run the applications event loop
sys.exit(app.exec())


