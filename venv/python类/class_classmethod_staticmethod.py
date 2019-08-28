#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2019/8/27 17:25
# @Author : merlinhuang
# @File   : class_classmethod_staticmethod.py

"""
Python类的静态方法和类方法区别
"""


class Foo:
    """类中的三种方法语法形式"""
    usage = "test"

    # 实例方法第一个参数必须为self，代表实例本身
    def instance_method(self):
        """实例方法"""
        print("是类{}的实例方法，只能被实例对象调用".format(Foo))
        # 通过self引用类属性
        print(self.usage)

    # 静态方法参数无要求，类似于普通函数
    @staticmethod  # 装饰静态方法
    def static_method():
        """静态方法"""
        print("是静态方法")
        # 使用类对象引用类属性
        print(Foo.usage)

    # 类方法第一个参数必须为cls，代表类本身
    @classmethod  # 装饰类方法
    def class_method(cls):
        """类方法"""
        print("是类方法")
        print(cls.usage)


foo = Foo()
# 实例访问类属性
print(foo.usage)
# 实例方法只能被实例对象调用
foo.instance_method()
# 静态方法可以被实例对象调用
foo.static_method()
# 类方法可以被实例对象调用
foo.class_method()
print("------------")

# 类对象调用静态方法
Foo.static_method()
# 类对象调用类方法
Foo.class_method()


"""
静态方法、类方法使用区别或者说使用场景
"""

# 1. 类方法用在模拟java定义多个构造函数的情况
# 由于python类中只能有一个初始化方法，不能按照不同的情况初始化类。


class Book:

    def __init__(self, title):
        self.title = title

    @classmethod
    def class_method_creat(cls, title):
        # 用新参数title重新初始化一个实例
        book = cls(title=title)
        return book

    @staticmethod
    def static_method_creat(title):
        # 调用类，重新初始化
        book = Book(title)  # 静态方法需要写死类名，不方便
        return book


# 调用__init__()初始化
book1 = Book("use instance_method_create book instance")
# 调用类方法初始化
book2 = Book.class_method_creat("use class_method_create book instance")
# 调用静态方法初始化
book3 = Book.static_method_creat("use static_method_create book instance")

print("book1 title: {}".format(book1.title))
print("book2 title: {}".format(book2.title))
print("book3 title: {}".format(book3.title))


# 2. 类中静态方法调用静态方法 && 类方法调用静态方法例子


class Foo:
    """Example of staticmethod and classmethod."""
    x, y = 1, 2

    @staticmethod
    def average(*mixes):
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():
        # 静态方法调用另一个静态方法
        return Foo.average(Foo.x, Foo.y)  # 使用类对象引用类属性

    @classmethod
    def class_method(cls):
        return cls.average(cls.x, cls.y)  # cls代表类本身


foo = Foo()
print(foo.static_method())
print(foo.class_method())


# 3. 继承关系中静态方法和类方法的区别


class Foo:
    """classmethod & staticmethod in inherit"""
    x, y = 1, 2

    @staticmethod
    def average(*mixes):
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():
        return Foo.average(Foo.x, Foo.y)

    @classmethod
    def class_method(cls):
        return cls.average(cls.x, cls.y)


class Son(Foo):
    """subclass of Foo"""
    x, y = 3, 5

    @staticmethod
    def average(*mixes):  # 重写父类方法
        return sum(mixes) / 3


p = Son()
# 子类的实例继承了父类的static_method静态方法，调用该方法，还是调用的父类的方法和类属性。
# 因为静态方法写死了父类类名
print(p.static_method())
# 子类的实例继承了父类的class_method类方法，调用该方法，调用的是子类的方法和子类的类属性。
# 因为类方法中cls代表当前类本身
print(p.class_method())
