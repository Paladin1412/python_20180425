#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2019/8/19 9:56
# @Author : merlinhuang
# @File   : class_magic_method.py

"""
Python中一些特殊成员和魔发方法的介绍与使用
"""


# 1. __doc__ 说明性文档和信息，python自建，无需定义。

class Foo:
    """Test of __doc__, auto to be collected by python."""

    def func(self):
        pass


# 打印类的说明文档
print(Foo.__doc__)

