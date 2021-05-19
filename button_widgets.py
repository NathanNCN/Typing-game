from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PyQt5.QtGui import *
class Play_game(QtWidgets.QPushButton):
    def __init__(self,parent=None):
        super(Play_game,self).__init__(parent)
        self.parent=parent
        self.initUI()


    def initUI(self):
        self.resize(150, 50)
        self.setText('Start Game')

class Rules(QtWidgets.QPushButton):
    def __init__(self,parent=None):
        super(Rules,self).__init__(parent)
        self.parent=parent
        self.initUI()


    def initUI(self):
        self.resize(150, 50)
        self.setText('How to play')