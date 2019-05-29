# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

import re

pattern = re.compile(r'hello', re.I)
print(dir(pattern))

rest = pattern.match('Hello, world')
print(rest)
print(dir(rest))
