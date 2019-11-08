#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python exception:
    对代码中的异常情况，进行捕获处理。
    python异常处理机制，用异常对象表示异常情况
"""


#  try...except
try:
    x, y = 1, 0
    # 可能产生异常的代码
    print("x/y:", x / y)
except ZeroDivisionError as e:  # 捕获异常
    # 异常处理
    print("Error: ", e)


# 程序产生的异常被捕获，不会终止。继续执行后续代码
print("single except.")


# 多个except 子句 - 处理可能产生多个异常的代码
# 最多只有一个except分支会被执行
try:
    x, y = 1, 0
    print(x / y)  # 第一个异常被捕获，进入到对应的异常处理子句，然后退出异常处理，不会再执行其他异常处理
    # 上面代码已经触发异常，下面可能产生异常的代码不会再被执行
    a, b = 1, 'd'
    print(a / b)
except ZeroDivisionError as e:  # 处理 ZeroDivisionError 异常
    print("ZeroDivisionError: ", e)
except TypeError as e:  # 处理 TypeError 异常
    print("TypeError: ", e)


print("muti except")


# 捕获未知异常 - 捕获某些难以预料的异常
"""
BaseException - 所有异常类的父类
Exception - 大部分异常类的父类
"""
try:
    x = 's'
    y = 5
    print(x / y)
except ZeroDivisionError as e:  # 捕获 ZeroDivisionError 异常
    print("ZeroDivisionError: ", e)
except TypeError as e:  # 捕获 TypeError 异常
    print("TypeError: ", e)
except BaseException as e:  # 捕获其他未知异常,作为最后一个 except 子句
    print("BaseException: ", e)

print("unexpected exception.")


# else 子句 - 位于except子句后面，当没有异常发生时，自动执行else子句
try:
    x, y = 10, 3
    print(x / y)
except ZeroDivisionError as e:
    print("ZeroDivisionError: ", e)
except TypeError as e:
    print("TypeError: ", e)
except BaseException as e:
    print("BaseException: ", e)
else:  # try中没有异常时，执行
    print("no error!")

print("hello world~")


# finally 子句 - 不管有没有发生异常都会被执行
# except
try:
    x = 1 / 0
    print(x)
except ZeroDivisionError as e:
    print("{}".format(e))
    # raise e  # 抛出异常，不拦截
finally:  # finally子句执行后，抛出异常，程序终止
    print('end')


# no except
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError: ", e)
finally:  # 捕获了异常，finally 子句也执行
    print('end')


# 使用 raise 手动引发异常
try:
    x, y = 1, 0
    print(x / y)
except ZeroDivisionError as e:
    print("ZeroDivisionError: ", e)
    # raise  # 不带参数时，将当前错误原样抛出
else:
    print("no error!")
finally:
    print('end')


# 创建异常类，抛出自定义的异常
# 自定义异常类，从 Exception 类继承
class SomeErr(Exception):
    """自定义异常类"""

    pass


try:
    x, y = 1, 0
    print(x / y)
except BaseException as e:
    print("BaseException: ", e)
    raise SomeErr('invalid value')  # 抛出自定义异常
else:
    print("no error!")
