# PyQt5 text area
# pythonprogramminglanguage.com

import sys
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
from PyQt5.QtCore import QSize

class ExampleWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(670, 470))    
        self.setWindowTitle("Article View Predictor") 

        # Add text field
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("Title \n")
        self.b.move(10,10)
        self.b.resize(200,50)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit( app.exec_() )