#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/4/18 22:05
# @Author : merlinhuang
# @File   : decorator2.py
#
# def hello():
#     print("hello")
#
# def bar(func):
#     func()
#
# # 把函数作为参数传递给函数
# bar(hello)


# def log(func):
#     # 装饰体
#     def wrapper():
#         print("{0} is running".format(func.__name__))
#         # 执行被修饰函数
#         return func()
#     # 返回新的函数
#     return wrapper
#
#
# def hello():
#     print("hello")
#
# # 装饰器 log(hello) 返回的是函数对象wrapper, 这条语句相当于 hello = wrapper
# hello = log(hello)
# hello()




# def log(func):
#     # wrapper中指定参数
#     def wrapper(name):
#         print("{0} is running".format(func.__name__))
#         # 执行被修饰函数
#         # func执行时需要带上参数
#         return func(name)
#     # 返回新的函数
#     return wrapper
#
# @log
# # 被修饰的函数带参数
# def hello(name):
#     print("hello {0}".format(name))
#
# hello("python")


def log(func):
    # wrapper中指定可变参数
    def wrapper(*args):
        print("{0} is running".format(func.__name__))
        # 执行被修饰函数
        # 可变参数
        func(*args)
        print("byby!")
    # 返回新的函数
    return wrapper

@log
# 被修饰的函数带参数
def hello(name, baby, father):
    print("hello {0}, {1}, {2}".format(name, baby, father))

hello("python", "C++", "java")