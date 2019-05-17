# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import PyQt5
import write_to_sheet
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pynput import keyboard
import keyboard as newKeyboard
import time
import decimal
import xlsxwriter
from threading import Thread
import time
import tkinter



class Ui_LOGIN(object):
    
    def passwordcor(self):
       
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_correctpassword()
        self.ui.setupUi(self.window)
        self.window.show()
      
    def passwordincor(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Incorrectpassword()
        self.ui.setupUi(self.window)
        self.window.show()        

    def setupUi(self, LOGIN):
        
        LOGIN.setObjectName("LOGIN")
        LOGIN.resize(1350, 800)
        LOGIN.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(LOGIN)
        self.centralwidget.setObjectName("centralwidget")
        self.sayn = QtWidgets.QLabel(self.centralwidget)
        self.sayn.setGeometry(QtCore.QRect(570, 240, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.sayn.setFont(font)
        self.sayn.setAutoFillBackground(False)
        self.sayn.setStyleSheet("color: rgb(255, 255, 255);")
        self.sayn.setAlignment(QtCore.Qt.AlignCenter)
        self.sayn.setObjectName("sayn")
       
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(550, 400, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.password.setFont(font)
        self.password.setStyleSheet("color: rgb(32, 151, 255);")
        self.password.setObjectName("password")

        self.passwordbox = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordbox.setGeometry(QtCore.QRect(550, 430, 311, 31))
        self.passwordbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.passwordbox.setObjectName("passwordbox")
        self.passwordbox.thread()
        self.loginbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loginbutton.setGeometry(QtCore.QRect(630, 490, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loginbutton.setFont(font)
        self.loginbutton.setStyleSheet("background-color: rgb(32, 151, 255);\n"
"color: rgb(255, 255, 255);")
        self.loginbutton.setObjectName("loginbutton")

        self.resetbutton = QtWidgets.QPushButton(self.centralwidget)
        self.resetbutton.setGeometry(QtCore.QRect(630, 580, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.resetbutton.setFont(font)
        self.resetbutton.setStyleSheet("background-color: rgb(32, 151, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.resetbutton.setObjectName("resetbutton")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(620, 540, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setStyleSheet("color: rgb(255, 255, 255);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(740, 540, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.ORtext = QtWidgets.QLabel(self.centralwidget)
        self.ORtext.setGeometry(QtCore.QRect(680, 530, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ORtext.setFont(font)
        self.ORtext.setStyleSheet("color: rgb(255, 255, 255);")
        self.ORtext.setAlignment(QtCore.Qt.AlignCenter)
        self.ORtext.setObjectName("ORtext")
        self.image = QtWidgets.QPushButton(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(630, 90, 141, 131))
        self.image.setStyleSheet("border-radius: 60px;\n"
"background-color: rgb(255, 255, 255);\n"
"image: url(3.png);")
        self.image.setText("")
        self.image.setObjectName("image")
        LOGIN.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LOGIN)
        self.statusbar.setObjectName("statusbar")
        LOGIN.setStatusBar(self.statusbar)

        self.retranslateUi(LOGIN)
        QtCore.QMetaObject.connectSlotsByName(LOGIN)
        #self.centralwidget.keyPressEvent = self.keyPressEvent

    def retranslateUi(self, LOGIN):
        _translate = QtCore.QCoreApplication.translate
        LOGIN.setWindowTitle(_translate("LOGIN", "Login"))
        self.sayn.setText(_translate("LOGIN", "SAYN SECURITIES"))
        self.password.setText(_translate("LOGIN", "Password"))
        self.loginbutton.setText(_translate("LOGIN", "LOGIN"))
        self.resetbutton.setText(_translate("LOGIN", "Forget Password"))
        self.ORtext.setText(_translate("LOGIN", "OR"))
        
    
def keylistener():
    a = []
    tim = []
    pr = []
    rl = []
    prt = []
    rlt = []  

    def on_press(event):
        key = event.name
        print(key)
        if key is "enter":
        # Stop listener
            print("ended")
            from write_to_sheet import write2sheet
            y=Thread(target=write2sheet(a, tim, pr, rl, prt, rlt), daemon=True)
            y.start()
            print ("recorded one password entery")
            newKeyboard.unhook_all()
            return False
        else:
            value = str(key)
            pr.append(value)
            prt.append(decimal.Decimal(time.clock()))
            a.append(value)
            tim.append(decimal.Decimal(time.clock()))

    def on_release(event):
        key = event.name
        if key is "enter":
            # Stop listener
            newKeyboard.unhook_all()
            return False
    
        value = str(key)
        rl.append(value)
        rlt.append(decimal.Decimal(time.clock()))
        a.append(value)
        tim.append(decimal.Decimal(time.clock()))
    
    newKeyboard.block_key("left windows")
    newKeyboard.on_press(on_press)
    newKeyboard.hook(on_release)
    
    print("keylogger running")

def main():
    keylistener()

    import sys
    app = QtWidgets.QApplication(sys.argv)
    LOGIN = QtWidgets.QMainWindow()
    ui = Ui_LOGIN()
    ui.setupUi(LOGIN);
    

   #x=Thread(target=LOGIN.show(),args=(1,))
    #x.run()    
    #app.processEvents()
    
    execu=app.exec()
    sys.exit(execu)

if __name__ == "__main__":
    main()