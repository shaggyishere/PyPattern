# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bdrba\Documents\QTDesign\formSalvataggiSoloNomeMatrice.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(362, 160)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 120, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_2.setObjectName("label_2")
        self.nameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.nameLineEdit.setGeometry(QtCore.QRect(10, 50, 341, 20))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.tagLineEdit = QtWidgets.QLineEdit(Dialog)
        self.tagLineEdit.setGeometry(QtCore.QRect(10, 90, 341, 20))
        self.tagLineEdit.setObjectName("tagLineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Salva"))
        self.label_2.setText(_translate("Dialog", "Nome"))
        self.label_3.setText(_translate("Dialog", "Tag"))
