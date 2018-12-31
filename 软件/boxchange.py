# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tt.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import pandas as pd
import string
import numpy as np
from pyecharts import Line
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
class Ui_Form(object):
    def setupUi(self, Form):
        self.path = './graph/boxchange.html'
        self.setWindowIcon(QIcon('douyin.png'))
        Form.setObjectName("Form")
        Form.resize(905, 700)
        self.widget = QWebEngineView(self)
        self.widget.setGeometry(QtCore.QRect(0, 90, 910, 650))
        self.widget.setObjectName("widget")
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 20, 85, 49))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setFont(font)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(83, 20, 41, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(340, 20, 85, 49))
        self.comboBox_4.setObjectName("comboBox_4")
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.comboBox_4.setFont(font)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(292, 20, 41, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(740, 4, 125, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(740, 48, 125, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.comboBox_5 = QtWidgets.QComboBox(Form)
        self.comboBox_5.setGeometry(QtCore.QRect(550, 20, 85, 49))
        self.comboBox_5.setObjectName("comboBox_5")
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.comboBox_5.setFont(font)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        #self.comboBox_5.addItem("")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(504, 20, 45, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
#美化
        self.meihuabt1 = QtWidgets.QPushButton(Form)
        self.meihuabt1.setGeometry(QtCore.QRect(4, 2, 14, 14))
        self.meihuabt1.setText("")
        self.meihuabt1.setObjectName("meihuabt1")
        self.meihuabt2 = QtWidgets.QPushButton(Form)
        self.meihuabt2.setGeometry(QtCore.QRect(32, 2, 14, 14))
        self.meihuabt2.setText("")
        self.meihuabt2.setObjectName("meihuabt2")
        self.meihuabt3 = QtWidgets.QPushButton(Form)
        self.meihuabt3.setGeometry(QtCore.QRect(60, 2, 14, 14))
        self.meihuabt3.setText("")
        self.meihuabt3.setObjectName("meihuabt3")
        self.meihuabt1.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.meihuabt2.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.meihuabt3.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        Form.setWindowOpacity(0.96)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setStyleSheet('''background-color:#FFF0F50 ;''')
        self.meihuabt3.clicked.connect(self.close)
        self.meihuabt1.clicked.connect(self.showMinimized)



        self.radioButton.toggled.connect(self.display)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "票房趋势"))
        self.comboBox_2.setItemText(0, _translate("Form", " 2018"))
        self.comboBox_2.setItemText(1, _translate("Form", " 2017"))
        self.comboBox_2.setItemText(2, _translate("Form", " 2016"))
        self.comboBox_2.setItemText(3, _translate("Form", " 2015"))
        self.label_2.setText(_translate("Form", "壹"))
        self.comboBox_4.setItemText(0, _translate("Form", " 2018"))
        self.comboBox_4.setItemText(1, _translate("Form", " 2017"))
        self.comboBox_4.setItemText(2, _translate("Form", " 2016"))
        self.comboBox_4.setItemText(3, _translate("Form", " 2015"))
        self.label_4.setText(_translate("Form", "贰"))
        self.comboBox_5.setItemText(0, _translate("Form", " 2018"))
        self.comboBox_5.setItemText(1, _translate("Form", " 2017"))
        self.comboBox_5.setItemText(2, _translate("Form", " 2016"))
        self.comboBox_5.setItemText(3, _translate("Form", " 2015"))


        self.radioButton.toggled.connect(self.display)
        self.label_5.setText(_translate("Form", "叁"))
        self.radioButton.setText(_translate("Form", "WATCH ME"))
        self.checkBox.setText(_translate("Form", "KEEP IT？"))

    def display(self):
        self.radioButton.setChecked(True)  
        conn = pymysql.connect(
            host = '127.0.0.1',
            user = 'root',
            passwd = '714511',
            db = 'qinwenrui',
            port = 3306,
            charset = 'utf8mb4'
            )

        year1 = int(self.comboBox_2.currentText().replace(' ',''))
        year2 = int(self.comboBox_4.currentText().replace(' ',''))#输入
        year3 = int(self.comboBox_5.currentText().replace(' ',''))#输入
        
        attr = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
        v1 = []
        v2 = []
        v3 = []
        sql = 'SELECT * FROM `dianying`;'
        df = pd.read_sql(sql,conn)

        a = df[(df.年份==str(year1))]
        for i in range(1,13):
            a1 = a[a.月份 == i]
            money = 0
            for k in a1.index.tolist():
                money = money+a1.loc[k].values[1]
            v1.append(money)

        a = df[(df.年份==str(year2))]
        for i in range(1,13):
            a1 = a[a.月份 == i]
            money = 0
            for k in a1.index.tolist():
                money = money+a1.loc[k].values[1]
            v2.append(money)

        a = df[(df.年份==str(year3))]
        for i in range(1,13):
            a1 = a[a.月份 == i]
            money = 0
            for k in a1.index.tolist():
                money = money+a1.loc[k].values[1]
            v3.append(money)

        line = Line('电影票房变化趋势',width = 900,height = 620)
        line._option['animation']= False
        # line.use_theme("dark")
        line.add('{}年'.format(year1),attr,v1,is_lable_show=True)
        line.add('{}年'.format(year2),attr,v2,is_lable_show=True)
        line.add('{}年'.format(year3),attr,v3,is_lable_show=True)
        line.render(self.path)
        self.widget.load(QUrl.fromLocalFile('/graph/boxchange.html'))