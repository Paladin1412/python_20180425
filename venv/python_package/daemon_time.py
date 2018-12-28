#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/11/8 21:31
# @Author : merlinhuang
# @File   : daemon_time.py

"""
time模块目前只支持到2038年前。如果需要处理范围之外的日期，请使用datetime模块
"""
import time


###　结构化时间 struct_time

# 使用time.localtime()等方法可以获得一个结构化时间元组.
print(type(time.localtime()))
#time.struct_time(tm_year=2018, tm_mon=11, tm_mday=8, tm_hour=21, tm_min=34, tm_sec=17, tm_wday=3, tm_yday=312, tm_isdst=0)
# 获取时间元组的元素值
local_time = time.localtime()
print(local_time)
print("This year is {0}, please keep learing!".format(local_time[0]))
# 切片
print(local_time[2:5])
# 获取对应的属性值 struct_time.xxx
print("Today is the {0}th day of the year.".format(local_time.tm_yday))

# time 是不可变类型，所有时间只读，不可更改
# local_time.tm_year = 2017


### 格式化时间字符串 string_time

# 利用time.strftime('%Y-%m-%d %H:%M:%S')等方法可以获得一个格式化时间字符串
# % 起控制作用
string_time = time.strftime("%y-%m-%d %H:%M:%S")
string_time = time.strftime("%B %y-%m-%d %H:%M:%S")
string_time = time.strftime("%c")
string_time = time.strftime("%d")
string_time = time.strftime("%I")
string_time = time.strftime("%j")
string_time = time.strftime("%p")
string_time = time.strftime("%p")
string_time = time.strftime("%U")
string_time = time.strftime("%w")
string_time = time.strftime("%W")
string_time = time.strftime("%x")
string_time = time.strftime("%X")
string_time = time.strftime("%y")
string_time = time.strftime("%Y")
string_time = time.strftime("%z")
string_time = time.strftime("%Z").encode("utf-8")
string_time = time.strftime("%%")
# string_time = time.strftime("%f")
print(string_time)
