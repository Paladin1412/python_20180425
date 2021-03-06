#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/4/12 20:48
# @Author : merlinhuang
# @File   : filew.py


import codecs


"""
w 写
r 读
a 追加
b 二进制
"""

ENCODING = "utf-8"

# # 读取文件
fr = open("test.txt", "r", encoding="utf-8")
print(fr.read())
fr.close()


# 写入文件
fw = open("test.log", "w", encoding="utf-8")
fw.write("hello world\nkeepdoing\n 走自己的路\ndevops\n2019-12-17, test...")
fw.close()

# 追加写入
fw = open("test.log", "a", encoding="utf-8")
fw.write("\n\nnewline\nhello world\nkeepdoing\n 走自己的路\ndevops")
fw.close()
# 读取文件

# 每次读取一行
fr = open("test.txt", "r", encoding="utf-8")
print(fr.readline())
# tell() 返回文件中光标当前位置
print(fr.tell())
print(fr.readline())
print(fr.tell())
fr.close()


# 每一行内容作为一个元素，组成一个列表

fr = open("test.txt", "r", encoding="utf-8")
for num, data in enumerate(fr.readlines(), start=1):
    print("第{0}行是：{1}".format(num, data.rstrip()))
fr.close()


a = ["9.79.56.200\n", "9.79.230.114\n", "9.79.231.93\n"]
with codecs.open("test.log", "w", encoding="utf-8") as fw:
    # 通过可迭代对象批量写入文件
    fw.writelines(a)
with codecs.open("test.log", "r", encoding="utf-8") as fw:
    print(fw.read())


# truncate()
ft = open("voip.log", "r+", encoding="utf-8")
print("截断前: ", ft.read().rstrip())
# 截断保留3个字符
ft.truncate(11)
print("截断后: ", ft.read().rstrip())
ft.close()

# 每次读取一行
fr = open("test.txt", "rb")
print(fr.readline())
# tell() 返回文件中光标当前位置
print("tell 位置：", fr.tell())
print(fr.readline())
print("tell 位置：", fr.tell())
fr.seek(+3, 0)
print("tell 位置：", fr.tell())
fr.seek(+3, 1)
print(fr.tell())
fr.seek(+3, 2)
print(fr.tell())
fr.close()


fr = open("test.txt", "r", encoding="utf-8")
# 文件描述符
fr.fileno()
# 文件编码
print(fr.encoding)
#  文件名
print(fr.name)
print(fr.mode)


# 判断文件是否关闭
print(fr.closed)
fr.close()
print(fr.closed)


with codecs.open("test.log", "w", encoding="utf-8") as fw:
    fw.write("hello world\nkeepdoing\n 走自己的路\ndevops\n2019-12-17, test...\n")

with open("test.log", 'r', encoding='utf-8') as fr:
    contents = fr.read()  # 获取文件全部内容，并在末尾添加换行
    print(contents.rstrip())
