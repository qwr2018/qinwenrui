from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import pandas as pd
import string
import numpy as np
from pyecharts import Bar
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
class Ui_Form(object):
    def setupUi(self, Form):
        self.path = './graph/roleactor.html'
        Form.setObjectName("Form")
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
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(262, 20, 69, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
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
        Form.setWindowTitle(_translate("Form", "劳模演员"))
        self.comboBox_2.setItemText(0, _translate("Form", "所有年份"))
        self.comboBox_2.setItemText(1, _translate("Form", "  2018"))
        self.comboBox_2.setItemText(2, _translate("Form", "  2017"))
        self.comboBox_2.setItemText(3, _translate("Form", "  2016"))
        self.comboBox_2.setItemText(4, _translate("Form", "  2015"))
        self.label_2.setText(_translate("Form", "年份"))
        self.comboBox_4.setItemText(0, _translate("Form", "  3"))
        self.comboBox_4.setItemText(1, _translate("Form", "  5"))
        self.comboBox_4.setItemText(2, _translate("Form", " 10"))
        self.label_4.setText(_translate("Form", "TOP"))
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
        rank = self.comboBox_4.currentText().replace(' ','')#输入
        r = int(rank)
        sql = 'SELECT * FROM `dianying`;'
        df = pd.read_sql(sql,conn)


        if year != '所有年份':
                a = df[df.年份==year]
        else:
                a = df

        # print(a[:3].values[0][3])
        act = []
        for i in range(len(a)):
            b = a.values[i][3]
            act.append(b)
        c = []
        for j in act:
            actor = j.replace('比利时','').replace('俄罗斯','').replace('中国香港','').replace('韩国','').replace('爱情','').replace('日本','').replace('法国','').replace('英国','').replace('美国','').replace(',中国大陆','').replace('犯罪','').replace('喜剧','').replace('剧情','').replace('纪录片','').replace('奇幻','').replace('动作','').replace('冒险','').replace('悬疑','').replace('动画','').replace('战争','').replace('家庭','').replace('科幻','').replace('历史','').replace('惊悚','')
            c.append(actor)
        l = ','.join(c)
        # print(l[:300].split(',')[1])
        num = l.count(',')

        #初始化
        dct = {}
        for i in range(num+1):
            a = l.split(',')[i]
            dct[a] = 0
        #统计出现个数
        for i in range(num+1):
            a = l.split(',')[i]
            dct[a] +=1 

        dct['']=0
        dct['中国大陆'] = 0
        dct[' ']=0
        dct['加拿大'] = 0
        #按值进行降序排列
        L = sorted(dct.items(),key = lambda item:item[1],reverse = True)
        L=L[:r]#tuple类型

        ACTOR = []
        v = []
        for p in range(r):
            ACTOR.append(L[p][0])
            v.append(L[p][1])

        bar = Bar('{}年劳模演员TOP{}'.format(year,r),title_pos = 'center',width = 907,height = 619)
        bar._option['animation']= False
        bar.use_theme('vintage')
        bar.add('',ACTOR,v,is_label_show = 1)
        bar.render(self.path)
        self.widget.load(QUrl.fromLocalFile('/graph/roleactor.html'))
