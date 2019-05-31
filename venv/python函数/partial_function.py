#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2019/5/21 9:34
# @Author : merlinhuang
# @File   : partial_function.py

"""
偏函数(Partial function)，在函数调用前，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

Python的 functools 模块提供了很多有用的功能，其中一个就是偏函数。
"""

import functools


r"""
在介绍函数参数的时候，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：
"""

# 用户自己创建函数，固定被调用函数的参数
def int2(x, base=2):
    """通过固定int()函数的参数base=2, 返回新的函数，简化int()的调用"""
    return int(x, base)


binarys = ['0001', '0010', '0100', '1000']
num = []
for b in binarys:
    # 调用固定参数的偏函数int2(),不用每次都给int()函数传入base=2
    num.append(int2(b))  # 将二进制b转换为十进制数
print(num)

r"""
借助 functools.partial 创建偏函数，不需要用户自定义函数实现 
简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

"""

# 借助functools.partial，把int()函数的参数 base 固定为2，返回一个新函数，调用新函数更简单
int2 = functools.partial(int, base=2)
print(int2('1000'))
print(int2('10001000'))
# 调用偏函数可以再次指定参数值
print(int2('1500', base=10))  # 10进制转换

# 创建偏函数可以接收的参数：函数对象、*args、**kw

int8 = functools.partial(int, base=8)  # **kw
print(int8('1234567'))
# 等价于
kw = {'base': 8}
print(int('1234567', **kw))

# 固定三个参数(10, 20, 15)
max2 = functools.partial(max, 10, 20, 15)  # *args
print(max2(1, 3, 5, 18))
# 会把固定的参数作为*args的一部分自动加到左边，等价于
args = (10, 20, 15, 1, 3, 5, 18)
print(max(*args))
