#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
文件对象的 truncate([size]) 方法用于截断文件
  fileObject.truncate( [ size ])
    如果指定了可选参数 size，则表示截断文件为 size 个字符 , 截断之后 size 后面的所有字符被删除
    如果没有指定 size，则从当前位置起截断
"""


with open("voip.log", "r+") as fo:
    print(fo.name)
    line = fo.read()
    print("读取第一行: %s" % line)
    # 截断剩下字符串
    print(fo.tell())
    # fo.truncate(5)  # 有size,从首行首字节开始截断
    fo.truncate()  # 当前位置为文件末尾，相当于不截断
    line = fo.readline()
    print("读取截断后数据: %s"  % line)

