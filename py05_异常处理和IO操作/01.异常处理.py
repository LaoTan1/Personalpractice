# !/usr/bin/eny python3
# - * -coning: utf-8 -*-
_author_ = '谭华锦'

# try:
#     print('try...........')
#     a = 5 / int('a')
# # except # 捕获特定异常
# # except ZeroDivisionError as e:
# except (ZeroDivisionError, ValueError) as e:
#     print('出现异常', e)
# else:
#     print('没有异常处理')
# finally:
#     print('finally........')
#
#
# # 自定义异常
#
# class UsernameExistsException(Exception):
#     pass
#
#
# def fn(username):
#     if username == 'Tom' or username == 'admin':
#         raise UsernameExistsException('该用户已存在')
#     else:
#         print('ok')
#
#
# fn(input('请输入用户名：'))

print('-' * 80)

try:
    open('1.py')
    print("没异常")

except NameError:
    print('有异常')

except Exception:
    print('上面没有捕获异常')
