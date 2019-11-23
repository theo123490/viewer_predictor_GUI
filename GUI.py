# PyQt5 text area
# pythonprogramminglanguage.com

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit, QLabel, QPushButton, QApplication
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
import logging


class ExampleWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        super().__init__()

        
        self.title = 'Article View Predictor'
        self.left = 40
        self.top = 40
        self.width = 800
        self.height = 900
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #add title label
        self.title_label = QLabel(self)
        self.title_label.setText('Title')
        self.title_label.move(10,10)
        self.title_label.setFont(QFont('Arial', 20))

        # Add title text area
        self.title_text = QPlainTextEdit(self)
        self.title_text.move(10,50)
        self.title_text.resize(500,50)
        
        #add Content label
        self.Content_label = QLabel(self)
        self.Content_label.setText('Content')
        self.Content_label.move(10,110)
        self.Content_label.setFont(QFont('Arial', 20))

        # Add Content text area
        self.Content_text = QPlainTextEdit(self)
        self.Content_text.move(10,150)
        self.Content_text.resize(500,400)

        # output title label
        self.output_title_label = QLabel(self)
        self.output_title_label.setText('Output :')
        self.output_title_label.move(530,130)
        self.output_title_label.setFont(QFont('Arial', 12))
        self.output_title_label.adjustSize()
        self.output_title_label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # Add Button
        self.button = QPushButton('find keywords', self)
        self.button.setToolTip('This is an example button')
        self.button.clicked.connect(self.on_click)
        self.button.move(600,70)

        #Add Logger
        self.logger = QPlainTextEdit(self)
        self.logger.setReadOnly(True)
        self.logger.move(530,150)
        self.logger.resize(200,300)







        self.show()



    def on_click(self):
        print(self.title_text.toPlainText())
        self.logger.appendPlainText(self.title_text.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit( app.exec_() )
