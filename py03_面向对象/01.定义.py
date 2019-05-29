# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
_author_ = '谭华锦'


# 定义一个类，使用class关键字
class Student:
    # pass
    # 类属性
    hobby = '哈哈'

    # 实例方法,将self作为第一个参数的方法
    def say_hi(self):
        print('hi' + ' ' + self.name)
        print(self.id)

    def say_hello(self, usename='无名氏'):
        print('hello' + ' ' + usename)

    # 类方法：使用@classmethod，将cls作为第一个参数
    @classmethod
    def shoew(cls, msg):  # cls表示当前的类
        print(msg, cls.hoppy)


# 创建类的对象
stu1 = Student()
stu2 = Student()
print(type(stu1))

# 为对象绑定属性
stu1.name = 'tom'  # 实例属性
stu1.age = 20
stu1.id = 2018
stu2.name = 'tan'
stu2.age = 22
stu2.id = 2019

print(stu1.name, stu1.age)

# 访问实例方法
stu1.say_hi()
stu2.say_hi()
stu1.say_hello()
print('*' * 80)

# 访问类属性
print(Student.hobby)
stu1.hobby = 'enen'
print(stu1.hobby)
print(Student.hoppy)
