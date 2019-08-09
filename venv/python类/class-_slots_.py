#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2019/8/5 20:59
# @Author : merlinhuang
# @File   : class-_slots_.py


"""
创建一个类的实例后，可以给该实例绑定任何属性和方法,这就是动态语言的灵活性
"""

class Student(object):
    pass


# 给实例绑定一个属性
s = Student()
s.name = "merlin"
print(s.name)


# 尝试给实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType

# 将方法绑定到实例
s.set_age = MethodType(set_age, s)

# 调用绑定的方法
s.set_age(25)
print(s.age)


# 给一个实例绑定的方法，对另一个实例是不起作用的

s2 = Student()
# s2.set_age(26)  # 在新的实例调用另一个实例的方法报错


# 给类绑定方法，可以应用到所有实例

def set_score(self, score):
    self.score = score


# 给类绑定新的方法
Student.set_score = set_score

# 给类绑定的方法，所有实例均可调用
s.set_score(100)
print(s.score)

s2.set_score(99)
print(s2.score)

# 动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现


"""
特殊变量 __slots__
限制类、实例的属性
"""

# 在类中定义特殊变量__slots__，来限制改类实例能添加的属性


class Student(object):
    """"""
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()
s.name = "merlin"
s.age = 25
# s.addr = "XIAN"  # 报错AttributeError，由于__slots__限制了该类的实例只能绑定name/age属性

# __slots__定义的属性仅对当前类实例起作用，对继承的子类实例是不起作用的


class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.addr = "XIAN"

# 在子类中定义__slots__，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__


class HighStudent(Student):
    """test"""
    __slots__ = ('ip', 'size', 'addr')

    def __init__(self, addr):
        # __slots__ 也限制了构造函数中的实例属性
        self.addr = addr


# 子类的__slots__为:'name', 'age','ip', 'size', 'addr'
h = HighStudent("Beijing")
h.name = "dashan"
h.age = 18
h.ip = '192.168.1.2'
h.size = 'XL'


# __slots__ 中指定私有属性"__属性"时，子类的__slots__中的属性名会变为"_类名__属性"
class Student(object):
    __slots__ = ('age', '__name')


class Ming(Student):
    __slots__ = ()

    def __init__(self, name):
        self._Student__name = name


ming = Ming('lim')  # 正确
