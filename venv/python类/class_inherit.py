#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2019/6/5 20:13
# @Author : Merlinhuang
# @File   : class_inherit.py

r"""
类继承
"""


class People():
    """class of people."""

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("%s is %d years old." % (self.name, self.age))


# 单继承
class Student(People):
    """sub class"""

    def __init__(self, sub_name, sub_age, sub_weight, grade):
        # 调用父类的__init__()方法
        People.__init__(self, sub_name, sub_age, sub_weight)
        self.grade = grade

    def speak(self):
        """重写父类speak方法"""
        print("%s is %d years old, she is at Upper %d grade." % (self.name,
                                                                 self.age,
                                                                 self.grade))


s1 = Student('lisa', 18, 95, 12)
s1.speak()
s2 = Student('yan', 7000, 90, 99)
s2.speak()


# 多继承
F = type('Food', (), {'remember2buy': 'spam'})
E = type('Eggs', (F,), {'remember2buy': 'eggs'})
G = type('GoodFood', (F, E), {})  # under Python 2.3 this is an error!
print(G.__mro__)

