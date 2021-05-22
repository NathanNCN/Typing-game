from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PyQt5.QtGui import *
from input_box import Inputbox
from text_widget import Textbox
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