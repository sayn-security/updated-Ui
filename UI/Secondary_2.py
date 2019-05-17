# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Secondary_2.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

order1=[]

class Ui_Secondary_Password(object):
    
    def get_pic1(self):
            order1.insert(1,'1')
    def get_pic2(self):
            order1.insert(2,'2')
    def get_pic3(self):
            order1.insert(3,'3')
    def get_pic4(self):
            order1.insert(4,'4')
    def get_pic5(self):
            order1.insert(5,'5')
    def get_pic6(self):
            order1.insert(6,'6')
    def get_pic7(self):
            order1.insert(7,'7')
    def get_pic8(self):
            order1.insert(8,'8')
    def print_or(self):
        print (order1)
    def log_order(self):
        ordoc=open("inoder.txt","w")
        for item in order1:
            ordoc.write(item)
        ordoc.close()

    def check_order(self):
        counter=0
        ordoc=open("inoder.txt","r")
        regorder=open("order_reg.txt","r")
        for item1 in order1:
            if (ordoc.mode=="r") & (regorder.mode=="r"):
                or1=ordoc.read()
                or2=regorder.read()
                
            if (or1 == or2):
                print("Welcome")
                break
            else:
                print("Wrong Pattern")    
                break
        ordoc.close()
        regorder.close()
        
    def setupUi(self, Secondary_Password):
        Secondary_Password.setObjectName("Secondary_Password")
        Secondary_Password.resize(1380, 800)
        Secondary_Password.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Secondary_Password)
        self.centralwidget.setObjectName("centralwidget")
        self.message = QtWidgets.QLabel(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(220, 150, 1051, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.message.setFont(font)
        self.message.setStyleSheet("color: rgb(32, 151, 255);\n"
"")
        self.message.setObjectName("message")
        self.dog = QtWidgets.QPushButton(self.centralwidget)
        self.dog.setGeometry(QtCore.QRect(400, 210, 131, 201))
        self.dog.setStyleSheet("border-radius: 60px;\n"
"background-color: rgb(0, 0, 0);\n"
"image: url(p10.jpg);")
        self.dog.setText("")
        self.dog.setObjectName("1")

        self.dog.clicked.connect(self.get_pic1)

        self.water = QtWidgets.QPushButton(self.centralwidget)
        self.water.setGeometry(QtCore.QRect(560, 210, 121, 201))
        self.water.setStyleSheet("border-radius: 60px;\n"
"background-color: rgb(0, 0, 0);\n"
"image: url(p7.jpg);")
        self.water.setText("")
        self.water.setObjectName("2")

        self.water.clicked.connect(self.get_pic2)

        self.paris = QtWidgets.QPushButton(self.centralwidget)
        self.paris.setGeometry(QtCore.QRect(720, 210, 121, 201))
        self.paris.setStyleSheet("border-radius: 60px;\n"
"background-color: rgb(0, 0, 0);\n"
"image: url(p2.jpg);")
        self.paris.setText("")
        self.paris.setObjectName("3")

        self.paris.clicked.connect(self.get_pic3)

        self.arc = QtWidgets.QPushButton(self.centralwidget)
        self.arc.setGeometry(QtCore.QRect(880, 210, 121, 201))
        self.arc.setStyleSheet("border-radius: 60px;\n"
"background-color: rgb(0, 0, 0);\n"
"image: url(p9.jpg);")
        self.arc.setText("")
        self.arc.setObjectName("4")

        self.arc.clicked.connect(self.get_pic4)

        self.eiffel = QtWidgets.QPushButton(self.centralwidget)
        self.eiffel.setGeometry(QtCore.QRect(400, 440, 121, 201))
        self.eiffel.setStyleSheet("border-radius: 60px;\n"
"background-color: rgb(0, 0, 0);\n"
"image: url(p1.jpg);")
        self.eiffel.setText("")
        self.eiffel.setObjectName("5")

        self.eiffel.clicked.connect(self.get_pic5)

        self.oxford = QtWidgets.QPushButton(self.centralwidget)
        self.oxford.setGeometry(QtCore.QRect(560, 440, 121, 201))
        self.oxford.setStyleSheet("border-radius: 60px;\n"
"background-color: rgb(0, 0, 0);\n"
"image: url(p3.jpg);")
        self.oxford.setText("")
        self.oxford.setObjectName("6")

        self.oxford.clicked.connect(self.get_pic6)

        self.flower = QtWidgets.QPushButton(self.centralwidget)
        self.flower.setGeometry(QtCore.QRect(720, 440, 121, 201))
        self.flower.setStyleSheet("border-radius: 60px;\n"
"background-color: rgb(0, 0, 0);\n"
"image: url(p8.jpg);")
        self.flower.setText("")
        self.flower.setObjectName("7")

        self.flower.clicked.connect(self.get_pic7)

        self.dog2 = QtWidgets.QPushButton(self.centralwidget)
        self.dog2.setGeometry(QtCore.QRect(880, 440, 121, 201))
        self.dog2.setStyleSheet("border-radius: 60px;\n"
"background-color: rgb(0, 0, 0);\n"
"image: url(p6.jpg);")
        self.dog2.setText("")
        self.dog2.setObjectName("8")

        self.dog2.clicked.connect(self.get_pic8)

        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(920, 650, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.submit.setFont(font)
        self.submit.setStyleSheet("background-color: rgb(32, 151, 255);\n"
"color: rgb(255, 255, 255);")
       
        self.submit.setObjectName("submit")

        self.submit.clicked.connect(self.print_or)
        self.submit.clicked.connect(self.log_order)
        self.submit.clicked.connect(self.check_order)
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(620, 0, 151, 141))
        self.frame.setStyleSheet("image: url(3.png);\n"
"border-radius: 60px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        Secondary_Password.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Secondary_Password)
        self.statusbar.setObjectName("statusbar")
        Secondary_Password.setStatusBar(self.statusbar)

        self.retranslateUi(Secondary_Password)
        QtCore.QMetaObject.connectSlotsByName(Secondary_Password)
    def retranslateUi(self, Secondary_Password):
        _translate = QtCore.QCoreApplication.translate
        Secondary_Password.setWindowTitle(_translate("Secondary_Password", "Secondary Password"))       
        self.message.setText(_translate("Secondary_Password","Your Password was correct but the pattern did not match. Please select the Pictures in order registered during Sign Up"))
        self.submit.setText(_translate("Secondary_Password", "Submit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Secondary_Password = QtWidgets.QMainWindow()
    ui = Ui_Secondary_Password()
    ui.setupUi(Secondary_Password)
    Secondary_Password.show()
    app.exec_()
    sys.exit()
    