# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Correct_password.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

#from Secondary_2 import Ui_Secondary_Password

class Ui_correctpassword(object):

    #def secpass(self):
        
    #    self.window=QtWidgets.QMainWindow()
      #  self.ui=Ui_Secondary_Password()
     #   self.ui.setupUi(self.window)
     #   correctpassword.hide()
      #  self.window.show()


    def setupUi(self, correctpassword):
        correctpassword.setObjectName("correctpassword")
        correctpassword.resize(831, 121)
        correctpassword.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.nextbutton = QtWidgets.QPushButton(correctpassword)
        self.nextbutton.setGeometry(QtCore.QRect(350, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nextbutton.setFont(font)
        self.nextbutton.setStyleSheet("background-color: rgb(32, 151, 255);\n"
"color: rgb(255, 255, 255);")
        self.nextbutton.setObjectName("nextbutton")

        #self.nextbutton.clicked.connect(self.secpass)

        self.MESSAGE = QtWidgets.QLabel(correctpassword)
        self.MESSAGE.setGeometry(QtCore.QRect(30, 10, 771, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.MESSAGE.setFont(font)
        self.MESSAGE.setStyleSheet("color: rgb(32, 151, 255);")
        self.MESSAGE.setAlignment(QtCore.Qt.AlignCenter)
        self.MESSAGE.setObjectName("MESSAGE")

        self.retranslateUi(correctpassword)
        QtCore.QMetaObject.connectSlotsByName(correctpassword)

    def retranslateUi(self, correctpassword):
        _translate = QtCore.QCoreApplication.translate
        correctpassword.setWindowTitle(_translate("correctpassword", "Correct Password"))
        self.nextbutton.setText(_translate("correctpassword", "NEXT"))
        self.MESSAGE.setText(_translate("correctpassword", "The password is correct, but the pattern did not match. Please click next for 2-factor authentication."))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    correctpassword = QtWidgets.QDialog()
    ui = Ui_correctpassword()
    ui.setupUi(correctpassword)
    correctpassword.show()
    sys.exit(app.exec_())
