# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = '谭华锦'


class Dog(object):
    def print_self(self):
        print('你好，我是***')


class Xiaotq(Dog):
    def print_self(self):
        print("Hello I'm ***")


def A(temp):
    temp.print_self()


dog1 = Dog()
dog2 = Xiaotq()

A(dog1)
A(dog2)


