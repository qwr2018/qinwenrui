# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie_data.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pymysql
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import pdfkit
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1400, 787)
        self.setWindowIcon(QIcon('douyin.png'))



        #初始化窗口
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(86, 175, 1228, 488))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(124, 64, 128, 61))
        self.comboBox.setObjectName("comboBox")
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(44, 68, 73, 45))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(512, 68, 73, 45))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(588, 64, 125, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.lineEdit.setFont(font);
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setFont(font)
        #self.comboBox_2.setAlignment(Qt.AlignCenter)
        self.comboBox_2.setGeometry(QtCore.QRect(356, 64, 130, 61))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        # self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(276, 68, 73, 45))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(756, 60, 97, 69))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(884, 60, 97, 69))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(1012, 60, 97, 69))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(1140, 60, 97, 69))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(1268, 60, 97, 69))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.pushButton_5.setFont(font)

        self.pushButton_5.setObjectName("pushButton_5")

        #生成报表按钮
        self.tablebt = QtWidgets.QPushButton(Form)
        self.tablebt.setGeometry(QtCore.QRect(1322, 375, 69, 120))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.tablebt.setFont(font)
        self.tablebt.setObjectName("tablebt")

        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(652, 674, 200, 100))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")

        #美化

        self.meihuabt1 = QtWidgets.QPushButton(Form)
        self.meihuabt1.setGeometry(QtCore.QRect(4, 8, 18, 18))
        self.meihuabt1.setText("")
        self.meihuabt1.setObjectName("meihuabt1")
        self.meihuabt2 = QtWidgets.QPushButton(Form)
        self.meihuabt2.setGeometry(QtCore.QRect(42, 8, 18, 18))
        self.meihuabt2.setText("")
        self.meihuabt2.setObjectName("meihuabt2")
        self.meihuabt3 = QtWidgets.QPushButton(Form)
        self.meihuabt3.setGeometry(QtCore.QRect(80, 8, 18, 18))
        self.meihuabt3.setText("")
        self.meihuabt3.setObjectName("meihuabt3")

        #美化

        self.meihuabt1.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.meihuabt2.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.meihuabt3.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setStyleSheet('''border:10px solid #FFF0F50''') ##F8F8FF
        Form.setStyleSheet('''background-color:#FFF0F50;''')
        self.tableWidget.setStyleSheet('''background-color:white;''') 
        self.pushButton.setStyleSheet('''QPushButton{background:#D1EEEE;border-radius:5px;}QPushButton:hover{background:#7AC5CD;}''')
        self.pushButton_2.setStyleSheet('''QPushButton{background:#B4EEB4;border-radius:5px;}QPushButton:hover{background:#9ACD32;}''')
        self.pushButton_3.setStyleSheet('''QPushButton{background:#FFC0CB;border-radius:5px;}QPushButton:hover{background:#EEA2AD;}''')
        self.pushButton_4.setStyleSheet('''QPushButton{background:#DDA0DD;border-radius:5px;}QPushButton:hover{background:#9F79EE;}''')
        self.pushButton_5.setStyleSheet('''QPushButton{background:#EE799F;border-radius:5px;}QPushButton:hover{background:#FF69B4;}''')
        self.tablebt.setStyleSheet('''QPushButton{background:#FFC0CB;border-radius:5px;}QPushButton:hover{background:#FF82AB;}''')

        Form.setWindowOpacity(0.92) # 设置窗口透明度
        self.tablebt.clicked.connect(self.getfile)
        self.meihuabt3.clicked.connect(self.close)
        self.meihuabt1.clicked.connect(self.showMinimized)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def getfile(self):#利用pdfkit和选择对话框生成报表pdf
        dlg = QFileDialog()
        dlg.setGeometry(QtCore.QRect(86,175, 1228, 488))
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.selectedFiles()
        
        try:#返回空的时候直接退出
            selectedFiles = dlg.getOpenFileNames(self,"选择需要生成报表的文件","./graph",'Document ( * )')
            namelst = selectedFiles[0]
            length = len(namelst)
            options = {
             'page-size': 'A4',
             'margin-top': '0.1in',
             'margin-right': '0.1in',
             'margin-bottom': '0.1in',
             'margin-left': '0.1in',
             'encoding': "UTF-8",
             }
            path_wk = r'./wkhtmltox/bin/wkhtmltopdf.exe' #安装位置
            config = pdfkit.configuration(wkhtmltopdf = path_wk)
            pdfkit.from_file(namelst, './table/table.pdf',configuration=config,options = options)
        except:
            dlg.close()



    def retranslateUi(self, Form):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "电影名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "票房"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "导演"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "演员"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "题材"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "年份"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "季度"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "月份"))
        self.comboBox.setItemText(0, _translate("Form", "所有年份"))
        self.comboBox.setItemText(1, _translate("Form", "  2018"))
        self.comboBox.setItemText(2, _translate("Form", "  2017"))
        self.comboBox.setItemText(3, _translate("Form", "  2016"))
        self.comboBox.setItemText(4, _translate("Form", "  2015"))
        self.label.setText(_translate("Form", "年份"))
        self.label_3.setText(_translate("Form", "演员"))
        self.comboBox_2.setItemText(0, _translate("Form", "所有分类"))
        self.comboBox_2.setItemText(1, _translate("Form", "  犯罪"))
        self.comboBox_2.setItemText(2, _translate("Form", "  剧情"))
        self.comboBox_2.setItemText(3, _translate("Form", "  奇幻"))
        self.comboBox_2.setItemText(4, _translate("Form", "  动作"))
        self.comboBox_2.setItemText(5, _translate("Form", "  冒险"))
        self.comboBox_2.setItemText(6, _translate("Form", "  悬疑"))
        self.comboBox_2.setItemText(7, _translate("Form", "  动画"))
        self.comboBox_2.setItemText(8, _translate("Form", "  战争"))
        self.comboBox_2.setItemText(9, _translate("Form", "  家庭"))
        self.comboBox_2.setItemText(10, _translate("Form", "  科幻"))
        self.comboBox_2.setItemText(11, _translate("Form", "  历史"))
        self.comboBox_2.setItemText(12, _translate("Form", "  喜剧"))
        self.comboBox_2.setItemText(13, _translate("Form", " 纪录片"))
        self.label_2.setText(_translate("Form", "分类"))
        self.pushButton.setText(_translate("Form", "云"))
        self.pushButton_2.setText(_translate("Form", "星"))
        self.pushButton_3.setText(_translate("Form", "势"))
        self.pushButton_4.setText(_translate("Form", "季"))
        self.pushButton_5.setText(_translate("Form", "月"))
        self.tablebt.setText(_translate("Form",'生\n成\n报\n表'))
        self.radioButton.setText(_translate("Form", "尋"))


    def findinfo(self):
        self.radioButton.setChecked(True)  
        year = self.comboBox.currentText()
        category = self.comboBox_2.currentText()
        actor = self.lineEdit.text()
        #----连接数据库----
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='714511', db='qinwenrui',charset='utf8')
        self.curs = self.conn.cursor() 

        #搜索功能
        if year == '所有年份': 
            if category == '所有分类':
                self.sqlstring = 'SELECT * FROM qinwenrui.dianying where `演员` like' + '\'%'+actor+'%\''
            else:
                self.sqlstring = 'SELECT * FROM qinwenrui.dianying where `演员` like' + '\'%'+actor+'%\''+'and `题材` = '+ '\''+category.replace(' ','')+'\''
        elif category == '所有分类':
            if year == '所有年份':
                self.sqlstring = 'SELECT * FROM qinwenrui.dianying where `演员` like' + '\'%'+actor+'%\''
            else:
                self.sqlstring = 'SELECT * FROM qinwenrui.dianying where `演员` like' + '\'%'+actor+'%\''+'and `年份` = '+ '\''+ year.replace(' ','')+'\''
        else:
            self.sqlstring = 'SELECT * FROM qinwenrui.dianying where `演员` like' + '\'%'+actor+'%\''+'and `年份` = '+ '\''+ year.replace(' ','')+'\''+'and `题材` = ' +'\''+category.replace(' ','')+'\''

        c = self.curs.execute(self.sqlstring)
        num = c#返回的数据长度

        self.tableWidget.setRowCount(c)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#禁止编辑
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)#禁止选择
        self.tableWidget.verticalHeader().setVisible(False)

        #插入数据
        for k in range(num):
            for i in self.curs:
                for j in range(8):
                    font = QtGui.QFont()
                    font.setFamily("幼圆")
                    font.setPointSize(10)
                    item = QTableWidgetItem(str(i[j]))
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setFont(font)
                    self.tableWidget.setItem(k,j,item)
                break
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.HorSectionClicked)#表头单击信号

    def HorSectionClicked(self):#点击表头则进行降序排列
        year = self.comboBox.currentText()
        category = self.comboBox_2.currentText()
        actor = self.lineEdit.text()
        if year == '所有年份': 
            if category == '所有分类':
                self.sqlstring = 'SELECT * FROM qinwenrui.dianying where `演员` like' + '\'%'+actor+'%\''+'and `票房` order by `票房` DESC'
            else:
                self.sqlstring = 'SELECT * FROM qinwenrui.dianying where `演员` like' + '\'%'+actor+'%\''+'and `题材` = '+ '\''+category.replace(' ','')+'\''+'and `票房` order by `票房` DESC'
        elif category == '所有分类':
            if year == '所有年份':
                self.sqlstring = 'SELECT * FROM qinwenrui.dianying where `演员` like' + '\'%'+actor+'%\''+'and `票房` order by `票房` DESC'
            else:
                self.sqlstring = 'SELECT * FROM qinwenrui.dianying where `演员` like' + '\'%'+actor+'%\''+'and `年份` = '+ '\''+ year.replace(' ','')+'\''+'and `票房` order by `票房` DESC'
        else:
            self.sqlstring = 'SELECT * FROM qinwenrui.dianying where `演员` like' + '\'%'+actor+'%\''+'and `年份` = '+ '\''+ year.replace(' ','')+'\''+'and `题材` = ' +'\''+category.replace(' ','')+'\''+'and `票房` order by `票房` DESC'

        c = self.curs.execute(self.sqlstring)
        num = c#返回的数据长度

        self.tableWidget.setRowCount(c)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)

        #插入数据
        for k in range(num):
            for i in self.curs:
                for j in range(8):
                    font = QtGui.QFont()
                    font.setFamily("幼圆")
                    font.setPointSize(10)
                    item = QTableWidgetItem(str(i[j]))
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setFont(font)
                    self.tableWidget.setItem(k,j,item)
                break