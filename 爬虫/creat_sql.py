import pymysql

db = pymysql.connect(host='127.0.0.1', user='root', password='714511', port=3306)
cursor = db.cursor()
cursor.execute("CREATE DATABASE qinwenrui DEFAULT CHARACTER SET utf8mb4")
db.close()
