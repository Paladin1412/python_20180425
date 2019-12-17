#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/4/16 21:00
# @Author : merlinhuang
# @File   : kaoshi.py



j = 0
for i in range(3, 100, 3):
    if i % 5 == 0:
        break
    j += i
print(j)

for i in range(1, 100, 3):
    if i % 5 == 0:
        print(i, end=' ')
print()

m = {'a': 1, 'b': 2}
print(m.items())

s = 'Rome was not built in one day.'
print('t: {0}, blank: {1}'.format(s.count('t'), s.count(' ')))

import random
f = lambda n: 1 if n <= 2 else f(n - 1) + f(n - 2)
a = b = [1, 1000]
a.append(f(random.randint(a[0], a[1])))
print(a, end=' ')
b.append(f(random.randint(b[0], b[1])))
print(b)

j = 0
for i in range(1, 30, 3):
    if i % 5 == 0:
        continue
    j += i
print(j)

