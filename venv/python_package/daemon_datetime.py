#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2019/2/13 15:38
# @Author : merlinhuang
# @File   : daemon_datetime.py


from datetime import date, timedelta, time, datetime, timezone

# datetime 模块
"""
datetime模块是包装了time模块的

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

# datetime.date 类
"""
定义：class datetime.date(year, month, day)
datetime模块下的日期类，只能处理年、月、日这种日期时间，不能处理时分秒。

在构造datetime.date对象的时候需要传递下面的参数：
    参数名称	取值范围
    year	[MINYEAR, MAXYEAR]
    month	[1, 12]
    day	    [1, 指定年份的月份中的天数]
"""
# 主要属性和方法
# datetime.date 实例
print(date(2018, 12, 12))  # __str__ = isoformat

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

# 方法 date.today()	    返回一个表示当前本地日期的date对象
print(type(date.today()))
# 当前本地日期的一个date对象
d = date.today()
print(d)
print(d.year)
print(d.month)
print(d.day)

# 方法 date.fromtimestamp(timestamp)	根据给定的时间戳，返回一个date对象
print(date.fromtimestamp(1688888))
print(type(date.fromtimestamp(1688888)))
# 指定时间戳的一个date对象
d = date.fromtimestamp(3600)
print(d)
print(d.year)
print(d.month)
print(d.day)

# 方法 date.replace(year[, month[, day]])  生成并返回一个新的日期对象，原日期对象不变
print(type(d.replace(year=2018, month=8, day=8)))
print(d.replace(year=2018, month=8, day=8))
# 原日期对象不变
print(d)

# 方法 date.timetuple() 返回日期对应的time.struct_time()对象
print(date.today().timetuple())
# <class 'time.struct_time'>
print(type(date.today().timetuple()))

# date.toordinal()	返回日期是是自 0001-01-01 开始的第多少天 year, month, day -> ordinal
print(date.today().toordinal())  # 当前本地日期距离 0001-01-01 多少天
print(date.today().replace(2019, 3, date.today().day + 1).toordinal())
print(date.fromtimestamp(1).toordinal())  # 1970年1月1号距离 0001-01-01 多少天
print(type(date.today().toordinal()))  # 返回 <class 'int'>

# date.weekday() 返回日期是星期几，[0, 6]，0表示星期一 "Return day of the week, where Monday == 0 ... Sunday == 6."
print(date.today().weekday())
# date.isoweekday() 返回日期是星期几，[1, 7], 1表示星期一 "Return day of the week, where Monday == 1 ... Sunday == 7."
# Day-of-the-week and week-of-the-year, according to ISO
print(date.today().isoweekday())

# date.isocalendar() 返回一个元组，格式为：(year, weekday, isoweekday)
# Return a 3-tuple containing ISO year(第几年), week number(今年的第几周), and weekday(周几)
print(date.today().isocalendar())

# date.isoformat() 返回‘YYYY-MM-DD’格式的日期字符串
print(date.today().isoformat())
print(type(date.today().isoformat()))

# date.strftime(format) 返回指定格式的日期字符串，与time模块的strftime(format, struct_time)功能相同
# 底层调用时间模块 time.strftime(),返回一个日期 string
print(date.today().strftime('%Y/%m/%d'))


# datetime.time 类
"""
datetime模块下的时间类，只能处理时分秒。
定义: class datetime.time(hour, [minute[, second, [microsecond[, tzinfo]]]])
        hour, minute (required)
        second, microsecond (default to zero)
        tzinfo (default to None)：tzinfo argument must be None or of a tzinfo subclass
        fold (keyword only, default to zero)
        
"""

# 实例化,默认参数 hour=0, minute=0, second=0, microsecond=0, tzinfo=None
time1 = time()
print(time1)  # 00:00:00 __str__实现
# 指定参数,创建一个 time 对象
time1 = time(8, 0, 8, 999)
print(time1)

# 主要属性和方法

# time.max time类所能表示的最大时间 time.max = time(23, 59, 59, 999999)
print(time.max)
print(time.max.__class__)
# time.min 	time类所能表示的最小时间 time.min = time(0, 0, 0)
print(time.min)
print(time.min.__class__)
# tim.resolution 时间的最小单位，即两个不同时间的最小差值：1微秒
print(time.resolution)  # time.resolution = datetime.timedelta(microseconds=1)
print(time.resolution.__class__)
print(timedelta(microseconds=1))

time2 = time(12, 10, 1, 999888)
# time.hour 时(0-23)
print(time2.hour)
# time.minute 分(0-59)
print(time2.minute)
# time.second 秒(0-59)
print(time2.second)
# time.microsecond 微秒(0-999999)
print(time2.microsecond)
# time.tzinfo timezone info object 返回传递给time构造方法的tzinfo对象，如果该参数未给出，则返回None
# 默认参数：tzinfo=None
print(time2.tzinfo)

time3 = time(6, 10, 0, 999999)
# time.replace(hour[, minute[, second[, microsecond[, tzinfo]]]])方法，生成并返回一个新的时间对象，原时间对象不变
print(time3.replace(18, 20, 20, 888888))  # 新时间对象 18:20:20.888888
print(time3)  # 原时间对象不变 06:10:00.999999
# replace()方法 默认参数均为None, 不指定值时返回原时间对象
print(time3.replace())
print(time3.replace().__class__)

time4 = time(10, 6, 10, 100999)
# time.isoformat()方法返回一个‘HH:MM:SS.%f’格式的时间字符串 Return the time formatted according to ISO
print(time4.isoformat())  # 默认最小单位是微秒
print(time4.isoformat().__class__)  # 默认最小单位是微秒
print(time4.isoformat(timespec='milliseconds'))  # 指定毫秒格式输出

# time.strftime()方法 返回指定格式的时间字符串，与time模块的strftime(format, struct_time)功能相同
# 底层调用时间模块 time.strftime(),返回一个时间 string
print(time(10, 8, 30, 999).strftime("%H:%M:%S"))
print(time(10, 8, 30, 999).strftime("%H:%M:%S.%f"))


# datetime.datetime类
"""
datetime模块下的日期时间类, 是datetime.date类的子类
定义: datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
    The year, month and day arguments are required.
    year, month=None, day=None, 
    hour=0, minute=0, second=0,microsecond=0,
    tzinfo=None
构造datetime实例时需要传递的参数：
    year	[MINYEAR, MAXYEAR]
    month	[1, 12]
    day	    [1, 指定年份的月份中的天数]
    hour	[0, 23]
    minute	[0, 59]
    second	[0, 59]
    microsecond	[0, 1000000]
    tzinfo	tzinfo的子类对象，如timezone类的实例
"""
# datetime的一个实例对象
# The year, month and day arguments are required.
dt = datetime(2019, 12, 12)
print(dt)
# The full format looks like 'YYYY-MM-DD HH:MM:SS.mmmmmm'.
dt = datetime(2019, 4, 7, 20, 58, 30, 666)
print(dt)  # 2019-04-07 20:58:30.000666 自定义__str__()实现

# If self.tzinfo is not None, the UTC offset is also attached, giving a full
# format of 'YYYY-MM-DD HH:MM:SS.mmmmmm+HH:MM
dt = datetime(2019, 4, 7, 20, 58, 30, 666, timezone.utc)
print(dt)  # 2019-04-07 20:58:30.000666+00:00
print(dt.__str__())

# 主要方法

# datetime.today()	返回一个表示当前本地日期时间的datetime对象
print(datetime.today())  # 实现 datetime(y, m, d, hh, mm, ss = time.localtime(time.time))
print(type(datetime.today()))  # <class 'datetime.datetime'>
# test

