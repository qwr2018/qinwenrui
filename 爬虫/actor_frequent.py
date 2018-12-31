import pymysql
import pandas as pd
import string
import numpy as np
from pyecharts import Bar

conn = pymysql.connect(
	host = '127.0.0.1',
	user = 'root',
	passwd = '714511',
	db = 'qinwenrui',
	port = 3306,
	charset = 'utf8mb4'
	)

year = 2018
rank = 10#输入

sql = 'SELECT * FROM `dianying`;'
df = pd.read_sql(sql,conn)


a = df[df.年份==str(year)]

# print(a[:3].values[0][3])
act = []
for i in range(len(a)):
	b = a.values[i][3].replace('比利时','').replace('俄罗斯','').replace('中国香港','').replace('韩国','').replace('爱情','').replace('日本','').replace('法国','').replace('英国','').replace('美国','').replace(',中国大陆','').replace('犯罪','').replace('喜剧','').replace('剧情','').replace('纪录片','').replace('奇幻','').replace('动作','').replace('冒险','').replace('悬疑','').replace('动画','').replace('战争','').replace('家庭','').replace('科幻','').replace('历史','').replace('惊悚','')[:10]
	act.append(b)
# c = []
# for j in act:
# 	actor = j.replace('比利时','').replace('俄罗斯','').replace('中国香港','').replace('韩国','').replace('爱情','').replace('日本','').replace('法国','').replace('英国','').replace('美国','').replace(',中国大陆','').replace('犯罪','').replace('喜剧','').replace('剧情','').replace('纪录片','').replace('奇幻','').replace('动作','').replace('冒险','').replace('悬疑','').replace('动画','').replace('战争','').replace('家庭','').replace('科幻','').replace('历史','').replace('惊悚','')
# 	c.append(actor)
l = ','.join(act)
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
# L = zip(dct.values(),dct.keys())[:rank]
L = sorted(dct.items(),key = lambda item:item[1],reverse = True)
L=L[:rank]#tuple类型
# sorted(L)
ACTOR = []
v = []
for p in range(rank):
	ACTOR.append(L[p][0])
	v.append(L[p][1])
print(ACTOR)
print(v)

bar = Bar('{}年劳模演员TOP{}'.format(year,rank),title_pos = 'center')
bar.use_theme("vintage")
bar.add('',ACTOR,v,is_label_show = 1,label_color = ['#C1232B','#B5C334','#FCCE10','#E87C25','#27727B'])
bar.render('劳模演员TOP.html')