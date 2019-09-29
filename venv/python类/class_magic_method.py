#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2019/8/19 9:56
# @Author : merlinhuang
# @File   : class_magic_method.py

"""
Python中一些特殊成员和魔发方法的介绍与使用
"""


# __doc__ 说明性文档和信息，python自建，无需定义。
class Foo:
    """Test of __doc__, auto to be collected by python."""

    def func(self):
        pass


# 打印类的说明文档
print(Foo.__doc__)


# __new__() 方法
class A:
    _dict = dict()

    def __new__(cls):
        if 'key' in A._dict:
            print("EXISTS")
            # 新创建的实例都指向第一个实例,每次都返回首次创建的实例
            return A._dict['key']
        else:
            print("NEW")
            # 只在创建第一个实例时执行一次
            return object.__new__(cls)

    def __init__(self):
        print("INIT")
        A._dict['key'] = self
        print(self)


a1 = A()
a2 = A()
a3 = A()

a1.name = 'a1'
# a1 a2 a3 其实指向同一个实例
print(a1.name)  # a1
print(a2.name)  # a1
print(a3.name)  # a1


# __str__() & __repr__()方法
"""
__str__(): 打印对象时，默认输出该方法的返回值；一般返回用户需要看到的字符串
__repr__(): 直接调用对象时，返回该方法的返回值；一般返回开发者看到的字符串，用于调试服务

通常__str__ 和 __repr__ 方法的代码是一样的
"""


# __str__()
class Foo:
    """__str__ && __repr__"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Foo objet (name: %s)" % self.name


Foo('coohx')  # <__main__.Foo object at 0x0215A190>
# 打印输出__str__方法返回的内容
print(Foo('coohx'))  # Foo objet (name: coohx)


# __repr__()
class Foo:
    """__str__ && __repr__"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Foo objet (name: %s). __str__" % self.name

    def __repr__(self):
        return "Foo objet (name: %s). __repr__" % self.name


# 直接调用时返回__repr__方法的返回值
Foo('coohx')  # Foo objet (name: coohx). __repr__
# 打印时输出__str__方法返回的内容
print(Foo('coohx'))  # Foo objet (name: coohx). __str__


# 通常__str__ 和 __repr__ 方法的代码是一样的
class Foo:
    """__str__ && __repr__"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Foo objet (name: %s)" % self.name

    __repr__ = __str__


# __iter__() 方法
"""
迭代器方法，
某些情况下，需要实例对象可被用于for循环，需要在类中定义__iter__()和__next__()方法,
__iter__()返回一个可迭代对象
__next__()返回可迭代对象的下一个元素，在后续没有元素时抛出StopIteration异常退出循环

"""


# 实现一个斐波那契数列的类， 用于for 循环
class Fib:
    """Fib class"""

    def __init__(self):
        self.a, self.b = 0, 1
        self.fv = self.a

    def __iter__(self):
        return self  # 返回可迭代对象，即实例本身

    def __next__(self):  # python2中是next()方法
        # 计算数列的下一个值
        self.a, self.b = self.b, self.a + self.b
        # 返回下一个值
        return self.a

    def usual_method(self):
        """test for usually method"""
        print("first value is %d" % self.fv)
        print("next value is %d" % self.a)


fib = Fib()
# 实例可直接进行for循环
for v in fib:
    if v > 20:
        break
    print(v)

# 实例的其他方法正常调用即可
fib.usual_method()


# __getitem__()  & __setitem__() &  __delitem__()
"""
使得实例对象可以像列表、字典那样执行与中括号有关的操作，他们分别表示取值、赋值、删除数据
a = 标识符[key]　： 　　执行__getitem__方法
标识符[key] = a  ： 　　执行__setitem__方法
del 标识符[key]　： 　　执行__delitem__方法

具体实现，与key类型有关，int型多为列表式的操作；str型多为字典式操作
"""


# __getitem__()  实现实例obj[n]取值操作
class Fib:
    """class Fib"""

    def __getitem__(self, n):  # n 索引值，此处是int型
        a, b = 1, 1
        for v in range(n):
            a, b = b, a + b
        return a


fib = Fib()
print(fib[1])  # 调用__getitem__()方法，传入索引值
print(fib[10])

# 支持切片操作 obj[star:stop:step], __getitem__()参数为int
# 对__getitem__()方法传入的参数进行判断


class Fib:
    """slice in class's obj"""

    def __getitem__(self, n):
        if isinstance(n, slice):
            a, b = 1, 1
            # 获取切片起始值、终止值
            start, stop = n.start, n.stop
            if start is None:
                start = 0
            L = []
            for v in range(stop):
                # 只从切片起始值开始追加返回结果
                if v >= start:
                    L.append(a)
                # 计算下一个值
                a, b = b, a + b
            return L

        if isinstance(n, int):
            a, b = 1, 1
            for v in range(n):
                a, b = b, a + b
            return a


fib = Fib()
# 对实例进行切边操作
print(fib[0:5])
print(fib[:10])
print(fib[3:7])

# 上面只是简单实现了实例对象的getitem操作，还不支持对带step参数切片操作 fib[1:10:2])、以及对负数进行处理，需要自己实现
# print(fib[1:10:2])  # 更完善的getitem取值操作，需要自己实现


# 结合__setitem__() __delitem__()，实现类似字典的获取、设置、删除值的操作
class Point:
    """
    实现：
    __getitem__()
    __setitem__()
    __delitem__()
    """

    def __init__(self):
        # 初始化一个记录坐标的字典，用于验证以上方法
        self.coordinate = {}

    def __str__(self):
        return "point(%s)" % self.coordinate

    def __getitem__(self, key):  # 参数为str型，实现类似字典的操作
        """用于实例的获取值"""
        return self.coordinate.get(key)

    def __setitem__(self, key, value):
        """用于实例设置值"""
        self.coordinate[key] = value

    def __delitem__(self, key):
        """用于实例删除值"""
        del self.coordinate[key]
        print("delete %s" % key)

    def __len__(self):
        return len(self.coordinate)

    __repr__ = __str__


pobj = Point()

pobj['x'] = 5  # 调用__setitem__()方法设置kv值
pobj['y'] = 10
print(pobj)

print(len(pobj))  # 调用 __len__()方法

print(pobj['x'])  # 调用 __getitem__方法获取值
print(pobj['y'])

del pobj['x']  # 调用 __delitem__()方法删除值
print(pobj)
print(len(pobj))
