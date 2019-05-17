# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Incorrect_password.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Incorrectpassword(object):

    

    def setupUi(self, Incorrectpassword):
        Incorrectpassword.setObjectName("Incorrectpassword")
        Incorrectpassword.resize(215, 159)
        Incorrectpassword.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.text1 = QtWidgets.QLabel(Incorrectpassword)
        self.text1.setGeometry(QtCore.QRect(30, 10, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text1.setFont(font)
        self.text1.setStyleSheet("color: rgb(32, 151, 255);")
        self.text1.setAlignment(QtCore.Qt.AlignCenter)
        self.text1.setObjectName("text1")
        self.OkButton = QtWidgets.QPushButton(Incorrectpassword)
        self.OkButton.setGeometry(QtCore.QRect(60, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OkButton.setFont(font)
        self.OkButton.setStyleSheet("background-color: rgb(32, 151, 255);\n"
"color: rgb(255, 255, 255);")
        self.OkButton.setObjectName("OkButton")


        self.retranslateUi(Incorrectpassword)
        QtCore.QMetaObject.connectSlotsByName(Incorrectpassword)

    def retranslateUi(self, Incorrectpassword):
        _translate = QtCore.QCoreApplication.translate
        Incorrectpassword.setWindowTitle(_translate("Incorrectpassword", "Incorrect Password"))
        self.text1.setText(_translate("Incorrectpassword", "Incorrect password"))
        self.OkButton.setText(_translate("Incorrectpassword", "OK"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Incorrectpassword = QtWidgets.QDialog()
    ui = Ui_Incorrectpassword()
    ui.setupUi(Incorrectpassword)
    Incorrectpassword.show()
    sys.exit(app.exec_())
