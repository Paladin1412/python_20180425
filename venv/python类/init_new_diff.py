#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2019/2/15 16:53
# @Author : merlinhuang
# @File   : init_new_diff.py

"""
__new__() 创建实例时被调用,Create and return a new object.
__init__() 初始化实例时被调用,Initialize self.

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
        self = object.__new__(cls)  # object中的__new__(cls[, ...])是静态方法,被@staticmethod修饰,此处cls看作是传递进去的实参，返回新创建的cls的实例,即self
        # 返回新的创建的实例前,根据需要进行修改定制
        self._role = "an instance of cls"
        print(self.__class__)
        return self  # 当前类的一个实例 new object instance,下一步初始化
        # return object.__new__(cls)
        # return super().__new__(cls)

    def __init__(self, name, age):  # self代表实例本身，其余参数与 __new__()参数一致
        """初始化实例"""
        print("Second: __init__ called")
        self.name = name
        self.age = age

    def __str__(self):
        """自定义__str__()"""
        return "<person: %s(%s)>" % (self.name, self.age)

    @property
    def get_role(self):
        return self._role


if __name__ == '__main__':
    person1 = Person('merlin', 25)
    print(person1.age)
    print(person1.get_role)

