import sys
import requests
import PyQt5
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtWidgets
from algorithms import Kmp, Mode, BoyerMoore, RabinKarp, Naive, Parser

TYPE = {"rabin_karp": RabinKarp.rabin_karp,
        "boyer_moore": BoyerMoore.boyer_moore,
        "naive": Naive.naive,
        "kmp": Kmp.kmp
        }
TYPES_MODE = {"memory_check": Mode.memory_check,
              "time_check": Mode.time_check
              }


def web_parser(link: str) -> str:
    """Функция, получающая на вход ссылку и возвращающая текст"""
    r = requests.get(link)
    r = r.text
    return r


class Ui(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.pushButton = None
        self.textEdit_2 = None
        self.textEdit = None
        self.comboBox = None
        self.comboBox_2 = None
        uic.loadUi('form.ui', self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.show()

    def on_pushButton_clicked(self):
        string, pattern, algo, mode, type_string = \
            self.textEdit_2.toPlainText(),\
            self.textEdit.toPlainText(), \
            self.comboBox.currentText(), \
            self.comboBox_2.currentText(), \
            self.comboBox_3.currentText()

        if type_string == 'Web Page':
            string = web_parser(string)
        pars = Parser(string, pattern)
        if mode == 'None':
            print(TYPE[algo](pars))
            exit()
        else:
            print(TYPES_MODE[mode](pars, TYPE[algo]))
            exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
