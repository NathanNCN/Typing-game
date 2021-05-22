from input_box import Inputbox
from text_widget import Textbox
from sentences import sentences
from score_window import Score
from PyQt5.QtWidgets import QMainWindow
import time
import random
from time import time


class Game(QMainWindow):
    def __init__(self,parent=None):
        super(Game, self).__init__(parent)
        self._WPM_info = Score()
        self.text = random.choice(sentences).split()
        self.i = 0
        self.error = 0
        self.initUI()
        self.time= None


    def initUI(self):
        self.setGeometry(600, 200, 500, 300)
        self.setWindowTitle('Typing game')

        self.input_box = Inputbox(self)
        self.input_box.move(150,225)
        self.input_box.returnPressed.connect(self.test)


        self.text_box = Textbox(self)
        self.text_box.move(20,30)

    def test(self):
        if self.typed_words == len(self.text):
            self.find_WPM(time())
            self._WPM_info.show()
        elif self.input_box.text()==self.text_box.text():
            self.text_box.setText(self.text[self.typed_words])
            self.typed_words+=1
            if self.typed_words==1:
                self.time=time()
        else:
            self.error+=1

    def find_WPM(self,end_time):
        self.time=end_time-self.time
        self._WPM_info.WPM = 10


