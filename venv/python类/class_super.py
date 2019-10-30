#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
super() 函数
super(cls, inst) 获得的是 cls 在 inst 的 MRO 列表中的下一个类。
"""


class Animal(object):

    def __init__(self, name):
        self.name = name

    def great(self):
        print("Hello, I am %s." % self.name)


class Dog(Animal):

    def great(self):
        # super()调用父类的同名函数，以实现父类的功能
        super().great()  # py2语法: super(Dog, self).greet()
        print("wang Wang...")


dog = Dog('dog hua hua')
dog.great()


class Case(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b


class T(Case):

    def __init__(self, a, b, c):
        # 调用父类的初始化方法
        super().__init__(a, b)  # py2语法:super(A, self).__init__(a, b)
        self.c = c


r"""
super() in MRO
"""


class Base(object):

    def __init__(self):
        print("enter Base")
        print("leave Base")


class A(Base):

    def __init__(self):
        print("enter A")
        super().__init__()  # py2: super(A, self).__init__()
        print("leave A")


class B(Base):

    def __init__(self):
        print("enter B")
        super().__init__()  # py2: super(B, self).__init__()
        print("leave B")


class C(A, B):

    def __init__(self):
        print("enter C")
        super().__init__()  # py2: super(C, self).__init__()
        print("leave C")


c = C()
print(c.__class__.mro())
print(C.mro())
