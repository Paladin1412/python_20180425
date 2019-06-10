#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2019/3/8 11:19
# @Author : merlinhuang
# @File   : type_creat_class.py


# 使用type()函数创建类
"""
1. type(object) -> the object's type
2. type(name, bases, dict) -> a new type
"""

# 传入一个对象时，返回对象的类型
print(type(1))

# 传入3个参数，创建新的type对象


# 使用class定义类
class A(object):
    # 类属性
    role = 'student'

    # 初始化
    def __init__(self, name):
        self.name = name

    # 类方法
    @classmethod
    def study(cls):
        pass

    # 静态方法
    @staticmethod
    def cal_student_num():
        pass

# 使用type()函数定义类


# 先定义类内部的方法
def __init__(self, name):
    self.name = name

@classmethod
def study(cls):
    pass

@staticmethod
def cal_student_num():
    pass


# 开始调用type()函数创建类
A = type(
    # name 要创建的类名
    'A',
    # base 代表基类（或父类），即需要继承的类对象；
    (object,),
    # dict 将外部定义的类属性、类方法、实例方法等，以键值对的形式建立映射关系。
    {
        'role': 'student',
        # 方法名称映射
        '__init__': __init__,
        'study': study,
        'cal_student_num': cal_student_num,
    }
)

student1 = A("jack")
print(student1.name)

# type()创建类后，name参数变成__name__对象属性，bases参数变成 __bases__ 对象属性，dict参数变成__dict__对象属性

print(A.__class__)
print(A.__name__)
print(A.__bases__)
print(A.__dict__)
