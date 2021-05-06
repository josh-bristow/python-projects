import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoCheckBox2 import *


class MyMenu(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.checkBoxChocAlmond.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxCookie.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxMintChoc.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxRocky.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxCoffee.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxSoda.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxMilkshake.stateChanged.connect(self.dispAmount)
        self.show()

    def dispAmount(self):
        amount = 0
        if self.ui.checkBoxChocAlmond.isChecked():
            amount += 30
        if self.ui.checkBoxMintChoc.isChecked():
            amount += 15
        if self.ui.checkBoxRocky.isChecked():
            amount += 40
        if self.ui.checkBoxCookie.isChecked():
            amount += 25
        if self.ui.checkBoxCoffee.isChecked():
            amount += 10
        if self.ui.checkBoxSoda.isChecked():
            amount += 15
        if self.ui.checkBoxMilkshake.isChecked():
            amount += 25
        self.ui.labelAmount.setText("Your total is R" + str(amount))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyMenu()
    w.show()
    sys.exit(app.exec_())
