#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/4/15 20:56
# @Author : Merlinhuang
# @File   : generate_list.py


# 列表生成式
# [exp for val in collection if condition]

l1 = [x * x for x in range(10) if x * x % 2 == 0]
print(l1)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
l2 = [k + '=' + v for k, v in d.items()]
print(l2)


l1 = [x * x for x in range(10)]
print(l1)

# 生成器1  ()
g1 = (x * x for x in range(10))
print(g1)
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
for i in g1:
    print(i, end="")


print()

# 生成器2  yield

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)


for n in fib(6):
    print(n)

g = fib(6)
while 1:
    try:
        x = next(g)
        print('g', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
