# !/usr/bin/eny python3
# - * -coning: utf-8 -*-
_author_ = '谭华锦'

# 方法1
# import py04_模块.mymodule
# print(py04_模块.mymodule.minus(3, 4))
# print(py04_模块.mymodule.a)

# import py04_模块.mymodule as m
# print(m.a)

# 方法2
# from py04_模块 import mymodule
# print(mymodule.a)
# print(mymodule.plus(3,5))

from py04_模块.mymodule import b, plus

print(b)
print(plus(2, 4))
