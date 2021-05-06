# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCheckBox2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(475, 344)
        Dialog.setStyleSheet("background-color:rgb(255, 170, 255)")
        self.groupBoxIceCream = QtWidgets.QGroupBox(Dialog)
        self.groupBoxIceCream.setGeometry(QtCore.QRect(30, 120, 181, 131))
        self.groupBoxIceCream.setObjectName("groupBoxIceCream")
        self.checkBoxRocky = QtWidgets.QCheckBox(self.groupBoxIceCream)
        self.checkBoxRocky.setGeometry(QtCore.QRect(10, 110, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxRocky.setFont(font)
        self.checkBoxRocky.setObjectName("checkBoxRocky")
        self.checkBoxChocAlmond = QtWidgets.QCheckBox(self.groupBoxIceCream)
        self.checkBoxChocAlmond.setGeometry(QtCore.QRect(10, 80, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxChocAlmond.setFont(font)
        self.checkBoxChocAlmond.setObjectName("checkBoxChocAlmond")
        self.checkBoxCookie = QtWidgets.QCheckBox(self.groupBoxIceCream)
        self.checkBoxCookie.setGeometry(QtCore.QRect(10, 50, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxCookie.setFont(font)
        self.checkBoxCookie.setObjectName("checkBoxCookie")
        self.checkBoxMintChoc = QtWidgets.QCheckBox(self.groupBoxIceCream)
        self.checkBoxMintChoc.setGeometry(QtCore.QRect(10, 20, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxMintChoc.setFont(font)
        self.checkBoxMintChoc.setObjectName("checkBoxMintChoc")
        self.groupBoxDrink = QtWidgets.QGroupBox(Dialog)
        self.groupBoxDrink.setGeometry(QtCore.QRect(280, 120, 161, 131))
        self.groupBoxDrink.setObjectName("groupBoxDrink")
        self.checkBoxSoda = QtWidgets.QCheckBox(self.groupBoxDrink)
        self.checkBoxSoda.setGeometry(QtCore.QRect(10, 50, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxSoda.setFont(font)
        self.checkBoxSoda.setObjectName("checkBoxSoda")
        self.checkBoxCoffee = QtWidgets.QCheckBox(self.groupBoxDrink)
        self.checkBoxCoffee.setGeometry(QtCore.QRect(10, 20, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxCoffee.setFont(font)
        self.checkBoxCoffee.setObjectName("checkBoxCoffee")
        self.checkBoxMilkshake = QtWidgets.QCheckBox(self.groupBoxDrink)
        self.checkBoxMilkshake.setGeometry(QtCore.QRect(10, 80, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxMilkshake.setFont(font)
        self.checkBoxMilkshake.setObjectName("checkBoxMilkshake")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(290, 90, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(50, 290, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelAmount.setFont(font)
        self.labelAmount.setText("")
        self.labelAmount.setObjectName("labelAmount")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBoxIceCream.setTitle(_translate("Dialog", "Ice Creams"))
        self.checkBoxRocky.setText(_translate("Dialog", "Rocky Road - R40"))
        self.checkBoxChocAlmond.setText(_translate("Dialog", "Chocolate Almond - R30"))
        self.checkBoxCookie.setText(_translate("Dialog", "Cookie Dough - R25"))
        self.checkBoxMintChoc.setText(_translate("Dialog", "Mint Chocolate Chip - R15"))
        self.groupBoxDrink.setTitle(_translate("Dialog", "Drinks"))
        self.checkBoxSoda.setText(_translate("Dialog", "Soda - R15"))
        self.checkBoxCoffee.setText(_translate("Dialog", "Coffee - R10"))
        self.checkBoxMilkshake.setText(_translate("Dialog", "Milkshake - R25"))
        self.label.setText(_translate("Dialog", "MENU"))
        self.label_2.setText(_translate("Dialog", "Select your Ice Cream: "))
        self.label_3.setText(_translate("Dialog", "Select your drink: "))
