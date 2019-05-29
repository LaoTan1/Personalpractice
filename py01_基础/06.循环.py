# !/usr/bin/eny python3
# - * -coning: utf-8 -*-
_author_ = '谭华锦'

# 循环两种 while, for in

# ---------while循环
# 计算1到100的和
i = 1
sum = 0
while i <= 100:
    sum += i
    if sum >= 1000:
        break
    i += 1
print(sum)

# ---------for.....in循环
names = ['tom', 'jack', 'alice']
for name in names:
    print(name, end=',')

print()
for i in range(1, 100, 2):
    print(i, sep='-', end=',')

# 用for....in计算1到100的和
print()
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# 练习
nums = ['tom', 'jack', 'tan']
for i in range(len(nums)):
    print(str(i) + ' ' + nums[i])

i = 0
while i < len(nums):
    print(str(i) + ' ' + nums[i])
    i += 1

for n in nums[1:]:
    print(n, end=',')

print()
a = [1, 2, 3, 4, 5, 7, 8, 9, 5, 3, 2, 2]
for n in a[1:]:
    if n % 2 == 1:
        continue
    print(n, end=',')
