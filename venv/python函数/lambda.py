#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/4/15 17:54
# @Author : Merlinhuang
# @File   : lambda.py



def factor(x):
    """求平方"""
    return x * x

print(factor(5))

# 匿名函数的写法
f = lambda x: x * x
print(f)
print(f(5))