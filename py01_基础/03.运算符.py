# !/usr/bin/eny python3
# - * -coning: utf-8 -*-
_author_ = '谭华锦'

# 算术运算符 + - * % / // **
print(5 + 2)
print(4 - 43)
print(30 * '******')  # 支持字符运算
print(5 / 45)
print(4 % 3)
print(3 // 4)  # 取整
print(2 ** 3)  # 幂
print(pow(2, 4))  # 幂

# 比较运算符 >,<,=,<=,>=，==，!=,
j = 5
print(j > 8)
print(10 > j > 4)
print('abc' > 'acd')  # 支持字符的比较

# 赋值运算符
a = 5
a += 5  # 等于a=a+5
print(a)

# 逻辑运算符 and or not
print(True and False)
print(5 < 3 or 4 < 3)
print(not 5 > 4)

# 条件运算符，也称三目运算符
print('aaaa' if 6 > 4 else 'bbbb')

# 成员运算符 in, not in
c = [3, 32, 4, 45, 7, 8, 9, 3, 3]
d = 5
print(d in c)

# 身份运算符 is, is not
m = [1, 3, 5, 7]
n = [1, 3, 5, 7]
x = n
print(m is n)
print(x is n)
'''
is 和 == 的区别
'''
print(m == n)
