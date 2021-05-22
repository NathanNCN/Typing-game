from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PyQt5.QtGui import *
class Score(QMainWindow):
    def __init__(self):
        super(Score,self).__init__()
        self._WPM = None
        self._accuarcy = None
        self.initUI()


    def initUI(self):
        self.setGeometry(600, 400, 300, 100)
        self.setWindowTitle('score')
        
        self.text = QtWidgets.QLabel(self)
        self.text.setFont(QFont('Times',12))
        self.text.setText(f'You scored #{str(self._WPM)}WPM.\n With a accuracy %')
        self.text.adjustSize()

