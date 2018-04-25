#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/4/15 18:20
# @Author : Merlinhuang
# @File   : higher_order_function.py


# 自定义一个高阶函数

def add(x, y, func):
    """
    :param x: int
    :param y: int
    :param func: function:abs()
    :return: int
    """
    return func(x) + func(y)


factor = add(5, -6, abs)
print(factor)


# map(function, Iterable)

def f(x):
    return x * x


# 把函数副作用到每一个元素上
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)
print(list(r))

strings = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(strings))

# reduce()

from functools import reduce


def add(x, y):
    return x + y


# reduce
"""

add(1, 3)  --> 4
add(4, 5)  --> 9
add(9, 7)  --> 16
add(16, 9) --> 25
"""
sum = reduce(add, [1, 3, 5, 7, 9])
print(sum)


# 把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：

def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


# str 2 int with reduce() and map()

def char2num(s):
    digits = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    return digits[s]


print(reduce(fn, map(char2num, '13579')))

reduce(lambda x, y: x * 10 + y, map(char2num, '2468'))


# filter
def is_odd(n):
    return n % 2 == 1


odd = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(odd))

# sorted()

print(sorted([12, 34, -3, 45, 66, 47]))

# key 指定的函数作用于每一个元素上，根据key返回的结果进行排序
print(sorted([12, -15, -3, 45, 66, 47], key=abs))
#
# list = [12, -15, -3, 45, 66, 47]
# keys = [12, 15, 3, 45, 66 47]
#
# keys排序结果 --> [3, 12, 15, 45, 47, 66]
#                  |   |   |   |  |   |
# 最终结果     --> [-3, 12, -15, 45, 47, 66]


m = dict(a=1, c=10, b=20, d=15)
print(m)
# 默认key排序
print(sorted(m))

print(dict(sorted(m.items())))
# 向key传入匿名函数，取可迭代对象的指定元素

# 取字典的value, 作用于每一个可迭代对象
# print(sorted(m.items(), key=lambda elem: elem[1]))
sorted_m = sorted(m.items(), key=lambda elem: elem[1])
print(dict(sorted_m))

# 取字典的key, 作用于每一个可迭代对象
# print(sorted(m.items(), key=lambda elem: elem[0]))
sorted_m = sorted(m.items(), key=lambda elem: elem[0])
print(dict(sorted_m))


