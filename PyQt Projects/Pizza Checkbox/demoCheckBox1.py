# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCheckBox1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(442, 343)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(40, 290, 261, 31))
        self.labelAmount.setText("")
        self.labelAmount.setObjectName("labelAmount")
        self.checkBoxCheese = QtWidgets.QCheckBox(Dialog)
        self.checkBoxCheese.setGeometry(QtCore.QRect(190, 100, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxCheese.setFont(font)
        self.checkBoxCheese.setObjectName("checkBoxCheese")
        self.checkBoxBacon = QtWidgets.QCheckBox(Dialog)
        self.checkBoxBacon.setGeometry(QtCore.QRect(190, 130, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxBacon.setFont(font)
        self.checkBoxBacon.setObjectName("checkBoxBacon")
        self.checkBoxRibs = QtWidgets.QCheckBox(Dialog)
        self.checkBoxRibs.setGeometry(QtCore.QRect(190, 160, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxRibs.setFont(font)
        self.checkBoxRibs.setObjectName("checkBoxRibs")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Large Pizza - R80"))
        self.label_2.setText(_translate("Dialog", "Select your extra toppings: "))
        self.checkBoxCheese.setText(_translate("Dialog", "Cheese - R5"))
        self.checkBoxBacon.setText(_translate("Dialog", "Bacon - R10"))
        self.checkBoxRibs.setText(_translate("Dialog", "BBQ Ribs - R15"))
