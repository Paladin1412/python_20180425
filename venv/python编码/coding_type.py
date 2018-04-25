#!/usr/bin/env python
# *- coding: utf-8 -*-
# @Time   : 2018/4/4 15:49
# @Author : merlinhuang
# @File   : daemon2.py


# 指定以unicode形式存储
s = u"哈哈哈"
print(s)
print(type(s))


# 默认字符串存储
h = "哈哈哈"
print(h)
print(type(h))


#
# m = s.decode("utf-8")
# print(type(m))
# print(m)
#

l =  [1, "哈哈哈"]

print(l)       # 输出内存中表示形式
print(l[1])    # 输出字符串内容


s = "中文"
a = s.decode("utf-8")
a.encode("gbk")
print(a)
