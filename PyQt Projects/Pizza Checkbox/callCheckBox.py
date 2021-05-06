import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoCheckBox1 import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.checkBoxCheese.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxBacon.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxRibs.stateChanged.connect(self.dispAmount)
        self.show()

    def dispAmount(self):
        amount = 80
        if self.ui.checkBoxCheese.isChecked():
            amount += 5
        if self.ui.checkBoxBacon.isChecked():
            amount += 10
        if self.ui.checkBoxRibs.isChecked():
            amount += 15
        self.ui.labelAmount.setText("The total cost for your pizza is R" + str(amount))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
