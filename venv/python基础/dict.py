#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/3/24 18:47
# @Author : Merlinhuang
# @File   : apollo.py


# name = input("please input your name: ")
# print("hello world {0}".format(name))

m = dict([("name", "AA"), ("age", 21)])
print(m)
m["name"] = "cc"
print(m)

name = [1, 2, 3, 4, 5, 6,]

person = {"name": "merlin",
          "gender": "man",
          "age": 21,
          }

for i in enumerate(person):
    """取对象对应的索引和值"""
    print(i)


for index, value in enumerate(name, 2):
    print("{0}: {1}".format(index, value))
# 导入
# alt + enter   快速导入要使用的模块
