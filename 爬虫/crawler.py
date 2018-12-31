import requests
from bs4 import BeautifulSoup
import re
import pymysql
def change_boxoffice(boxoffice):
    if boxoffice[-1] == '亿':
        boxoffice = float(boxoffice[:-1])*100000000
    elif boxoffice[-1] == '万':
        boxoffice = float(boxoffice[:-1])*10000
    else:
        return 0
    boxoffice = int(boxoffice)
    return boxoffice
# def change_quater(M):
#     quater = 0
#     if M <= 3:
#         quater = 1
#     elif 3<M<=6:
#         quater = 2  
#     elif 6<M<=9:
#         quater = 3
#     elif 9<M<=12:
#         quater = 4
#     return quater

def get_url(url):
    cookies = {'DIDA642a4585eb3d6e32fdaa37b44468fb6c':'3n9nrid0rvpotrhqa2voq4ll91','Hm_lpvt_e71d0b417f75981e161a94970becbb1b':'1544525148','Hm_lvt_e71d0b417f75981e161a94970becbb1b':'1544524448','remember':'UyLjExMTM4NC4xMDI4MTYuMA%3D%3D','time':'TU4LjExOTk1Mi4xMTM1MjYuMA%3D%3D'}

    r = requests.get(url,cookies = cookies)
    r.encoding = r.apparent_encoding
    return r.text

#获取页面地址
def get_page(text):
    soup = BeautifulSoup(text,'html.parser')
    # a = soup.find_all('a',attrs={'href':'/film/'+r"[\d]{4}"})
    a = soup.find_all('a')
    pagecodelst = []
    for i in a:
        try:
            href = i.attrs['href']
            b = re.search(r"/film/[\d]{4}",href)
            pagecodelst.append(b.group(0))
        except:
            continue    
    return pagecodelst

def get_info(url):
    dct = {}
    box_url ='http://58921.com'+url+'/boxoffice'
    b = get_url(box_url)
    box_soup = BeautifulSoup(b,'html.parser')
    c = box_soup.find('h3',attrs={'class':'panel-title'})
    boxoffice = c.text.split(' ')[1][:-1]
    boxoffice = change_boxoffice(boxoffice)

    # boxoffice = re.find(r"[\d].*?")
    url = 'http://58921.com'+url
    r = get_url(url)
    soup = BeautifulSoup(r,'html.parser')
    a = soup.find('title')
    name = a.text.split('-')[0]
    n = soup.find('ul',attrs={'class':"dl-horizontal content_view_fields content_view_film_fields"})
    member = n.find_all('a')
    director = member[1].text
    num = len(member)
    actor = ''
    for i in range(2,num-2):
        if i == 2:
            actor = member[i].text
        else:
            actor = actor+','+ member[i].text
    movie_type = member[-1].text
    t = re.search(r"[\d]{4}-[\d]{2}-[\d]{2}",n.text)
    time = t.group(0)
    year = time.split('-')[0]
    month = time.split('-')[1]
    M = int(month)
    if M <= 3:
        quater = 1
    elif 3<M<=6:
        quater = 2  
    elif 6<M<=9:
        quater = 3
    elif 9<M<=12:
        quater = 4
    dct['名字'] = name
    dct['票房'] = boxoffice
    dct['导演'] = director
    dct['演员'] = actor
    dct['题材'] = movie_type
    dct['年份'] = year
    dct['季度'] = quater
    dct['月份'] = month 

    return dct
   
     # for i in n.text:
    #     try:
    #         print(i)
    #     except:
    #         continue
# url = 'http://58921.com/film/6191'
# get_info(url)

def send_to_mysql(dct):
    table = 'dianying'
    keys = ','.join(dct.keys())
    values = ','.join(['%s']*len(dct))
    db = pymysql.connect(host = '127.0.0.1',user = 'root',password = '714511',port = 3306,db='qinwenrui')
    cursor = db.cursor()
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    try:
        if cursor.execute(sql, tuple(dct.values())):
            print("Successful")
            db.commit()
    except:
        print('Failed')
        db.rollback()
    db.close()

def main():
    urlist = ['http://58921.com/alltime/2018','http://58921.com/alltime/2017','http://58921.com/alltime/2016','http://58921.com/alltime/2015']
    # for i in range(4):
    for j in range(0,15):
        dct = {}
        url = urlist[3]+'?page='+str(j)
        u = get_url(url)
        page = get_page(u)
        for k in range(len(page)):
            try: 
                dct = get_info(page[k])
                print(dct)
                send_to_mysql(dct)
                num = num+1
            except:
                continue

main()