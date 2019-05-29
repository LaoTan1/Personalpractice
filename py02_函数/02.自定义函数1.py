# !/usr/bin/eny python3
# - * -coning: utf-8 -*-
_author_ = '谭华锦'

''''
def 函数名(形参)：
'''


# 定义函数
def calc(num1, num2):
    res = num1 + num2
    return res


print(calc(3, 5))  # 调用函数

# 参数类型检查
''''
def my_abs(x):
   if not isinstance(x, (int, float)):
    raise TypeError('参数类型不正确，只能为数值类型')

    if x>=0:
        return x
    else:
        return -x

print(my_abs(123))

print(help(my_abs))
'''


# 默认参数，即有默认值的参数
def my_pow(x, y=2):
    if y == 0:
        return 1
    res = x
    for i in range(y - 1):
        res *= x
        return res


print(my_pow(2, 9))
print(my_pow(5))


# 可变参数，使用*表示参数个数可变的
def my_sum(x, *y):
    print(x)
    print(y)


my_sum(3, 5, 35, 6, 67, 7, )

muns = [3, 345, 5, 645, 6, 34]
my_sum(3, *muns)


# 关键字参数，使用**，参数个数可变的
def f1(x, **y):
    print(x)
    print(y)


f1(32, a=3, b=2312)  # y字典
