# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = '谭华锦'


class Animal(object):
    def __hi(self):
        print('hi')

    def run(self):
        print('--跑--')

    def eat(self):
        print('--吃--')


class Dog(Animal):
    def call(self):
        print('--旺旺-')


class shuaotq(Dog):
    def a(self):
        self.call()
        super().call()


d = shuaotq()
d.a()
d.call()
d.run()

