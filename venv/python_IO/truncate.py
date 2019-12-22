#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
文件对象的 truncate([size]) 方法用于截断文件
  fileObject.truncate( [ size ])
    如果指定了可选参数 size，则表示从文件开头截断文件为 size 个字符 , 截断之后 size 后面的所有字符被删除
    如果没有指定 size，从文件开头截断到光标当前位置，剩余内容删除.
"""


with open("voip.log", "r+", encoding='utf-8') as fo:
    print(fo.name)
    fo.seek(28)  # 将光标移动到第二行末尾
    print(fo.tell())
    fo.truncate()  # size为空，从文件开头截断到光标当前位置，剩余内容删除
    fo.seek(0, 0)  # 移动到最开头
    line = fo.readlines()  # 从当前光标位置下一个字节开始读取
    print("读取截断后数据: %s" % line)
    print(fo.tell())  # 此时光标位于文件末尾
    fo.truncate(10)  # 指定size, 从文件开头开始截断为size个字符
    fo.seek(0, 0)  # 光标置于文件最开始，进行读取
    content = fo.read()
    print("截取10个字符10后：%s" % content)
