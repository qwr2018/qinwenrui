import pymysql
import pandas as pd
import string
import numpy as np
from pyecharts import WordCloud

conn = pymysql.connect(
	host = '127.0.0.1',
	user = 'root',
	passwd = '714511',
	db = 'qinwenrui',
	port = 3306,
	charset = 'utf8mb4'
	)

year = 2018
rank = 4#输入

sql = 'SELECT * FROM `dianying`;'
df = pd.read_sql(sql,conn)

a = df[df.年份==str(year)]
a = a.sort_values('票房',ascending = False)
# print(a[:3].values[1][1])

name = []
v = []
for i in range(rank):
	name.append(a[:rank].values[i][0])
	v.append(a[:rank].values[i][1])
cloud = WordCloud(width = 900,height = 620,background_color='#12cf96')
cloud.add('',name,v,shape = 'star')
cloud.render('cloud.png')