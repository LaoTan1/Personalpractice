# !/usr/bin/eny python3
# - * -coning: utf-8 -*-
_author_ = '谭华锦'

# 将字符串转化类型
a = '25'
b = int(a)
print(type(a), type(b))
print(b)

# 字符串切片
name = 'tom cruise'
print(name[0])
print(name[-1])
print(name[0:3])
print(name[:9])
print(name[1:8:2])

name = 'tom cruise'
age = 20
height = 180.5
print('大家好，我是' + name + '身高：' + str(height) + '年龄：' + str(age))
print('大家好，我是%s,身高：%s年龄：%s' % (name, height, age))
print('当地时间：%d年-%02d月-%02d日' % (2019, 2, 6))
