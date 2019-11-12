#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
python debug
"""


# print()
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)  # 使用print()打印变量值，辅助排错
    return 10 / n


def main():
    foo('2')


main()


# assert
def boo(s):
    n = int(s)
    # 断言，条件为真，什么都不做；为假时，抛出 AssertionError，并包含错误信息,程序终止
    assert n != 0, 'n is zero!'
    return 10 / n


# boo('0')


import logging

# 设置日志级别，默认为WARNING
logging.basicConfig(level=logging.INFO)


def func(s):
    n = int(s)
    # 调用logging打印变量值，进行跟踪
    logging.info("n = %d " % n)
    return 10 / n


func("100")
