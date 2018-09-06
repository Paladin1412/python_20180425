#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/9/6 21:13
# @Author : merlinhuang
# @File   : daemon_IO.py


from io import StringIO

"""
StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口
"""

"""
StringIO 在内存中读写str

StringIO 和文件操作的方法基本一致，基本所有关于文件的方法都可以用

"""
# 创建一个 StringIO 对象
f = StringIO()

# 写入数据
f.write("hello")
f.write(" ")
f.write("world!")

# getvalue()方法获得写入后的str
print(f.getvalue())

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f = StringIO("Hello!\nWeb!\nUp!")
while 1:
    s = f.readline()
    if s == '':
        break
    print(s.strip())



"""
BytesIO 在内存中读写bytes

StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO

"""

from io import BytesIO

f = BytesIO()
# 将中文str 编码后成为 bytes类型，写入到内存
f.write("学习".encode('utf-8'))

# 读出bytes类型
print(f.getvalue())
print(f.getvalue().decode('utf-8'))

# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
f = BytesIO(b'\xe5\xad\xa6\xe4\xb9\xa0')
print(f.read())


# 几个特殊的方法
# s.getvalue()   此函数没有参数，无论读写位置在哪里，都能够返回对象s中的所有数据
# s.truncate(0)	参数为0，表示清空所有写入的内容
# s.flush()     刷新内部缓冲区

print(f.getvalue().decode('utf-8'))
# 清空f内存
f.truncate(0)
# f输出为空
print("f: {0} ".format(f.getvalue().decode('utf-8')))
