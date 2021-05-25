from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PyQt5.QtGui import *
import sys
class Textbox(QtWidgets.QLineEdit):
    def __init__(self,parent=None):
        super(Textbox,self).__init__(parent)
        self.parent=parent
        self.initUI()


    def initUI(self):
        self.resize(450, 150)
        self.setDisabled(True)
        self.setFont(QFont('Times', 15))
        self.setText('Start')



