import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoRadioButton2 import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonM.toggled.connect(self.dispSelected)
        self.ui.radioButtonL.toggled.connect(self.dispSelected)
        self.ui.radioButtonXL.toggled.connect(self.dispSelected)
        self.ui.radioButtonXXL.toggled.connect(self.dispSelected)
        self.ui.radioButtonDebitCard.toggled.connect(self.dispSelected)
        self.ui.radioButtonBanking.toggled.connect(self.dispSelected)
        self.ui.radioButtonCod.toggled.connect(self.dispSelected)
        self.show()

    def dispSelected(self):
        selected1 = ""
        selected2 = ""
        if self.ui.radioButtonM.isChecked():
            selected1 = "Medium"
        if self.ui.radioButtonL.isChecked():
            selected1 = "Large"
        if self.ui.radioButtonXL.isChecked():
            selected1 = "X-Large"
        if self.ui.radioButtonXXL.isChecked():
            selected1 = "XX-Large"
        if self.ui.radioButtonDebitCard.isChecked():
            selected2 = "Debit/Credit Card"
        if self.ui.radioButtonBanking.isChecked():
            selected2 = "NetBanking"
        if self.ui.radioButtonCod.isChecked():
            selected2 = "Cash On Delivery"
        self.ui.labelSelected.setText("Chosen shirt size is " + selected1 + " and payment method is " + selected2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
