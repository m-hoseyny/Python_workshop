# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 23:24:14 2018

@author: microsoft
"""

import urllib.request  as urllib2 
from bs4 import BeautifulSoup

url = 'https://www.isna.ir/service/Economy'

page = urllib2.urlopen(url)
soup = BeautifulSoup(page)
soup_pretty = soup.prettify()

div_itemlist = soup.find_all('div', id = 'itemlist')
section_box6 = soup.find_all('section', id = 'box6')
list_of_news = section_box6.find_all('li')
news = soup.body.main.div.div.div.div.find




