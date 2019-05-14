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
print("The instance of datetime.date")
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
print("The instance of datetime.time")
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
# time.isoformat()方法返回一个‘HH:MM:SS.mmmmmm’格式的时间字符串 Return the time formatted according to ISO
print(time4.isoformat())  # 默认最小单位是微秒
print(time4.isoformat().__class__)  # 字符串格式
print(time4.isoformat(timespec='milliseconds'))  # 指定毫秒格式输出

# time.strftime()方法 返回指定格式的时间字符串，与time模块的strftime(format, struct_time)功能相同
# 底层调用时间模块 time.strftime(),返回一个时间 string
print(time(10, 8, 30, 999).strftime("%H:%M:%S"))
print(time(10, 8, 30, 999).strftime("%H:%M:%S.%f"))


# datetime.datetime类
"""
一定要注意这是datetime模块下的datetime类，千万不要搞混了！
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
print("The instance of datetime.datetime")
# datetime的一个实例对象
# The year, month and day arguments are required.
dt = datetime(2019, 12, 12)
print(dt)
# The full format looks like 'YYYY-MM-DD HH:MM:SS.mmmmmm'.
dt = datetime(2019, 4, 7, 20, 58, 30, 666)
print(dt)  # 2019-04-07 20:58:30.000666 自定义__str__()实现

# 初始化带时区信息
# If self.tzinfo is not None, the UTC offset is also attached, giving a full
# format of 'YYYY-MM-DD HH:MM:SS.mmmmmm+HH:MM'
dt = datetime(2019, 4, 7, 20, 58, 30, 666, timezone.utc)
print(dt)  # 2019-04-07 20:58:30.000666+00:00
print(dt.__str__())


# 主要属性和方法

# datetime.today()	返回一个表示当前本地日期时间的datetime对象
# today()方法继承自datetime.date类
print(datetime.today())  # 实现 datetime(y, m, d, hh, mm, ss = time.localtime(time.time))
print(type(datetime.today()))  # <class 'datetime.datetime'>


# datetime.now([tz]) tz可选，返回指定时区的日期时间的datetime对象，tz不指定时，返回当前本地日期时间的datetime对象
print(datetime.now())  # 2019-05-06 21:13:31.719628
# 指定tz为timezone.utc，比当前慢8小时
print(datetime.now(timezone.utc))  # 2019-05-06 13:13:31.719628+00:00

# datetime.utcnow() 返回当前utc日期时间的datetime对象 Construct a UTC datetime from time.time().
print(datetime.utcnow())

# datetime.fromtimestamp(t[, tz]) 根据指定的时间戳创建一个datetime对象
import time
# tz默认为None
print(datetime.fromtimestamp(time.time()))
# 带时区信息，返回'YYYY-MM-DD HH:MM:SS.mmmmmm+HH:MM'格式的datetime对象
print(datetime.fromtimestamp(time.time(), timezone.utc))

# datetime.utcfromtimestamp(t) 根据指定的时间戳创建一个UTC时区的 datetime对象. 因为本身就是UTC时区，所以无utc offset
# 'YYYY-MM-DD HH:MM:SS.mmmmmm'
print(datetime.utcfromtimestamp(time.time()))

# datetime.combine(date, time) 把指定的date和time对象整合成一个datetime对象
print(datetime.combine(date.today(), time1))
print(datetime.combine(date.today(), time2))

# datetime.strptime(date_string, format) 将日期时间字符串转换为datetime对象
print(datetime.strptime("2019-05-07 12:10:01", "%Y-%m-%d %H:%M:%S"))
print(type(datetime.strptime("2019-05-07 12:10:01", "%Y-%m-%d %H:%M:%S")))
print(datetime.strptime("2019-05-07 16:38:47.281021", "%Y-%m-%d %H:%M:%S.%f"))
print(datetime.strptime("2019-05-07 16:38:47.281021", "%Y-%m-%d %H:%M:%S.%f").__class__)

# dt.year, dt.month, dt.day 年、月、日
dt = datetime.today()
print(dt.year)
print(dt.month)
print(dt.day)
# dt.hour, dt.minute, dt.second 时、分、秒
print(dt.hour)
print(dt.minute)
print(dt.second)
# dt.microsecond, dt.tzinfo	微秒、时区信息
print(dt.microsecond)
print(dt.tzinfo)

# dt.date()	获取datetime对象对应的date对象
print(dt.date())
print(dt.date().__class__)
# dt.time()	获取datetime对象对应的time对象, tzinfo 为None
print(dt.time())
# dt.timetz() 获取datetime对象对应的time对象，tzinfo与datetime对象的tzinfo相同
print(dt.timetz())  # 17:22:46.590853 tz默认为None
print(datetime.now(timezone.utc).timetz())  # 指定tz为utc, 比当前时间慢8小时 09:22:46.590853+00:00

# dt.replace()	生成并返回一个新的datetime对象，如果所有参数都没有指定，则返回一个与原datetime对象相同的对象
dt = datetime.today()
print(dt.replace())
print(dt.replace(2018))
print(dt)

# dt.timetuple() 返回datetime对象对应的time.struct_time对象
# tzinfo默认为None, dst=-1
print(dt.timetuple())
# <class 'time.struct_time'>
print(type(dt.timetuple()))

# dt.utctimetuple() 返回datetime对象对应的utc时间的tuple
# Return UTC time tuple compatible with time.gmtime().
# 当前时区为UTC+8,UTC时间比当前时间慢8小时
print(datetime.utcnow().utctimetuple())  # bug: utctimetuple() can not -offset

# dt.timestamp() 返回datetime对象对应的时间戳，Python 3.3才新增的
dt = datetime.now()
print(dt.timestamp())
# 当前时区为UTC+8,UTC时间比当前时间慢8小时
print(datetime.utcnow().timestamp())

# dt.toordinal() 继承自 datetime.date类，返回日期是是自 0001-01-01 开始的第多少天
# 当前日期到0001-01-01过了多少天
print(dt.toordinal())
# utc时区，时间戳为10s，即1970-01-01 00:00:10到0001-01-01过了多少天
print(datetime.fromtimestamp(10, timezone.utc))
print(datetime.fromtimestamp(10, timezone.utc).toordinal())

# dt.weekday() 继承自 datetime.date类, 返回日期是星期几，[0, 6]，0表示星期一 "Return day of the week, where Monday == 0 ... Sunday == 6."
print(datetime.now().weekday())
# dt.isoweekday() 继承自 datetime.date类, 返回日期是星期几，[1, 7], 1表示星期一 "Return day of the week, where Monday == 1 ... Sunday == 7."
print(datetime.now().isoweekday())

# dt.isocalendar()继承自 datetime.date类, 返回一个元组，格式为：(year, weekday, isoweekday)
# Return a 3-tuple containing ISO year(第几年), week number(今年的第几周), and weekday(周几)
print(datetime.now().isocalendar())

# dt.isoformat([sep[, timespec]]) Return the time formatted according to ISO.
# Optional argument sep specifies the separator between date and time, default 'T'.
print(datetime.now().isoformat())
# 指定date和time的分隔符为空格
print(datetime.now().isoformat(sep=' '))
print(datetime.now().isoformat(sep='/'))
# 指定 timespec 为毫秒
print(datetime.now().isoformat(sep=' ', timespec="milliseconds"))  # 2019-05-07 21:23:04.635

# dt.ctime() 返回本地日期时间的格式化字符串 "weekday mounth day HH:MM:SS year"
print(datetime.now().ctime())  # Wed May  8 09:22:53 2019
print(datetime.now().ctime().__class__)  # <class 'str'>

# dt.strftime(format) 返回指定格式的时间字符串
print(datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"))
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# datetime.timedelta 类
"""
class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
timedelta 对象表示两个不同日期时间对象之间的差值，可以对datetime.date, datetime.time和datetime.datetime对象做算术运算。
将所有内容标准化为天,秒,微秒的形式：
    Representation: (days, seconds, microseconds)
返回：
    datetime supports subtraction of two datetime objects returning a timedelta
    subtraction of a datetime and a timedelta giving a datetime
"""
print("The instance of datetime.timedelta")
# 默认 days=0, seconds=0, microseconds=0, milliseconds=0, hours=0, weeks=0
print(timedelta())  # 0:00:00 __str__() 实现
print(type(timedelta()))

# timedelta.min 由 timedelta(-999999999)生成的timedelta对象
print(timedelta.min)  # -999999999 days, 0:00:00
print(type(timedelta.min))

# timedelta.max 由 timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)生成的timedelta对象
print(timedelta.max)  # 999999999 days, 23:59:59.999999
print(type(timedelta.max))

# timedelta.resolution 由 timedelta(microseconds=1)生成的timedelta对象
print(timedelta.resolution)  # 0:00:00.000001
print(type(timedelta.resolution))

# timedelta.days  天 [-999999999, 999999999]
# 其他时间单位向days换算后，取最终的 days
print(timedelta(days=2019, seconds=100, microseconds=5000000, milliseconds=1000, weeks=1).days)  # 2019+1*7=2026days
print(timedelta(days=2019, seconds=100, microseconds=5000000, milliseconds=1000, weeks=1))  # 2026 days, 0:01:46

# timedelta.seconds 秒 [0, 24*3600],小于1天. 大于一天则取余数部分
# 小单位化大单位，其他时间单位向days换算后，取最终的 seconds
print(timedelta(days=2019, seconds=100, microseconds=5000000, milliseconds=1000, weeks=1).seconds)  # 100+5+1=106seconds
print(timedelta(days=2019, seconds=(24*3600), microseconds=5000000, milliseconds=1000, weeks=1).seconds)  # 5+1=6seconds

# timedelta.microseconds 微秒 [0, 999999],小于1S. 大于1s则取余数部分
# 小单位化大单位，向seconds换算后，取最终的 microseconds
print(timedelta(days=2019, seconds=(24*3600), microseconds=5000000, milliseconds=1000, weeks=1).microseconds)  # (5+1)%1=0microseconds
print(timedelta(microseconds=10, milliseconds=10).microseconds)  # (10+10000)%1000000=10010microseconds

# timedelta.total_seconds() 返回timedelta对象包含的总秒数
# 一年包含的总秒数
print(timedelta(365).total_seconds())

# 用timedelta进行时间运算
## datetime.datetime 与 datetime.timedelta对象，返回 datetime.datetime

dt = datetime.now()
print(dt)
# 3天后
dt += timedelta(3)
print(dt)
# datetime与timedelta运算,返回datetime类型对象
print(type(dt))  # <class 'datetime.datetime'>

# 3天前
dt = datetime.now()
dt += timedelta(-3)
print(dt)

# 3小时后
dt = datetime.now()
dt = dt + timedelta(hours=3)
print(dt)

# 3小时前
print(datetime.now() + timedelta(hours=-3))
# 3小时30秒后
print(datetime.now() + timedelta(hours=3, seconds=30))

## datetime.datetime 与 datetime.datetime对象，返回 datetime.timedelta

dt = datetime.now()
# 利用timedelta得出10小时后的datetime
dt2 = datetime.now() + timedelta(hours=10)
# 计算2个datetime的差值
td = dt2 - dt
print(td)  # 10:00:00 不满1天
# 是一个 timedelta 类型，表示 差值
print(type(td))  # <class 'datetime.timedelta'>
# 以(days, seconds, microseconds)形式表示
print(td.seconds)  # 36000s
print(td.days)  # 0 不足一天
print(td.microseconds)  # 0 大于1s,用second表示

# 用timedelta与date, time 对象进行时间运算
date1 = date.today()
print(date1)
date2 = date1 + timedelta(days=1)
print(date2)
print(type(date2))  # date 对象

td2 = date2 - date1
print(td2)  # 1 day, 0:00:00
print(type(td2))

import datetime
time1 = datetime.time(20, 30, 30)
print(time1)
# time2 = time1 + timedelta(seconds=30)  # unsupported operand type(s) for +: 'datetime.time' and 'datetime.timedelta'
