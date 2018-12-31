# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import info
import exist
class Ui_Form(object):
    def setupUi(self, Form):
        self.child = info()
        self.exist = ex()
        self.userFile = './user.txt'
        self.flag = 0
        Form.setObjectName("Form")
        Form.resize(425, 415)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 305, 349, 65))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 47, 413, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        self.label.setFont(font)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 195, 349, 65))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 120, 349, 65))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(4, 8, 15, 15))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(32, 8, 15, 15))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 8, 15, 15))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")



        #美化
        self.pushButton.setStyleSheet('''QPushButton{background:#FFC0CB;border-radius:5px;}QPushButton:hover{background:#DB7093;}''')
        self.pushButton_2.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.pushButton_3.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.pushButton_4.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setStyleSheet('''background-color:white;''') 

        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setPlaceholderText('用户名')
        self.lineEdit_3.setPlaceholderText('密码')
        self.lineEdit_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setEchoMode(QLineEdit.Password)#密码输入

        self.pushButton.clicked.connect(self.userRegister)
        self.pushButton_4.clicked.connect(Form.close)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "确认"))
        self.label.setText(_translate("Form", "创造属于你的账号"))


    def userRegister(self):
        self.username = self.lineEdit_4.text()
        self.password = self.lineEdit_3.text()
        self.flag = 0
        try:
            with open(self.userFile,'r',encoding = 'utf-8') as f:
                for line in f:
                    line = line.strip()
                    line_new = line.split("#")
                    if line_new[0] == self.username:
                        self.flag = 1
                        self.exist.show()
                        break
        except IOError:
            self.flag = 1

        if self.flag == 0:
            with open(self.userFile,'a',encoding = 'utf-8') as f:
                temp = '\n'+self.username+'#'+self.password
                f.write(temp)
            self.child.show()
            # time.sleep(5)
            #
            self.close()


class info(QtWidgets.QWidget,info.Ui_Form):
    def __init__(self,parent = None):
        super(info,self).__init__(parent)
        self.setupUi(self)



class ex(QtWidgets.QWidget,exist.Ui_Form):
    def __init__(self,parent = None):
        super(ex,self).__init__(parent)
        self.setupUi(self)