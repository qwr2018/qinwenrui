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
from pyecharts import Pie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
class Ui_Form(object):
    def setupUi(self, Form):
        self.path = './graph/jidutype.html'
        Form.setObjectName("Form")
        self.setWindowIcon(QIcon('douyin.png'))
        Form.resize(905, 700)
        self.widget = QWebEngineView(self)
        self.widget.setGeometry(QtCore.QRect(-9, 90, 927, 635))
        self.widget.setObjectName("widget")
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 20, 111, 49))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setFont(font)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(49, 20, 69, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(338, 20, 92, 49))
        self.comboBox_4.setObjectName("comboBox_4")
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.comboBox_4.setFont(font)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(262, 20, 69, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(462, 21, 125, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(692, 21, 133, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
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
        Form.setWindowTitle(_translate("Form", "电影词云"))
        self.comboBox_2.setItemText(0, _translate("Form", "所有年份"))
        self.comboBox_2.setItemText(1, _translate("Form", "  2018"))
        self.comboBox_2.setItemText(2, _translate("Form", "  2017"))
        self.comboBox_2.setItemText(3, _translate("Form", "  2016"))
        self.comboBox_2.setItemText(4, _translate("Form", "  2015"))
        self.label_2.setText(_translate("Form", "年份"))
        self.comboBox_4.setItemText(0, _translate("Form", "  1"))
        self.comboBox_4.setItemText(1, _translate("Form", "  2"))
        self.comboBox_4.setItemText(2, _translate("Form", "  3"))
        self.comboBox_4.setItemText(3, _translate("Form", "  4"))
        self.label_4.setText(_translate("Form", "季度"))
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

        year = self.comboBox_2.currentText().replace(' ','')
        quater = self.comboBox_4.currentText().replace(' ','')#输入

        sql = 'SELECT * FROM `dianying`;'
        df = pd.read_sql(sql,conn)
        if year != '所有年份':
            a = df[(df.年份==year)&(df.季度==int(quater))]
        else:
            a = df[(df.季度==int(quater))]

        M = []
        TYPE = a[['题材','票房']]
        c = TYPE[(TYPE.题材 == '犯罪')]
        money=0
        for k in c.index.tolist():
            money = money + c.loc[k].values[1]
        M.append(money)

        c = TYPE[(TYPE.题材 == '喜剧')]
        money=0
        for k in c.index.tolist():
            money = money + c.loc[k].values[1]
        M.append(money)

        c = TYPE[(TYPE.题材 == '剧情')]
        money=0
        for k in c.index.tolist():
            money = money + c.loc[k].values[1]
        M.append(money)

        c = TYPE[(TYPE.题材 == '纪录片')]
        money=0
        for k in c.index.tolist():
            money = money + c.loc[k].values[1]
        M.append(money)

        c = TYPE[(TYPE.题材 == '奇幻')]
        money=0
        for k in c.index.tolist():
            money = money + c.loc[k].values[1]
        M.append(money)

        c = TYPE[(TYPE.题材 == '动作')]
        money=0
        for k in c.index.tolist():
            money = money + c.loc[k].values[1]
        M.append(money)

        c = TYPE[(TYPE.题材 == '冒险')]
        money=0
        for k in c.index.tolist():
            money = money + c.loc[k].values[1]
        M.append(money)

        c = TYPE[(TYPE.题材 == '悬疑')]
        money=0
        for k in c.index.tolist():
            money = money + c.loc[k].values[1]
        M.append(money)

        c = TYPE[(TYPE.题材 == '动画')]
        money=0
        for k in c.index.tolist():
            money = money + c.loc[k].values[1]
        M.append(money)

        c = TYPE[(TYPE.题材 == '战争')]
        money=0
        for k in c.index.tolist():
            money = money + c.loc[k].values[1]
        M.append(money)

        c = TYPE[(TYPE.题材 == '家庭')]
        money=0
        for k in c.index.tolist():
            money = money + c.loc[k].values[1]
        M.append(money)

        c = TYPE[(TYPE.题材 == '科幻')]
        money=0
        for k in c.index.tolist():
            money = money + c.loc[k].values[1]
        M.append(money)

        c = TYPE[(TYPE.题材 == '历史')]
        money=0
        for k in c.index.tolist():
            money = money + c.loc[k].values[1]
        M.append(money)

        #TYPE.loc[rows]获取信息
        tp = ['犯罪','喜剧','剧情','纪录片','奇幻','动作','冒险','悬疑','动画','战争','家庭','科幻','历史']

        # cnt = []
        # for k in TYPE.index.tolist():#获得dataframe数据类型的行标
        #   cnt.append(TYPE.loc[k])
        # num = [cnt.count('犯罪'),cnt.count('喜剧'),cnt.count('剧情'),cnt.count('纪录片'),cnt.count('奇幻'),cnt.count('动作'),cnt.count('冒险'),cnt.count('悬疑'),cnt.count('动画'),cnt.count('战争'),cnt.count('家庭'),cnt.count('科幻'),cnt.count('历史')]
        pie = Pie('{}年第{}季度题材票房占比'.format(year,quater),title_pos ='center',width = 907,height = 619 )
        pie._option['animation']= False
        pie.use_theme('dark')
        pie.add('',tp,M,center = [50,50],radius = [0,60],is_label_show = True,legend_orient = 'vertical',legend_pos = 'left')
        pie.render(self.path)
        self.widget.load(QUrl.fromLocalFile('/graph/jidutype.html'))
