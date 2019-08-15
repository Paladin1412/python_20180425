#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/4/18 22:05
# @Author : merlinhuang
# @File   : decorator2.py
#
r"""
装饰器：
    装饰器本质上是一个 Python 函数或类
    在不改变原函数定义的情况下，给现有的函数增加新的功能；
    装饰器相同于把函数进行了包装，返回一个新的函数对象；
    装饰器通过@符号进行使用；要借助Python的@语法，把decorator置于函数的定义处；
"""


# #把函数作为参数传递给函数
def hello():
    print("hello")


def bar(func):
    func()


bar(hello)


# #简单的装饰器
def log(func):
    # 装饰体
    def wrapper():
        print("{0} is running".format(func.__name__))
        # 执行被修饰函数
        return func()
    # 返回新的函数
    return wrapper


def hello():
    print("hello")


# 装饰器 log(hello) 返回的是函数对象wrapper, 这条语句相当于 hello = wrapper
hello = log(hello)
hello()


# #@语法糖
def log(func):
    # wrapper中指定参数
    def wrapper(name):
        print("{0} is running".format(func.__name__))
        # 执行被修饰函数
        # func执行时需要带上参数
        return func(name)
    # 返回新的函数
    return wrapper


@log  # @用来使用装饰器
# 被修饰的函数带参数
def hello(name):
    print("hello {0}".format(name))


hello("python")


# #被修饰函数带参数
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
def hello(name, baby, father):  # 被修饰的函数带参数
    print("hello {0}, {1}, {2}".format(name, baby, father))


hello("python", "C++", "java")


# 被修饰的函数中参数是关键字参数
def log(func):
    """被修饰函数具有可变参数、关键字参数"""
    # wrapper中指定可变参数,关键字参数
    def warapper(*args, **kwargs):
        print("{0} is running".format(func.__name__))
        func(*args, **kwargs)
        print("byby!")
    # 返回新函数
    return warapper


@log  # 等价于 hello = log(hello)
def hello(name, **describe):
    """
    :param name:
    :param describe:
    :return:
    """
    print("hello {0}".format(name))
    print(describe.items())


hello("merlin", age=25, high=180)


# #带参数的装饰器 @decorate(args)
def log(level):
    """
    带参数的装饰器，最外层做了一层封装
    log相当于带参数的闭包，它的参数被内部函数(装饰器)引用，返回一个新的函数(装饰器)
    """

    def decorate(func):
        """内层真正的装饰器"""
        def wrapper(*args, **kwargs):
            """装饰体"""
            if level == "warn":
                print("{0} is down.".format(func.__name__))
            if level == "debug":
                print("{0} is dead.".format(func.__name__))
            func(*args, **kwargs)
            print("{0} !!!".format(level))

        # 返回装饰体
        return wrapper

    # 返回最后封装的函数体
    return decorate  # 指向内层真正的装饰器


@log(level="warn")  # 等价于 hello = log(level="warn")(hello)
def hello(name, **describe):
    """被修饰函数"""
    print("hello {0}.".format(name))
    print(describe.items())


# hello = log(level="warn")(hello)  #  思想: 一层一层向层函数传递参数
hello("pony", age=18, addr="Beijing")


# #function.warps
"""
使用装饰器极大地复用了代码，但是他有一个缺点就是原函数的元信息不见了，比如函数的docstring、__name__、参数列表
"""


def logged(func):
    """"""
    def with_log(*args, **kwargs):
        """new doc message with decorate!"""
        print(func.__name__)
        func(*args, **kwargs)

    return with_log


@logged
def hello(name):
    """raw doc message!"""
    print("hello {0}.".format(name))


hello("merlin")
# 输出被装饰器修饰过的函数的属性
print(hello.__name__)  # with_log, hello被with_log取代
print(hello.__doc__)  # doc也是装饰后的新函数的


# 使用functools.wraps保留原函数的元信息
"""
wraps本身也是一个装饰器，它能把原函数的元信息拷贝到装饰器里面的 func 函数中，这使得装饰器里面的 func 函数也有和原函数 hello一样的元信息了。
"""

from functools import wraps


def logged(func):
    """"""
    # 使用@wraps保留原函数信息
    @wraps(func)
    def with_log(*args, **kwargs):
        """new doc message with decorate!"""
        print(func.__name__)
        func(*args, **kwargs)

    return with_log


@logged
def hello(name):
    """raw doc message!"""
    print("hello {0}".format(name))


hello("KB")
print(hello.__name__)  # 保留原函数名
print(hello.__doc__)  # 原函数的doc

