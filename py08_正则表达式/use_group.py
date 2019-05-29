# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

import re


def test_grout():
    content = 'hello, world!'
    p = re.compile(r'world')
    rest = p.search(content)
    print(rest)
    if rest:
        # group的使用
        print(rest.group())
        # groups的使用
        print(rest.groups())


def test_id_card():
    """身份证的正则匹配"""
    # p = re.compile(r'^(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)$')
    p = re.compile(r'^(\d{6})(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})(\d{3})([0-9]|X)$')

    id1 = '440883199807212244'
    id2 = '44088319980721224x'
    rest1 = p.search(id1)
    print(rest1.group(1))
    print(rest1.groups())
    print(rest1.groupdict())


if __name__ == '__main__':
    test_grout()
    test_id_card()
