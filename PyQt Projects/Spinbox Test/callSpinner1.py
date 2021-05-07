import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoSpinner1 import *


class BookStore(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.spinBoxBookQty.editingFinished.connect(self.result_book)
        self.ui.doubleSpinBoxPaperLength.editingFinished.connect(self.result_paper)
        self.show()

    def result_book(self):
        if len(self.ui.lineEditBookPrice.text()) != 0:
            book_price = int(self.ui.lineEditBookPrice.text())
        else:
            book_price = 0
        total_book_amount = self.ui.spinBoxBookQty.value() * book_price
        self.ui.lineEditBookAmount.setText(str(total_book_amount))

    def result_paper(self):
        if len(self.ui.lineEditPaperPrice.text()) != 0:
            paper_price = int(self.ui.lineEditPaperPrice.text())
        else:
            paper_price = 0
        total_paper_amount = self.ui.doubleSpinBoxPaperLength.value() * paper_price
        self.ui.lineEditPaperAmount.setText(str(total_paper_amount))
        total_book_amount = int(self.ui.lineEditBookAmount.text())
        total_amount = total_book_amount + total_paper_amount
        self.ui.labelTotalAmount.setText(str(total_amount))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = BookStore()
    w.show()
    sys.exit(app.exec_())
