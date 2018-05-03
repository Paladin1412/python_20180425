#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/5/2 20:06
# @Author : merlinhuang
# @File   : hello.py
# Python模块的标准文件模板


# 一个字符串，表示文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
"""a test module"""

# 内置变量把作者写进去
__author__ = "merlinhuang"

import sys

def test():
    """test module"""
    # sys模块的argv属性用list存储了命令行的所有参数
    # argv至少有一个元素，第一个参数是.py文件的名称
    args = sys.argv
    if len(args) == 1:
        print("Hello world!")
    elif len(args) == 2:
        print("Hello, %s!" % args[1])
    else:
        print("Too many arguments!")

# 直接运行该文件时, Python解释器把一个特殊变量__name__置为__main__
# 在其他地方导入该模块时,if为False
if __name__ == "__main__":
    test()

