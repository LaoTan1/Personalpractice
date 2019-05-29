# !/usr/bin/eny python3
# - * -coning: utf-8 -*-
_author_ = '谭华锦'

# 键—值（key—value）
# 定义字典
score = {'tom': 98, 'jack': 100, 'alice': 88}
print(score)
print(type(score))

# 获取
print(score['jack'])
print(score.get('alice'))

# 添加
score['lucy'] = 90
score['tom'] = 78
print(score)

# 删除
score.pop('tom')
print(score)

# 判断元素是否在指定的key
print('tom' in score)

print(score)

# 遍历
print(score.keys())
print(score.values())
print(score.items())

# 输出
for k in score.keys():
    print(k, score[k])
print('-' * 40)

for v in score.values():
    print(v)
print('-' * 40)

for k, v in score.items():
    print(k, v)

# -----集合
# 定义set,使用大括号{}
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 9}
print(type(s))
l = [1, 2, 3, 4, 6, 47, 6, 23, 231, 3]
print(s)
s = set(l)  # 调用set函数将list转化为set,来实现去除重复元素
print(s)

# 增加
l.app(2)

# 删除
l.remove(321)

print(l)
