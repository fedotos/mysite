#!/usr/bin/python
# coding=UTF-8
__author__ = 'fdts'

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from urllib.parse import urlencode

SITE1 = "http://sharik.cv.ua/index.php"
SITE2 = "http://freebookspot.es/"
SITE3 = "http://sharik.cv.ua/page1.php"

try:
    html = urlopen(SITE1)
except HTTPError as e:
    print(e)
    exit()
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

encoding='utf-8'
url = 'https://www.kinopoisk.ru/user/2007910/votes/list/ord/year/#list' # url для второй страницы
r = urlopen(url)
print("*************************")
print(r.info())
print("*************************")
bsobj1 = BeautifulSoup(r.read(), "html.parser")
print(bsobj1.head)
print(bsobj1.body)
# with open('test.html', 'w') as output_file:
#  output_file.write(r.text.encode('cp1251'))