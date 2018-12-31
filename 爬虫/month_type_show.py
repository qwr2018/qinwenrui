import pymysql
import pandas as pd
import string
import numpy as np
from pyecharts import Pie


conn = pymysql.connect(
	host = '127.0.0.1',
	user = 'root',
	passwd = '714511',
	db = 'qinwenrui',
	port = 3306,
	charset = 'utf8mb4'
	)

year = 2018
month = 11


sql = 'SELECT * FROM `dianying`;'
df = pd.read_sql(sql,conn)
a = df[(df.年份==str(year))&(df.月份==month)]

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
# 	cnt.append(TYPE.loc[k])
# num = [cnt.count('犯罪'),cnt.count('喜剧'),cnt.count('剧情'),cnt.count('纪录片'),cnt.count('奇幻'),cnt.count('动作'),cnt.count('冒险'),cnt.count('悬疑'),cnt.count('动画'),cnt.count('战争'),cnt.count('家庭'),cnt.count('科幻'),cnt.count('历史')]
pie = Pie('{}年{}月题材票房占比'.format(year,month),title_pos ='center',width = 900,height = 620 )
pie.add('',tp,M,center = [50,50],radius = [0,60],is_label_show = True,legend_orient = 'vertical',legend_pos = 'left')
pie.render('月份题材分布.html')
print(TYPE)