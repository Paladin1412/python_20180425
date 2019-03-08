#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2019/2/15 16:53
# @Author : merlinhuang
# @File   : init_new_diff.py

"""
__init__() 初始化实例时被调用
__new__() 创建实例时被调用
先__new__()再__init__()

"""

# 只有 __init__() 初始化
class Person(object):
    """a people class"""
    def __init__(self, name, age):
        """初始化实例"""
        self.name = name
        self.age = age

    def __str__(self):
        """自定义__str__()"""
        return "<person: %s(%s)>" % (self.name, self.age)
    __repr__ = __str__


# __new__先创建实例，__init__()再初始化实例
class Person(object):
    """a people class"""
    def __new__(cls, name, age):
        """创建实例"""
        print("First: __new__ called")
        return object.__new__(cls)
        # return super().__new__(cls)

    def __init__(self, name, age):
        """初始化实例"""
        print("Second: __init__ called")
        self.name = name
        self.age = age

    def __str__(self):
        """自定义__str__()"""
        return "<person: %s(%s)>" % (self.name, self.age)


if __name__ == '__main__':
    person1 = Person('merlin', 25)
    # 打印对象
    print(person1)
