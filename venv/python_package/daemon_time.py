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

### 时间戳  UTC时间1970年01月01日00时00分00秒到现在的总秒数

# time.time()获取当前系统的时间戳
# 输出UNIX时间戳,与时区无关
print(time.time())


### time 模块的主要方法

# time.sleep(t) 睡眠或暂停程序t秒, t可以是浮点数/整数
# time.sleep(3.5)
print(time.time())

# time.time() 返回当前系统的时间戳
print(time.time())

# 利用time.time()计算程序运行时间, 以时间戳为准
def func():
    """test program run time"""
    time.sleep(1.15)
    pass

t1 = time.time()
func()
t2 = time.time()
print(t2 - t1)


## time.gmtime([secs]) 将时间戳转换为UTC(GMT格林威治时间)时区的结构化时间,可选参数secs的默认值为time.time()
utc_gm_time = time.gmtime()
print(utc_gm_time)
# time.struct_time(tm_year=2018, tm_mon=12, tm_mday=31, tm_hour=3(当前时区为UTC+8,UTC时间比当前时间慢8小时), tm_min=55,
# tm_sec=6, tm_wday=0, tm_yday=365, tm_isdst=0)
# 当前时间戳减去3600s,即1小时
time_stamp = time.time() - 3600
utc_gm_time = time.gmtime(time_stamp)
print(utc_gm_time)

## time.localtime([secs]) 将时间戳转换为本地时区的结构化时间, 如果secs参数未提供，则以时间戳为准, 即time.time()
local_time = time.localtime()
print(local_time)
# 提前1小时
local_time = time.localtime(time.time() - 3600)
print(local_time)

##　time.ctime([secs]) 把时间戳转化为本地时间的格式化字符串, 默认使用time.time()作为参数
# Convert a time in seconds since the Epoch to a string in local time.
str_time = time.ctime()
print(str_time)
str_time = time.ctime(time.time())
print(str_time)
# Mon Feb  8 17:51:39 2038
# 指定一个时间戳
str_time = time.ctime(1)   # Thu Jan  1 08:00:01 1970,当前时区东八区，加8小时
print(str_time)
# 当前时间提前3600s,即1小时
str_time = time.ctime(time.time() - 3600)
print(str_time)

## time.asctime([tuple]) 把结构化时间转化为格式化时间字符串, 默认将time.localtime()作为参数
# Convert a time tuple to a string
str_from_struc_time = time.asctime()
print(str_from_struc_time)
str_from_struc_time = time.asctime(time.localtime())
print(str_from_struc_time)
# 格林威治当前格式化时间字符串
gm_str_from_struc_time = time.asctime(time.gmtime())
print(gm_str_from_struc_time) # Mon Dec 31 07:13:00 2018, 比当前时间早8小时


## time.mktime([tuple]) 把结构化时间转化为时间戳, 与gmtime(),localtime()相反的操作. 接收 struct_time 对象作为参数
# Convert a time tuple in local time to seconds since the Epoch.
time_stamp_from_struct_time = time.mktime(time.localtime())
print(time_stamp_from_struct_time)
print(time.ctime(time_stamp_from_struct_time))
# 由gmtime()得到当前格林威治的结构化时间,比本地慢8小时,
time_stamp_from_struct_time = time.mktime(time.gmtime())
# 输出的格式化时间字符串时间实际为UTC时间
print(time.ctime(time_stamp_from_struct_time))


## time.strftime(format[, tuple]) 返回格式化字符串表示的时间
# 把一个struct_time（如time.localtime()和time.gmtime()的返回值）转化为格式化的时间字符串，显示的格式由参数format决定,
# 如果元组中任何一个元素越界, 就会抛出ValueError的异常.
# 未指定tuple时, 默认传入 time.localtime().
string_time = time.strftime("%Y-%m-%d %H:%M:%S")
print(string_time)
# 指定time.gmtime()作为struct_time
string_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
print(string_time)  # 2018-12-31 08:22:32 UTC早8小时

## time.strptime(string[, format]) 将格式化时间字符串转化成结构化时间
# time.strptime()方法根据指定的格式(fromat)把一个时间字符串(string)解析为时间元组,
# 要注意的是, string提供的字符串要和format参数的格式一一对应, 并且值也要在合法的区间范围内，千万不要整出14个月来。
str_time = "2018-12-31 16:40:30"
time_tuple = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
# 输出给定格式化时间字符串的struct_time元组
print(time_tuple)
str_time1 = "2018/12/31 16:40:30"
# 格式化时间字符串的格式要与format指定的格式一致
time_tuple = time.strptime(str_time1, "%Y/%m/%d %H:%M:%S")
# 输出给定格式化时间字符串的struct_time元组
print(time_tuple)


## time.clock() 返回执行当前程序的CPU时间,用来衡量不同程序的耗时.
"""
该方法在不同的系统上含义不同。在Unix系统上，它返回的是“进程时间”，用秒表示的浮点数（时间戳）。在Windows中，第一次调用，返回的是进程运
行的实际时间，而第二次之后的调用是自第一次调用以后到现在的运行时间。
"""
# 程序从开始到当前CPU时间
print(time.clock())


def procedure() -> None:  # -> None 为程序注释，返回值为None
    """test time.clock()"""
    time.sleep(3)


time_start = time.clock()
procedure()
time_stop = time.clock()
# 函数procedure()CPU运行时间
print("{0} seconds process time!".format(time_stop - time_start))

# test git stash
print(time.time())
