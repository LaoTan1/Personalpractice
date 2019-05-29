# !/usr/bin/eny python3
# - * -coning: utf-8 -*-
_author_ = '谭华锦'

# 查看函数的帮助信息
help(print)
help(abs)

# 数学运算
print(abs(-5))
a = (21, 43, 54, 56, 6, 87, 9, 560)
print(max(a))
print(max(21, 43, 54, 56, 6, 87, 9, 560))

# 类型转化
print(int('123'))
print(str(123))
print(float('13.4'))
print(bool(9))

# 判断数据类型
a = 'abc'
print(type(a))
print(isinstance(a, int) or isinstance(a, float))
