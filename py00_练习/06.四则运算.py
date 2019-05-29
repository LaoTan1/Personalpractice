# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
_author_ = '谭华锦'

import random


class MyMath:
    # def __init__(self, sum):
    #     self.sum = sum

    def addition(self):
        (x, y) = myrandom()
        print('x + y =')
        return x + y

    def subtraction(self0):
        (x, y) = myrandom()
        print('x - y =')
        return x - y

    def multiplicative(self):
        (x, y) = myrandom()
        print('x * y =')
        return x * y

    def division(self):
        (x, y) = myrandom()
        print('x / y =')
        return x / y


def myrandom():
    x = random.randing()
    y = random.randing()
    return x, y


class MyMess:
    def __init__(self, i):
        i = random.randing(1, 3)
        self.i = i

    def correct(self):
        if self.i == 1:
            print("--correct.不错哦，继续努力！")
        elif self.i == 2:
            print("--correct.非常好！")
        else:
            print("--correct.很好，答案正确!")

    def error(self):
        if self.i == 1:
            print("--error.静一静，再想想！")
        elif self.i == 2:
            print("--error.继续努力！")
        else:
            print("--error.加油，你可以的！")


def main():
    run = MyMath()
    print('*' * 30)
    print("开始测试:本测试有十道题，每道题你有三次机会作答\n")
    for i in range(1, 4):
        sum = int(input())
