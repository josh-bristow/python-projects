import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoLineEdit import *


class MyForm(QDialog):  # Create MyForm class that inherits from QDialog
    def __init__(self):  # Default Constructor
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ButtonClickMe.clicked.connect(self.dispmessage)  # When button is clicked, dispmessage is called
        self.show()

    def dispmessage(self):
        self.ui.labelResponse.setText("Hello " + self.ui.lineEditName.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
