import pymysql

db = pymysql.connect(host='127.0.0.1', user='root', password='714511', port=3306, db='qqq')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS dianying (名字 VARCHAR(255) NOT NULL, 票房 BIGINT NOT NULL, 导演 VARCHAR(255) NOT NULL, 演员 VARCHAR(255) NOT NULL, 题材 VARCHAR(255) NOT NULL, 年份 VARCHAR(255) NOT NULL, 季度 INT NOT NULL, 月份 INT NOT NULL, PRIMARY KEY (名字))'
cursor.execute(sql)
db.close()
