#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2019/5/16 20:45
# @Author : merlinhuang
# @File   : closure.py
r"""
return function
closure,闭包
"""

def lazy_sum(*args):
    """返回函数"""
    def sum():
        an = 0
        for n in args:
            an = an + n
        return an
    # 返回函数
    return sum

# 不会立即执行
f = lazy_sum(1, 3, 5, 7, 9)
# 返回函数
print(f)
print(f.__class__)  # <class 'function'>
# 引用时，才执行
print(f())


def count():
    """闭包"""
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        # 把函数f追加进去
        fs.append(f)
    return fs


# 返回函数及其变量,不会立刻执行
f1, f2, f3 = count()
# 调用时执行，引用的内部变量i是3
print(f1(), f2(), f3())


def count():
    """"""
    def f(j):
        def g():
            return j * j
        # 返回内层函数
        return g
    fs = []
    for i in range(1, 4):
        # 利用f()的参数绑定循环变量i
        fs.append(f(i))  # 传参,f(i)立即被执行
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())
