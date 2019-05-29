# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.sina.com.cn/china/')
res.encoding = 'utf-8'
print(res.text, 'html.parser')
