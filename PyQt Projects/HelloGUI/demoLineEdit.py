from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(355, 216)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 91, 16))
        self.label_2.setObjectName("label_2")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(60, 90, 47, 13))
        self.labelResponse.setObjectName("labelResponse")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(170, 50, 113, 20))
        self.lineEditName.setObjectName("lineEditName")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(160, 160, 75, 23))
        self.ButtonClickMe.setObjectName("ButtonClickMe")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Enter your name:"))
        self.labelResponse.setText(_translate("Dialog", "TextLabel"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))
