# PyQt5 text area
# pythonprogramminglanguage.com

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit, QLabel, QPushButton, QApplication
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
import logging
import Feature_extraction as fe


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

        # Add Button tokenize title
        self.tokenize_title = QPushButton('tokenize title', self)
        self.tokenize_title.setToolTip('Tokenize the title')
        self.tokenize_title.clicked.connect(self.token_title)
        self.tokenize_title.move(600,40)

        # Add Button find keywords
        self.find_keywords = QPushButton('find keywords', self)
        self.find_keywords.setToolTip('find 20 keywords from content')
        self.find_keywords.clicked.connect(self.find_keyword)
        self.find_keywords.move(600,70)

        #Add Logger
        self.logger = QPlainTextEdit(self)
        self.logger.setReadOnly(True)
        self.logger.move(530,150)
        self.logger.resize(200,300)


        self.show()



    def find_keyword(self):
        self.logger.setPlainText('')
        keyword_dict = fe.find_content_keyword(self.Content_text.toPlainText())
        print(keyword_dict)
        self.logger.appendPlainText(str(keyword_dict))
    
    def token_title(self):
        self.logger.setPlainText('')
        title_dict = fe.find_title_keyword(self.title_text.toPlainText())
        print(title_dict)
        self.logger.appendPlainText(str(title_dict))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit( app.exec_() )
