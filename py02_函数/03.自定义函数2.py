# !/usr/bin/eny python3
# - * -coning: utf-8 -*-
_author_ = '谭华锦'


# 空函数
def empty():
    pass  # 使用pass


# 函数的返回值
def f1():
    name = 'tanhuajian'
    age = 20
    sex = 'male'
    return name, age, sex


# print(f1()) #返回值是一个tuple
a, b, c = f1()
print(a, b, c)


# 递归函数
def cale(x, y):
    # 常规方法
    '''
   if y==0:
        return 1
   sum = x
   for i in range(y - 1):
       sum *= x
   return sum
   '''


    if y == 0:
        return 1
    else:
         return x * cale(x, y-1)

print(cale(2, 4))
