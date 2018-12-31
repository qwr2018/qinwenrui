from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from login import Ui_Form
import login
import info
import register
import movie_data
import roleactor
import cloud
import quater
import month
import boxchange
class MainWindow(QtWidgets.QMainWindow,Ui_Form,movie_data.Ui_Form):#首页模块
	def __init__(self,parent = None):
		super(MainWindow,self).__init__(parent)
		self.setupUi(self)
		self.userFile = "./user.txt"
		with open(self.userFile,'a') as f:
			f.write('')
		self.regui = reg()
		self.movie_data = moviedata()
		self.pushButton.clicked.connect(self.showreg)
		self.setWindowIcon(QIcon('douyin.png'))
	def showreg(self):
		self.regui.show()
	def showmoviedata(self):
		self.movie_data.show()
		self.close()


class reg(QtWidgets.QWidget,register.Ui_Form):#注册模块
	def __init__(self,parent = None):
		super(reg,self).__init__(parent)
		self.setupUi(self)
		self.setWindowTitle('注册')
		self.child = info()
		
class info(QtWidgets.QWidget,info.Ui_Form):
	def __init__(self,parent = None):
		super(info,self).__init__(parent)
		self.setupUi(self)

class moviedata(QtWidgets.QWidget,movie_data.Ui_Form):
	def __init__(self,parent = None):
		super(moviedata,self).__init__(parent)
		self.setupUi(self)
		self.setWindowTitle('电影数据')
		self.radioButton.clicked.connect(self.search)
		self.cld = cloud()
		self.rac = roleactor()
		self.box = boxchange()
		self.qua = quater()
		self.mon = month()
		self.pushButton.clicked.connect(self.cloud)
		self.pushButton_2.clicked.connect(self.roleactor)
		self.pushButton_3.clicked.connect(self.boxchange)
		self.pushButton_4.clicked.connect(self.quater)
		self.pushButton_5.clicked.connect(self.month)
	def search(self):
		self.findinfo()

	def cloud(self):
		self.cld.show()

	def roleactor(self):
		self.rac.show()

	def boxchange(self):
		self.box.show()

	def quater(self):
		self.qua.show()

	def month(self):
		self.mon.show()

class cloud(QtWidgets.QWidget,cloud.Ui_Form):
	def __init__(self,parent = None):
		super(cloud,self).__init__(parent)
		self.setupUi(self)

class roleactor(QtWidgets.QWidget,roleactor.Ui_Form):
	def __init__(self,parent = None):
		super(roleactor,self).__init__(parent)
		self.setupUi(self)

class boxchange(QtWidgets.QWidget,boxchange.Ui_Form):
	def __init__(self,parent = None):
		super(boxchange,self).__init__(parent)
		self.setupUi(self)	

class quater(QtWidgets.QWidget,quater.Ui_Form):
	def __init__(self,parent = None):
		super(quater,self).__init__(parent)
		self.setupUi(self)	

class month(QtWidgets.QWidget,month.Ui_Form):
	def __init__(self,parent = None):
		super(month,self).__init__(parent)
		self.setupUi(self)	

if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())