# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

import re

"""
使用sub进行替换
"""

s = 'one1two222three324four34231five34six34'
p = re.compile(r'\d+')
rest = p.sub('@', s)
print(rest)

# 换位置
s2 = 'hello world'
p2 = re.compile(r'(\w+) (\w+)')
rest = p2.sub(r'\2 \1', s2)
print(rest)

# 替换并改变内容
