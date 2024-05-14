import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
#from PyQt5 import uic
from RPN import is_digit, calculate
from ui_fcalc import Ui_MainWindow


class Calc(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #uic.loadUi('fcalc.ui', self)
        self.le_focus = self.le_func
        self.initUI()

    def initUI(self):
        #цвет на кнопках установил
        self.btn_eq.setStyleSheet("background-color: orange")
        self.btn_del.setStyleSheet("background-color: #1560BD")
        self.btn_ac.setStyleSheet("background-color: #1560BD")

        app.focusChanged.connect(self.focus)

        self.btn_eq.clicked.connect(self.run)

        self.le_func.returnPressed.connect(self.run)
        self.le_x.returnPressed.connect(self.run)

        self.btn_del.clicked.connect(self.delete)

        self.btn_ac.clicked.connect(self.clear)

        self.btn_0.clicked.connect(self.input)
        self.btn_1.clicked.connect(self.input)
        self.btn_2.clicked.connect(self.input)
        self.btn_3.clicked.connect(self.input)
        self.btn_4.clicked.connect(self.input)
        self.btn_5.clicked.connect(self.input)
        self.btn_6.clicked.connect(self.input)
        self.btn_7.clicked.connect(self.input)
        self.btn_8.clicked.connect(self.input)
        self.btn_9.clicked.connect(self.input)
        self.btn_sin.clicked.connect(self.input)
        self.btn_cos.clicked.connect(self.input)
        self.btn_tg.clicked.connect(self.input)
        self.btn_ctg.clicked.connect(self.input)
        self.btn_asin.clicked.connect(self.input)
        self.btn_acos.clicked.connect(self.input)
        self.btn_atg.clicked.connect(self.input)
        self.btn_actg.clicked.connect(self.input)
        self.btn_br1.clicked.connect(self.input)
        self.btn_br2.clicked.connect(self.input)
        self.btn_log2.clicked.connect(self.input)
        self.btn_ex.clicked.connect(self.input)
        self.btn_lg.clicked.connect(self.input)
        self.btn_mult.clicked.connect(self.input)
        self.btn_div.clicked.connect(self.input)
        self.btn_ln.clicked.connect(self.input)
        self.btn_plus.clicked.connect(self.input)
        self.btn_minus.clicked.connect(self.input)
        self.btn_pi.clicked.connect(self.input)
        self.btn_e.clicked.connect(self.input)
        self.btn_point.clicked.connect(self.input)
        self.btn_sqrt.clicked.connect(self.input)
        self.btn_x.clicked.connect(self.input)

    def focus(self):
        if self.le_x.hasFocus():
            self.le_focus = self.le_x
        elif self.le_func.hasFocus():
            self.le_focus = self.le_func

    def delete(self):
        ind = self.le_focus.cursorPosition()
        if ind > 0:
            ind -= 1
            self.le_focus.setText(self.le_focus.text()[:ind] + self.le_focus.text()[ind+1:])
        self.le_focus.setCursorPosition(ind)
        self.le_focus.setFocus()

    def clear(self):
        self.le_func.clear()
        self.le_x.clear()
        self.lbl_result.clear()
        self.le_func.setFocus()

    def input(self):
        ind = self.le_focus.cursorPosition()
        new_text = self.sender().text()
        self.le_focus.setText(self.le_focus.text()[:ind] + new_text + self.le_focus.text()[ind:])
        self.le_focus.setCursorPosition(ind + len(new_text))
        self.le_focus.setFocus()

    def run(self):
        string = self.le_func.text()
        if "x" in string:
            x = self.le_x.text()
            if "x" in x:
                result = "error"
            else:
                if not is_digit(x):
                    x = calculate(x)
                    if not is_digit(str(x)):
                        result = "error"
                    else:
                        result = calculate(string, x)
                else:
                    result = calculate(string, float(x))
        else:
            result = calculate(string)
        self.lbl_result.setText(str(result)+" ")
        self.le_func.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calc()
    calc.show()
    sys.exit(app.exec())




