# !/usr/bin/eny python3
# - * -coning: utf-8 -*-
_author_ = '谭华锦'

''''
变量的作用域scope:
1.全局作用域
    函数以外的区域都是全局作用域
    在全局作用域中定义的变量都是全局变量
2.函数作用域，也称为局部作用域
'''

a = 5  # 全局变量

if True:
    c = 5  # 全局变量


def fn():
    b = 5  # 局部变量


def fn1():
    x = 4

    def fn2():
        x = 3
        print(x)


print('*' * 80)


# global关键字
def fn2():
    # a=10
    global a  # 在函数中改变全局变量
    a = 10

    print('函数内部：a=', a)


fn2()

print('函数外部：a=', a)

'''
命名空间namespce 
'''
# locals() 获取当前作用域的命名空间
scope = locals()
print(scope)
print(type(scope))

print(scope['a'])
