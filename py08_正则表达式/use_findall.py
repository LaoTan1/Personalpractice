# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

import re

content = 'one1two12Three123four1234'

p = re.compile(r'[a-z]+', re.I)
rest = p.findall(content)
print(rest)
