# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
_author_ = '谭华锦'

import pymysql

config = {
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'password': '',
    'databass': 'python',
    'charset': 'utf8'
}
conn = pymysql.connect(**config)

cursor = conn.cursor()

sql = '''
    insert into t_user
    (username, password, age, height)
    valuse
    ('tom', '123',21,34)
'''
num = cursor.execute(sql)
print(num)
cursor.close()
conn.close()
