import sys
import os
import re
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pynput import keyboard
import time
import decimal
import xlsxwriter
from threading import Thread
import time
import tkinter
from Login import Ui_LOGIN
from Reset import Ui_reset
from Login import keylistener
from Correct_password import Ui_correctpassword
from Incorrect_password import Ui_Incorrectpassword
from registration import Ui_Registration
from Secondary import Ui_secondary
from Secondary_2 import Ui_Secondary_Password
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string
import emailsayn


class incorwindow(QtWidgets.QDialog, Ui_Incorrectpassword):
    def __init__(self, parent=None):
        super(incorwindow, self).__init__(parent)
        self.setupUi(self)
        self.OkButton.clicked.connect(self.hide)



class loginwindow(QtWidgets.QMainWindow, Ui_LOGIN):
    
    def __init__(self, parent=None):
        super(loginwindow, self).__init__(parent)
        self.setupUi(self)
        self.loginbutton.clicked.connect(self.hide)
          
class secd2window(QtWidgets.QMainWindow, Ui_Secondary_Password):
    
    def __init__(self, parent=None):
        super(secd2window, self).__init__(parent)
        self.setupUi(self)
        self.submit.clicked.connect(self.hide)
        
class resetwindow(QtWidgets.QMainWindow, Ui_reset):
    def __init__(self, parent=None):
        super(resetwindow, self).__init__(parent)
        self.setupUi(self)
        self.backbutton.clicked.connect(self.hide)

class regwindow(QtWidgets.QMainWindow, Ui_Registration):
    
    def __init__(self, parent=None):
        super(regwindow, self).__init__(parent)
        self.setupUi(self)
        self.nextbutton.clicked.connect(self.hide)

class regsecdwindow(QtWidgets.QMainWindow, Ui_secondary):
    
    def __init__(self, parent=None):
        super(regsecdwindow, self).__init__(parent)
        self.setupUi(self)
        self.backbutton.clicked.connect(self.hide)

class Manager:
    

   
    def keyPressEvent(self, e):
        print ("event", e)
        if e.key()  == QtCore.Qt.Key_Return :
            self.check_passlog()
        elif e.key() == QtCore.Qt.Key_Enter :   
            self.check_passlog()

    def check_passlog(self):
                usdata1=self.login.passwordbox.text()
                usdoc1= open("temp_pass.txt","w")
                usdoc1.write(usdata1)
                usdoc1.close()
                temppass= open("temp_pass.txt","r")
                regpass=open("regpass.txt","r")
                tp=temppass.read()
                rp=regpass.read()
                if(tp == rp):
                    print("Correct Password")
                    self.secd2.show()
                else:
                    print("Incorrect Password")
                    self.inco.show()
                temppass.close()
                regpass.close()
                 
    def __init__(self):
       
        self.login = loginwindow()
        self.inco = incorwindow()
        self.secd2=secd2window()
        self.reset=resetwindow()
        self.reg=regwindow()
        self.regsecd=regsecdwindow()
        x=Thread(target=self.login.show())
        x.start()    
        app.processEvents()
 
        self.login.centralwidget.keyPressEvent = self.keyPressEvent
        self.login.loginbutton.clicked.connect(self.check_passlog)
        self.inco.OkButton.clicked.connect(self.login.show)
        self.login.resetbutton.clicked.connect(self.reset.show)
        self.reset.backbutton.clicked.connect(self.login.show)
        self.secd2.submit.clicked.connect(self.login.hide)
        self.reg.nextbutton.clicked.connect(self.regsecd.show)
        self.regsecd.backbutton.clicked.connect(self.reg.show)
        #self.login.resetbutton.clicked.connect(emailsayn.sender(2,'wasabiijunior@gmail.com'))
        

if __name__ == '__main__':
    keylistener()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    app.exec_()
    #print(sender(2,'wasabiijunior@gmail.com'))
    sys.exit()
    