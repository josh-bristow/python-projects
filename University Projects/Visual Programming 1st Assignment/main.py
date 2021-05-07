import re
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from windowApp import *

class Durban(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonEmail.clicked.connect(self.subscribed)
        self.ui.radioButtonCoastlands.toggled.connect(self.disp_amount_coastlands)
        self.ui.radioButtonPearls.toggled.connect(self.disp_amount_pearls)
        self.ui.radioButtonRoyal.toggled.connect(self.disp_amount_royal)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1000)
        self.showlcd()
        self.show()

    def subscribed(self):
        if len(self.ui.lineEditEmail.text()) != 0 and valid_email(self.ui.lineEditEmail.text()):
            subscribe_message = self.ui.lineEditEmail.text() + "\nhas been subscribed!"
        else:
            subscribe_message = "You have not entered a valid email!"
        self.ui.labelEmail.setText(subscribe_message)

    def disp_amount_coastlands(self):
        if len(self.ui.lineEditHotels.text()) != 0:
            total_amount_coastlands = float(self.ui.lineEditHotels.text()) * 750
        else:
            total_amount_coastlands = 0
        self.ui.lineEditHotelTotal.setText(str(total_amount_coastlands))

    def disp_amount_pearls(self):
        if len(self.ui.lineEditHotels.text()) != 0:
            total_amount_pearls = float(self.ui.lineEditHotels.text()) * 1050
        else:
            total_amount_pearls = 0
        self.ui.lineEditHotelTotal.setText(str(total_amount_pearls))

    def disp_amount_royal(self):
        if len(self.ui.lineEditHotels.text()) != 0:
            total_amount_royal = float(self.ui.lineEditHotels.text()) * 1200
        else:
            total_amount_royal = 0
        self.ui.lineEditHotelTotal.setText(str(total_amount_royal))

    def showlcd(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm')
        self.ui.lcdNumber.display(text)


regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def valid_email(email):
    if re.search(regex, email):
        return True
    else:
        return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Durban()
    w.show()
    sys.exit(app.exec_())
