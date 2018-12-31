#环境配置
将“python所需要的库”文件夹中的文件夹放入python的lib的site-packages的文件夹中。

# 完成的基本功能

# 爬虫系统
功能：

创建数据库
爬取58921电影网的电影信息，包括电影名、票房、导演、演员、上映年份、上映月份、上映季度
创建可视化信息


##实现方法：

###创建mysql数据库及表格
1.先运行creat_sql.py文件，将pymysql.connect()里的user和password分别改为自己数据库的用户名和密码
2.运行creat_table.py，将pymysql.connect()里的user和password分别改为自己数据库的用户名和密码

###爬取数据
运行crawler.py文件,将pymysql.connect()里的user和password分别改为自己数据库的用户名和密码


# 软件部分 
##环境配置
在mysql workbench导入“数据库文件“文件夹中的sql文件，并将自己数据库的用户名和密码分别改为root和714511,或者在每个文件夹中的pymysql.connect()函数中将user和password参数分别改为'root'和'714511'

##完成的基本功能
具有UI界面

登录功能：UI文件夹里的login.py的98行的check函数
注册功能及验错功能：UI文件夹里的register.py的88行的Register函数

可视化功能，包括：电影词云、劳模、月度题材占比、季度题材占比、票房趋势变化
电影词云：cloud.py的122行
劳模：roleactor.py的114行
月度题材占比：month.py的138行
季度题材占比：quater.py的121行
票房趋势变化：boxchange.py的150行

生成报表功能：movie_data.py的199行

##附加功能
查找电影信息，显示电影信息：movie_data.py的276行的findinfo函数
根据标签进行搜索，标签包括电影分类、电影上映年份、演员：：movie_data的276行的findinfo函数
对电影的票房进行排序：movie_data.py的HorSectionClicked函数

##实现方法
运行UI文件夹中的main.py文件
可视化文件保存在UI文件夹的graph文件夹中
报表文件保存在UI文件夹的table文件夹中