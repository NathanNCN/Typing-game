from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PyQt5.QtGui import *
import sys
class Inputbox(QMainWindow):
    def __init__(self):
        super(Inputbox,self).__init__()
        self.initUI()


    def initUI(self):
        self.input = QtWidgets.QLineEdit(self)
        self.input.resize(200, 50)
        self.input.move(155, 200)
        self.input.returnPressed.connect(self.test)


        self.word = QtWidgets.QLineEdit(self)
        self.word.resize(300, 150)
        self.word.move(105, 30)
        self.word.setDisabled(True)
        self.word.setFont(QFont('Times', 40))
        self.word.setText('Bread')



    def test(self):
        print('test')




