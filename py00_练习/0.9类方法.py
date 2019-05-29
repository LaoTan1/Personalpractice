# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = '谭华锦'


class Letter(object):
    sum = 0

    def __init__(self, name):
        self.name = name
        Letter.sum += 1


A = Letter('A')
B = Letter('B')
C = Letter('C')
print(Letter.sum)
print('*' * 30)


class Game(object):
    # 类属性
    sum = 0

    # 实例方法
    def __init__(self):
        # 实例属性
        self.name = 'Tom'

    # 类方法
    @classmethod
    def add_sum(cls):
        Game.sum = 100


    #静态方法
    @staticmethod
    def print_muss():
        print('  穿越火线v11.1')
        print('1.开始游戏')
        print('2.结束游戏')


game = Game()
# Game.add_sum()
game.add_sum()
print(Game.sum)
Game.print_muss()

