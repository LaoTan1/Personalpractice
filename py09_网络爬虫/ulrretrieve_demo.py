# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

import urllib.request

urllib.request.urlretrieve("http://ww.baidu.com", "D://\\爬虫练习\\demo.html")

urllib.request.urlcleanup()

temp = urllib.request.urlopen("http://ww.baidu.com")
print(temp.info())

# 200表示成功
print(temp.getcode())

print(temp.geturl())


#timeout,反应时间，超时设置
for i in range(1, 100):
    try:
        temp = urllib.request.urlopen("http://www.imooc.com", timeout=0.1)
        print(len(temp.read().decode("utf-8)")))
    except Exception as err:
        print("出现异常" + str(err))
