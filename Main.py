from How_to_play import HowTo
from typing_game import Game
from button_widgets import Play_game,Rules
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PyQt5.QtGui import *
import time
import random
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self._howto = HowTo()
        self._gamewindow = Game()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Typing Game')

        self.title = QtWidgets.QLabel(self)
        self.title.move(150, 50)
        self.title.setFont(QFont('Times', 12))
        self.title.setText('Typing game')

        self.rules = Rules(self)
        self.rules.move(125, 150)
        self.rules.clicked.connect(self.toggle_howto)

        self.start_game = Play_game(self)
        self.start_game.move(125, 90)
        self.start_game.clicked.connect(self.toggle_game)

    def toggle_howto(self):
        if self._howto.isVisible():
            self._howto.hide()
        else:
            self.rules.setText('Close window?')
            self._howto.show()

    def toggle_game(self):
        self._gamewindow.show()



def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

main()
