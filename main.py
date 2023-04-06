import sys
import PyQt5
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtWidgets
from algorithms import SearchAlgo, Mode

TYPES_ALGO = {"kmp": SearchAlgo.kmp,
              "boyer_moore": SearchAlgo.boyer_moore,
              "rabin_karp": SearchAlgo.rabin_karp,
              "naive": SearchAlgo.naive,
              }
TYPES_MODE = {"memory_check": Mode.memory_check, "time_check": Mode.time_check}


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
        string, pattern, algo, mode = \
            self.textEdit_2.toPlainText(),\
            self.textEdit.toPlainText(), \
            self.comboBox.currentText(), \
            self.comboBox_2.currentText()
        if mode == 'None':
            print(TYPES_ALGO[algo](string, pattern))
            exit()
        else:
            print(TYPES_MODE[mode](string, pattern, TYPES_ALGO[algo]))
            exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
