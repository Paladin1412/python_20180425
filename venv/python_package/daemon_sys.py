#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/5/15 22:22
# @Author : merlinhuang
# @File   : daemon_sys.py


"""
sys模块主要是针对与Python解释器相关的变量和方法
"""
import sys

# sys.argv 获取命令行参数列表，第一个参数是py程序本身文件名，列表索引为0

# 输出脚本名
print(sys.argv[0])


for index, argv in enumerate(sys.argv):
    print("sys[{0}] 第{0}个参数: {1}".format(index, argv))

# 退出python程序,exit(0)表示正常退出,参数非0时会引发一个SystemExit异常
# sys.exit(0),下面的不会执行
# print("Test exit")

# sys.version	获取Python解释程器的版本信息
print(sys.version)

# 最大 Int 值
print(sys.maxsize)
print(2 ** 31 - 1)

# python模块搜索路径
print(sys.path)

# 返回操作系统平台名称
print(sys.platform)

# 返回异常信息三元元组
print(sys.exc_info())

# 获取系统当前编码，默认为utf-8
print(sys.getdefaultencoding())

# 获取文件系统使用编码方式，默认是utf-8
print(sys.getfilesystemencoding())

# 以字典的形式返回所有当前Python环境中已经导入的模块
print(sys.modules)

# 返回一个列表，包含所有已经编译到Python解释器里的模块的名字
print(sys.builtin_module_names)

# 当前Python的版权信息
print(sys.copyright)

print(sys.getrefcount(sys))

print(sys.getwindowsversion())

def find_module(module):
    if module in sys.builtin_module_names:
        print(module, "内置于-->", "__builtin__")
    else:
        print(module, "模块位于-->", __import__(module).__file__)
find_module('os')
find_module('sys')
find_module('time')
find_module('zlib')
find_module('string')

# a = input("dd\n")
# s = input("Please input name!")
#
# print('Please input name!',)
# s = sys.stdin.readline()[:-1]

# 从控制台重定向到文件

# 备份标准输出
__console__ = sys.stdout

#  redirection start
f_handler = open('out.log', 'w')
# 把文件对象赋值给sys.stdout
sys.stdout = f_handler
# 输出到文件中
print("i am from stdout, to file.")

# redirection end
sys.stdout = __console__
# 输出到控制台
print("i am from stdout, to consple.")


import sys
import time


def bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    r = '\r[%s%s]%d%%' % ("="*num, " "*(100-num), rate_num, )
    sys.stdout.write(r)
    sys.stdout.flush()


if __name__ == '__main__':
    for i in range(0, 101):
        time.sleep(0.1)
        bar(i, 100)