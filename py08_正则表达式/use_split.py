# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

import re

"""
使用split正则分割字符
"""

s = 'one1two222three324four34231five34six34'
p = re.compile(r'\d+')
rest = p.split(s, 2)
print(rest)
