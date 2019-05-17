# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Check_Code.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CodeMessage(object):
    def setupUi(self, CodeMessage):
        CodeMessage.setObjectName("CodeMessage")
        CodeMessage.resize(560, 112)
        CodeMessage.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.message1 = QtWidgets.QLabel(CodeMessage)
        self.message1.setGeometry(QtCore.QRect(20, 10, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.message1.setFont(font)
        self.message1.setStyleSheet("color: rgb(32, 151, 255);")
        self.message1.setObjectName("message1")
        self.OkButton3 = QtWidgets.QPushButton(CodeMessage)
        self.OkButton3.setGeometry(QtCore.QRect(220, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OkButton3.setFont(font)
        self.OkButton3.setStyleSheet("background-color: rgb(32, 151, 255);\n"
"color: rgb(255, 255, 255);")
        self.OkButton3.setObjectName("OkButton3")

        self.retranslateUi(CodeMessage)
        QtCore.QMetaObject.connectSlotsByName(CodeMessage)

    def retranslateUi(self, CodeMessage):
        _translate = QtCore.QCoreApplication.translate
        CodeMessage.setWindowTitle(_translate("CodeMessage", "Check Code"))
        self.message1.setText(_translate("CodeMessage", "The code has been sent to your email. Please check your email and enter the code provided."))
        self.OkButton3.setText(_translate("CodeMessage", "OK"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CodeMessage = QtWidgets.QDialog()
    ui = Ui_CodeMessage()
    ui.setupUi(CodeMessage)
    CodeMessage.show()
    sys.exit(app.exec_())
