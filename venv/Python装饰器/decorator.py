#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/4/17 21:54
# @Author : merlinhuang
# @File   : decorator.py

# 定义装饰器
def log(fun):
    def wrapper():
        print("####start####")
        # return fun()
        fun()
        print("####end####")
    # 返回是一个新的函数对象
    return wrapper

@log
def hi():
    print("hello world!")

hi()
# a = hi
# a()



def logged(func):
    def wrapper(*args, **kw):
        print("call {0}:".format(func.__name__))
        return func(*args, **kw)
    return wrapper


@logged
def now():
    print("2018-04-18")

now()
# 被装饰器修饰后函数属性变了
print(now.__name__)



