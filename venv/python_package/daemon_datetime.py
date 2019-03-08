#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2019/2/13 15:38
# @Author : merlinhuang
# @File   : daemon_datetime.py


from datetime import date, timedelta
import time


# datetime 模块
"""
dataetime主要定义了以下几个类
datetime.date       日期类
datetime.time       时间类
datetime.datetime   日期与时间类
datetime.timedelta  表示两个date、time、datetime实例之间的时间差
datetime.tzinfo	    时区相关信息对象的抽象基类
datetime.timezone   python3.2中新增的功能，实现tzinfo抽象基类的类，表示与UTC的固定偏移量

使用datetime模块主要就是对其前四个类的操作.

datetime 模块中还定义了两个常量:
datetime.MINYEAR    datetime.date或datetime.datetime对象所允许的年份的最小值，该值为1
datetime.MAXYEAR    datetime.date或datetime.datetime对象所允许的年份的最大值，该值为9999

"""

### datetime.date 类

"""
定义：class datetime.date(year, month, day)
datetime模块下的日期类，只能处理年月日这种日期时间，不能处理时分秒。

在构造datetime.date对象的时候需要传递下面的参数：
    参数名称	取值范围
    year	[MINYEAR, MAXYEAR]
    month	[1, 12]
    day	    [1, 指定年份的月份中的天数]

主要属性和方法：    
"""
# date.max	        date对象所能表示的最大日期：9999-12-31
# 源码定义： date.max = datetime.date(9999, 12, 31)
print(type(date.max))
print(date.max)

# date.min	        date对象所能表示的最小日期：00001-01-01
# 源码定义：date.min = datetime.date(1, 1, 1)
print(type(date.min))
print(date.min)

# date.resoluation	date对象表示的日期的最小单位：天
# 源码定义：date.resolution = datetime.timedelta(days=1)
print(type(date.resolution))
print(date.resolution)
# 等价于 datetime.timedelta 类的一个实例
print(timedelta(days=1))  # 自定义__str__()实现

# 方法date.today()	    返回一个表示当前本地日期的date对象
print(type(date.today()))
# 当前本地日期的一个date对象
d = date.today()
print(d)
print(d.year)
print(d.month)
print(d.day)

# 方法date.fromtimestamp(timestamp)	根据给定的时间戳，返回一个date对象
date.fromtimestamp(time.time())
print(type(date.fromtimestamp(time.time())))
# 指定时间戳的一个date对象
d = date.fromtimestamp(3600)
print(d)
print(d.year)
print(d.month)
print(d.day)

# date.replace(year[, month[, day]])  生成并返回一个新的日期对象，原日期对象不变
print(type(d.replace(year=2018, month=8, day=8)))
print(d.replace(year=2018, month=8, day=8))
# 原日期对象不变test
print(d)
