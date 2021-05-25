from How_to_play import HowTo
from typing_game import Game
from button_widgets import Play_game,Rules
from sentences import sentences
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *
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

        self.start_game = Play_game(self)
        self.start_game.move(125, 90)

    def open_how_to_play(self):
        if self._howto.isVisible():
            self._howto.hide()
        else:
            self.rules.setText('Close window?')
            self._howto.show()

    def open_game(self):
        self.start_game.setText('Play again?')
        self._gamewindow.show()
        self.rest_game()

    def rest_game(self):
        self._gamewindow.error = 0
        self._gamewindow.text = random.choice(sentences).split()
        self._gamewindow.typed_words = 0
        self._gamewindow.time = None
        self._gamewindow.input_box.setText('')
        self._gamewindow.text_box.setText('Start')
        self._gamewindow._WPM_info.hide()








def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

main()
