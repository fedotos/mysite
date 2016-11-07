#!/usr/bin/python
# coding=UTF-8
__author__ = 'fdts'

from urllib.request import urlopen
from bs4 import BeautifulSoup

SITE1 = "http://sharik.cv.ua/index.php"
SITE2 = "http://freebookspot.es/"
SITE3 = "http://sharik.cv.ua/page1.php"

html = urlopen(SITE1)
bsobj = BeautifulSoup(html.read(),"html.parser")
print(html.geturl()) #из книги дронов
print(html.info())
print(html.code)
print(html.msg)
print("----------------------------------------------------------------------------")
# for line in html: print(line) #из книги дронова
# print(html.readline())
#print(bsobj)
print("----------------------------------------------------------------------------")
print(bsobj.head)
print(bsobj.div)
print(bsobj.title)

try:
    html1 = urlopen(SITE3)
except HTTPError as e:
    print(e)
    exit()
bsobj = BeautifulSoup(html1.read(),"html.parser")
print(bsobj.head)


