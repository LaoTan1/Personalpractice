# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = '谭华锦'


class Dog(object):

    def __init__(self):
        print('__init__')

    def __del__(self):
        print('__del__')

    def __str__(self):
        print('__str__')
        return 'hi'

    def __new__(cls):
        print('__new__')
        return object.__new__(cls)


dog = Dog()
