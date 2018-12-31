import pymysql
import pandas as pd
import string
import numpy as np
from pyecharts import Line

import pyecharts

pyecharts.configure(
    jshost=None,
    echarts_template_dir=None,
    force_js_embed=None,
    output_image=None,
    global_theme=None
)
conn = pymysql.connect(
	host = '127.0.0.1',
	user = 'root',
	passwd = '714511',
	db = 'qinwenrui',
	port = 3306,
	charset = 'utf8mb4'
	)

year1 = 2015
year2 = 2016
year3 = 2017


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
# line = pyecharts.setOption({
# 			    "title": [
# 			        {
# 			            "text": "\u7535\u5f71\u7968\u623f\u53d8\u5316\u8d8b\u52bf",
# 			            "left": "auto",
# 			            "top": "auto",
# 			            "textStyle": {
# 			                "fontSize": 18
# 			            },
# 			            "subtextStyle": {
# 			                "fontSize": 12
# 			            }
# 			        }
# 			    ],
# 			    "toolbox": {
# 			        "show": true,
# 			        "orient": "vertical",
# 			        "left": "95%",
# 			        "top": "center",
# 			        "feature": {
# 			            "saveAsImage": {
# 			                "show": true,
# 			                "title": "save as image"
# 			            },
# 			            "restore": {
# 			                "show": true,
# 			                "title": "restore"
# 			            },
# 			            "dataView": {
# 			                "show": true,
# 			                "title": "data view"
# 			            }
# 			        }
# 			    },
# 			    "series_id": 4541527,
# 			    "tooltip": {},
# 			    "series": [],
# 			    "legend": [
# 			        {
# 			            "data": []
# 			        }w
# 			    ],
# 			    "animation": false
# 			})


line = Line('哈哈')
line._option['animation']= False
line.print_echarts_options()
line.add('{}年'.format(year1),attr,v1,is_lable_show=True)
line.add('{}年'.format(year2),attr,v2,is_lable_show=True)
line.add('{}年'.format(year3),attr,v3,is_lable_show=True)
line.render('每年每月票房变化趋势.html')