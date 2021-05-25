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
        self.clicked.connect(self.open_typing_game)

    def open_typing_game(self):
        self.parent.open_game()

class Rules(QtWidgets.QPushButton):
    def __init__(self,parent=None):
        super(Rules,self).__init__(parent)
        self.parent=parent
        self.initUI()

    def initUI(self):
        self.resize(150, 50)
        self.setText('How to play')
        self.clicked.connect(self.open_how_to)

    def open_how_to(self):
        self.parent.open_how_to_play()
