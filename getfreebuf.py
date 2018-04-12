# -*- coding: utf-8 -*-
'''
Create on 2018-3-22
@author:niuniuniuniuniu
Project:freebuf 情报收集
'''
import re
import os
import sys
import requests
from bs4 import BeautifulSoup as bsp
reload(sys)
sys.setdefaultencoding('utf8') 
title=[]
url1=[]
dict={}
result={}
file=open('F:\\python\\freebuf\\a.html','w')
def get_message():
    url="http://www.freebuf.com"
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0"}
    res=requests.get(url,headers=header)
    soup=bsp(res.text,"html.parser")
    a=soup.find_all('div',class_="news-img")
    
    for i in a:
        url1.append(i.a['href'])
        title.append(i.img['title'])
    for i in range(len(title)):
        dic={title[i]:url1[i]}
        dict.update(dic)
    #word=re.compile(u'\u62db\u8058|\u62db|\u62db\u4eba|\u8df3\u69fd|\u5b9e\u4e60|\u6316\u4eba|\u8bda\u62db')
    word=re.compile(u'招聘|诚聘|招人|招|聘|实习生|挖人')
    for key in dict:
        match=word.search(key)
        if match:
            pass
        else:
            dic={key:dict[key]}
            result.update(dic)
    for key in result:
        file.write('<a href=')
        file.write('"')
        file.write(result[key])
        file.write('">')
        file.write(key)
        file.write('</a>')
        file.write('<br>')
        
        
    file.close()
        

            
if __name__=='__main__':
    get_message()
    
