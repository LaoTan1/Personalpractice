# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
_author_ = '谭华锦'

# try:
#     f = open('hi', encoding='utf-8')
#     print(f.read())
# except FileNotFoundError as e:
#     print('找不到该文件', e)
# finally:
#     if f:
#         f.close()

# 使用with.....as语句，会自动调用close()
# with open('hi', encoding='utf-8') as f:
#     # print(f.read())
#     # print(f.read(5))
#     print(f.readline().strip())
#     print(f.readline())

# ——写文件
with open('hi', mode='a', encoding='utf-8') as f:
    f.write('你好！')

# ——读二进制文件
with open('p.png', mode='rb') as f:
    with open('hi.png', mode='wb') as out:
        out.write(f.read())
        print('拷贝成功')
