import sys
import PyQt5
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtWidgets
from algorithms import Kmp, Mode, BoyerMoore, RabinKarp, Naive, Parser
from web_parser import WebParser

TYPE = {"rabin_karp": RabinKarp,
        "boyer_moore": BoyerMoore,
        "naive": Naive,
        "kmp": Kmp
        }

TYPES_MODE = {"memory_check": Mode.memory_check,
              "time_check": Mode.time_check
              }


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
        url, pattern, algorithm, mode, type_string = \
            self.textEdit_2.toPlainText(),\
            self.textEdit.toPlainText(), \
            self.comboBox.currentText(), \
            self.comboBox_2.currentText(), \
            self.comboBox_3.currentText()

        if type_string == 'Web Page':
            page_text = WebParser(url).get_page_text()
        else:
            page_text = url

        algorithm_object = TYPE[algorithm](page_text, pattern)
        if mode == 'None':
            print(algorithm_object.search_method())
            exit()
        else:
            if mode == 'time_check':
                print(TYPES_MODE[mode](algorithm_object))
            else:
                TYPES_MODE[mode](algorithm_object)
            exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
