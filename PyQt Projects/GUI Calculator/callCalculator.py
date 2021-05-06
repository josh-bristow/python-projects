import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoCalculator import *


class myCalc(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonPlus.clicked.connect(self.addtwonum)
        self.ui.pushButtonSubtract.clicked.connect(self.subtracttwonum)
        self.ui.pushButtonMultiply.clicked.connect(self.multiplytwonum)
        self.ui.pushButtonDivide.clicked.connect(self.dividetwonum)
        self.show()

    def addtwonum(self):
        if len(self.ui.lineEditFirst.text()) != 0:
            a = int(self.ui.lineEditFirst.text())
        else:
            a = 0
        if len(self.ui.lineEditSecond.text()) != 0:
            b = int(self.ui.lineEditSecond.text())
        else:
            b = 0
        add_sum = a + b
        self.ui.labelResult.setText("Addition: " + str(add_sum))

    def subtracttwonum(self):
        if len(self.ui.lineEditFirst.text()) != 0:
            a = int(self.ui.lineEditFirst.text())
        else:
            a = 0
        if len(self.ui.lineEditSecond.text()) != 0:
            b = int(self.ui.lineEditSecond.text())
        else:
            b = 0
        diff = a - b
        self.ui.labelResult.setText("Subtraction: " + str(diff))

    def multiplytwonum(self):
        if len(self.ui.lineEditFirst.text()) != 0:
            a = int(self.ui.lineEditFirst.text())
        else:
            a = 0
        if len(self.ui.lineEditSecond.text()) != 0:
            b = int(self.ui.lineEditSecond.text())
        else:
            b = 0
        multiply = a * b
        self.ui.labelResult.setText("Mutliplication: " + str(multiply))

    def dividetwonum(self):
        if len(self.ui.lineEditFirst.text()) != 0:
            a = int(self.ui.lineEditFirst.text())
        else:
            a = 0
        if len(self.ui.lineEditSecond.text()) != 0:
            b = int(self.ui.lineEditSecond.text())
        else:
            b = 1
        division = a / b
        self.ui.labelResult.setText("Division: " + str(division))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myCalc()
    w.show()
    sys.exit(app.exec_())
