from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PyQt5.QtGui import *
from input_box import Inputbox
import sys


class HowTo(QMainWindow):
    def __init__(self):
        super(HowTo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Typing Game')

        self.title = QtWidgets.QLabel(self)
        self.title.move(120, 50)
        self.title.setFont(QFont('Times', 12))
        self.title.setText('Typing game How to play')
        self.title.adjustSize()

        self.text = QtWidgets.QLabel(self)
        self.text.move(40, 80)
        self.text.setFont(QFont('Times', 9))
        self.text.setText('There will be word that pop up on the GUI. You will need'
                          '\n to type the word out and submit the word. If the word is '
                          '\n not excatly like the one on screen you will not be able '
                          '\nto move on to the next word. The faster you type the word '
                          '\nthe more points you get. goal of the game is to be as quick as '
                          '\npossible and try to get the most amount of points possible')
        self.text.adjustSize()

class Game(QtWidgets.QWidget):
    def __init__(self):
        super(Game, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 200, 500, 300)
        self.setWindowTitle('Typing game')

        self.input_box = Inputbox()
        self.input_box.move(30,30)







class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.howto_ = HowTo()
        self.gamewindow_ = Game()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Typing Game')

        self.title = QtWidgets.QLabel(self)
        self.title.move(150, 50)
        self.title.setFont(QFont('Times', 12))
        self.title.setText('Typing game')

        self.rules = QtWidgets.QPushButton(self)
        self.rules.resize(150, 50)
        self.rules.setText('How to play')
        self.rules.move(125, 150)
        self.rules.clicked.connect(self.toggle_howto)

        self.start_game = QtWidgets.QPushButton(self)
        self.start_game.resize(150, 50)
        self.start_game.setText('Start Game')
        self.start_game.move(125, 90)
        self.start_game.clicked.connect(self.toggle_game)

    def toggle_howto(self):
        if self.howto_.isVisible():
            self.howto_.hide()
        else:
            self.rules.setText('Close window?')
            self.howto_.show()

    def toggle_game(self):
        self.gamewindow_.show()


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

