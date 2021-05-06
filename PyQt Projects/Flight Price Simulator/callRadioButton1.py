import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoRadioButton1 import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonFirstClass.toggled.connect(self.dispFare)
        self.ui.radioButtonBusinessClass.toggled.connect(self.dispFare)
        self.ui.radioButtonEconomyClass.toggled.connect(self.dispFare)
        self.show()

    def dispFare(self):
        fare = 0
        if self.ui.radioButtonFirstClass.isChecked():
            fare = 12000
        if self.ui.radioButtonBusinessClass.isChecked():
            fare = 8000
        if self.ui.radioButtonEconomyClass.isChecked():
            fare = 5000
        self.ui.labelFare.setText("Your ticket cost is R" + str(fare))


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
