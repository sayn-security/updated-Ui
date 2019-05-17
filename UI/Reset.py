# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reset.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_reset(object):

   # def backlogin_button(self):
    #    from Login import Ui_LOGIN
     #   self.window=QtWidgets.QMainWindow()
      #  self.ui=Ui_LOGIN()
       # self.ui.setupUi(self.window)
        #reset.hide()
        #self.window.show()
    




    def setupUi(self, reset):
        reset.setObjectName("reset")
        reset.resize(1380, 800)
        reset.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(reset)
        self.centralwidget.setObjectName("centralwidget")
        self.sayn = QtWidgets.QLabel(self.centralwidget)
        self.sayn.setGeometry(QtCore.QRect(600, 240, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.sayn.setFont(font)
        self.sayn.setAutoFillBackground(False)
        self.sayn.setStyleSheet("color: rgb(255, 255, 255);")
        self.sayn.setAlignment(QtCore.Qt.AlignCenter)
        self.sayn.setObjectName("sayn")
        self.message = QtWidgets.QLabel(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(410, 320, 621, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.message.setFont(font)
        self.message.setStyleSheet("color: rgb(32, 151, 255);")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setObjectName("message")
        self.message2 = QtWidgets.QLabel(self.centralwidget)
        self.message2.setGeometry(QtCore.QRect(640, 410, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.message2.setFont(font)
        self.message2.setStyleSheet("color: rgb(32, 151, 255);")
        self.message2.setAlignment(QtCore.Qt.AlignCenter)
        self.message2.setObjectName("message2")
        self.textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox.setGeometry(QtCore.QRect(530, 460, 391, 31))
        self.textbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textbox.setObjectName("textbox")
        self.resend = QtWidgets.QPushButton(self.centralwidget)
        self.resend.setGeometry(QtCore.QRect(380, 520, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.resend.setFont(font)
        self.resend.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 151, 255);\n"
"")
        self.resend.setObjectName("resend")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(880, 520, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.submit.setFont(font)
        self.submit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 151, 255);\n"
"")
        self.submit.setObjectName("submit")
        self.image = QtWidgets.QPushButton(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(650, 80, 151, 141))
        self.image.setStyleSheet("image: url(3.png);\n"
"border-radius: 60px;\n"
"background-color: rgb(255, 255, 255);")
        self.image.setText("")
        self.image.setObjectName("image")

        self.backbutton = QtWidgets.QPushButton(self.centralwidget)
        self.backbutton.setGeometry(QtCore.QRect(30, 20, 71, 41))
        self.backbutton.setStyleSheet("background-color: rgb(32, 151, 255);\n"
"image: url(arrow 4.png);")
        self.backbutton.setText("")
        self.backbutton.setObjectName("backbutton")

        #self.backbutton.clicked.connect(self.backlogin_button)

        reset.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(reset)
        self.statusbar.setObjectName("statusbar")
        reset.setStatusBar(self.statusbar)

        self.retranslateUi(reset)
        QtCore.QMetaObject.connectSlotsByName(reset)

    def retranslateUi(self, reset):
        _translate = QtCore.QCoreApplication.translate
        reset.setWindowTitle(_translate("reset", "Reset Password"))
        self.sayn.setText(_translate("reset", "SAYN SECURITIES"))
        self.message.setText(_translate("reset", "Athentication code has been sent to the registered E-mail"))
        self.message2.setText(_translate("reset", "Enter Code"))
        self.resend.setText(_translate("reset", "Re-send"))
        self.submit.setText(_translate("reset", "Submit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    reset = QtWidgets.QMainWindow()
    ui = Ui_reset()
    ui.setupUi(reset)
    reset.show()
    app.exec_()
