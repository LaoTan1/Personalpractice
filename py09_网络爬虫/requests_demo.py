# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

import requests
from bs4 import BeautifulSoup

# def getHTTPText(url):
#     try:
#         r = requests.get(url, timeout=1)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "产生异常"
#
#
# # head()方法
# def gethead():
#     r = requests.head("http://www.baidu.com")
#     headers = r.headers
#     print(headers)
#
# def data_demo():
#     r = requests.request("POST","http://www.baidu.com",data="你好！")
#     print(r.text)
#
# if __name__ == "__main__":
#     # url = "http://www.imooc.com"
#     # print(getHTTPText(url))
#     # gethead()
#     data_demo()

url = "http://www.baidu.com"
r = requests.get(url)
print(r.text)
demo=r.text
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())
