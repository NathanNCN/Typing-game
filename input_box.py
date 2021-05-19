from PyQt5 import QtWidgets, QtCore
from text_widget import Textbox
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PyQt5.QtGui import *
import sys
class Inputbox(QtWidgets.QLineEdit):
    def __init__(self,parent=None):
        super(Inputbox,self).__init__(parent)
        self.parent=parent
        self.initUI()


    def initUI(self):
        self.resize(200, 50)
        self.move(155, 200)











