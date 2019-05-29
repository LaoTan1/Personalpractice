# !/usr/bin/eny python3
# - * -coning: utf-8 -*-
_author_ = '谭华锦'

# 列表list
names = ['tam', 'jack', 'mike']
print(names)
print(type(names))

# 获取元素
print(names[1])
print(names[:3])

# 追加元素
names.append('tan')

# 插入元素
names.insert(3, 'hua')

# 删除元素
names.remove('tam')
print(names)

# 弹出元素
print(names.pop(0))

# 获取元素个数
print(len(names))
print(names.count('tom'))  # 统计元素个数
print('-' * 40)

# 元组，初始后不能再改
nums = (2, 3, 4, 5, 54, 43)

print(nums[3], nums[-1])
print(nums[1:5])

'''不能
nums[0]=21
print(nums)
'''

'''
a=nums[0]
b=nums[1]
c=nums[2]
d=nums[3]
e=nums[4]
f=nums[5]
'''
a, b, c, d, e, f = nums
print(a, b, c, d, e, f)
