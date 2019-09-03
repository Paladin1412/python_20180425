#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2019/8/16 10:43
# @Author : merlinhuang
# @File   : class_@property.py

"""
内置property装饰器
  - 类方法转为属性进行调用
  - 重新实现属性的setter、getter、deleter方法
"""


# 不使用@propert装饰器，传统的定义属性的get、set、delete方法
class Student:
    """返回、设置、删除学生分数的类"""
    def __init__(self, score):
        # protected 变量
        self._score = score

    def get_score(self):
        """获取属性值的方法，避免在类外部直接操作属性"""
        return self._score

    def set_score(self, score):
        """设置属性值的方法，避免在类外部直接操作属性"""
        if not isinstance(score, int):
            raise ValueError("score must be an integer!")
        if score < 0 or score > 100:
            raise ValueError("score must between 0 ~ 100!")
        self._score = score


s = Student(98)
print(s.get_score())  # 98

s.set_score(88)  # 调用类内部提供的set_score方法设置属性
print(s.get_score())  #


# 使用@property装饰器，实现属性调用式的方法调用
class Student:
    """返回、设置、删除学生分数的类"""
    def __init__(self, score):
        # protected 变量
        self._score = score

    @property  # 将类伪装成属性，score可以当作属性调用，相当于get方法
    def score(self):
        """"""
        return self._score

    @score.setter  # 将被装饰的方法score当作属性来赋值
    def score(self, score):
        """"""
        if not isinstance(score, int):
            raise ValueError("score must be an integer!")
        if score < 0 or score > 100:
            raise ValueError("score must between 0 ~ 100!")
        self._score = score

    @score.deleter
    def score(self):
        del self._score
        print("score has been deleted!")


s2 = Student(100)
# 将方法当作属性调用
print(s2.score)  # 获取值
s2.score = 87  # 设置值

print(s2.score)
del s2.score  # 删除属性
# print(s2.score)  # 报错，因为属性已经被删除


# 只读属性，不定义 setter 方法
class Student:
    """"""
    def __init__(self, age):
        self.__age = age

    @property  # getter方法
    def age(self):
        return self.__age


s3 = Student(18)
print(s3.age)
# s3.age = 19  # 报错，没有定义setter方法，不能赋值


"""
除了使用装饰器的方式将一个方法伪装成属性外，Python内置的builtins模块中property()函数，为我们提供了第二种设置类属性的手段。
property()函数的参数：
    第一个参数是方法名，调用 实例.属性 时自动执行的方法
    第二个参数是方法名，调用 实例.属性 ＝ XXX时自动执行的方法
    第三个参数是方法名，调用 del 实例.属性 时自动执行的方法
    第四个参数是字符串，调用 实例.属性.__doc__时的描述信息
"""
# #property()函数


class People:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    def del_age(self):
        print("删除年龄数据！")
    # 使用property()函数，将类伪装成属性。其效果和装饰器的方法是一样的。
    age = property(get_age, set_age, del_age, "age")  # 核心语句


p = People("bob", 19)
print(p.age)
p.age = 22
print(p.age)
del p.age
