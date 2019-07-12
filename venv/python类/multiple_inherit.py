#!/bin/env python3
# -*- coding: utf-8 -*-

r"""
multiple inheritance
"""

# C3 MRO
class A(object):

    def foo(self):
        print('A foo')

    def bar(self):
        print('A bar')


class B(object):

    def foo(self):
        print('B foo')

    def bar(self):
        print('B bar')


class C1(A):
    pass


class C2(B):

    def bar(self):
        print('C2 bar')


class D(C1, C2):
    pass


if __name__ == '__main__':
    print(D.__mro__)
    d = D()
    d.foo()
    d.bar()


# Example1
class People:
    """一个描述人的基本类"""

    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性
    __weight = 0
    # 定义构造方法

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说： 我 %d 岁。" % (self.name, self.age))


# 单继承实例
class Student(People):
    """继承自People类"""

    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构造函数
        # super.__init__(n, a, w)
        People.__init__(self, n, a, w)
        self.grade = g

    # 重写父类方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多继承的基类之一
class Speaker:
    """一个演讲家的基类"""
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class Talent(Speaker, Student):
    """继承自Speaker Student类"""
    a = ''

    def __init__(self, n, a, w, g, t):
        # 调用父类构造函数
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


print(Talent.__mro__)
talent1 = Talent("Tim", 25, 60, 4, "Python")
talent1.speak()  # 优先继承括号中排前地父类的方法
talent2 = Talent("tom", 19, 70, 9, 'C++')
talent2.speak()

# 可以对实例变量动态绑定属性/方法,称为该实例的特有属性或方法
talent1.addr = "china"
print(talent1.addr)


# super()函数
class A:
    """base class"""
    def __init__(self, name):
        self.name = name
        print("父类的__init__方法被执行了!")

    def show(self):
        print("父类的show方法被执行了!")


class B(A):
    """sub class"""
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        # 利用super()函数强制调用父类同名的方法,不覆盖父类同名方法
        super().show()


obj = B("M", 15)
obj.show()
