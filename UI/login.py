# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import movie_data
import passwrong
class Ui_Form(object):
    def setupUi(self, Form):
        self.userFile = "./user.txt"
        self.movie_data = movie_data.Ui_Form()
        self.passw = passw()
        Form.setObjectName("Form")
        Form.resize(425, 415)
        Form.setMinimumSize(QtCore.QSize(10, 10))
        #美化窗口
        #Form.setWindowOpacity(0.9) # 设置窗口透明度
        #Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setStyleSheet('''background-color:white;''') 

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 195, 349, 65))
        self.lineEdit.setObjectName("lineEdit")
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        #
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 337, 349, 49))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 120, 349, 65))
        self.lineEdit_2.setObjectName("lineEdit_2")
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit.setPlaceholderText('密码')
        self.lineEdit_2.setPlaceholderText('用户名')
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit.setEchoMode(QLineEdit.Password)#密码输入
        

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 278, 349, 49))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(69, 50, 413, 41))
        font = QtGui.QFont()
        # font.setFamily("Comic Sans MS")
        font.setFamily('幼圆')
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.meihuabt1 = QtWidgets.QPushButton(Form)
        self.meihuabt1.setGeometry(QtCore.QRect(4, 8, 15, 15))
        self.meihuabt1.setText("")
        self.meihuabt1.setObjectName("meihuabt1")
        self.meihuabt2 = QtWidgets.QPushButton(Form)
        self.meihuabt2.setGeometry(QtCore.QRect(32, 8, 15, 15))
        self.meihuabt2.setText("")
        self.meihuabt2.setObjectName("meihuabt2")
        self.meihuabt3 = QtWidgets.QPushButton(Form)
        self.meihuabt3.setGeometry(QtCore.QRect(60, 8, 15, 15))
        self.meihuabt3.setText("")
        self.meihuabt3.setObjectName("meihuabt3")

        #美化
        self.meihuabt1.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.meihuabt2.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.meihuabt3.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.pushButton.setStyleSheet('''QPushButton{background:#FFC0CB;border-radius:5px;}QPushButton:hover{background:#FFC0CB;}''')
        self.pushButton_2.setStyleSheet('''QPushButton{background:#D1EEEE;border-radius:5px;}QPushButton:hover{background:#E0FFFF;}''')
        # self.meihuabt1.clicked.connect(self.showMaximized)
        self.meihuabt2.clicked.connect(self.showMinimized)
        self.meihuabt3.clicked.connect(Form.close)
        self.pushButton_2.clicked.connect(self.check)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def check(self):
        username = self.lineEdit_2.text()
        password = self.lineEdit.text()
        tag = 0
        # if username == None | password == None:
        #     self.passw.show()
        try:
            f = open(self.userFile,'r',encoding = 'utf-8')
            for line in f:
                line = line.strip()
                line_list = line.split('#')
                if line_list[0] == username and line_list[1] == password:
                    tag = 1
        except IOError:
            tag =0

        if tag == 1:
            self.movie_data.show()
            self.close()
        else:
            self.passw.show()

#前
#E0FFFF
        #美化


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登陆"))
        self.pushButton.setText(_translate("Form", "注册"))
        self.pushButton_2.setText(_translate("Form", "登录"))
        self.label.setText(_translate("Form", '    豆瓣酱'))

class passw(QtWidgets.QMainWindow,passwrong.Ui_Form):
    def __init__(self,parent = None):
        super(passw,self).__init__(parent)
        self.setupUi(self)