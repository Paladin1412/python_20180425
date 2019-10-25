#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
元类-metaclass
用来创建类的可调用对象，一般使用类作为元类。
元类的目的主要是为了控制类的创建行为。
"""


# class Foo(object):
#     """普通类"""
#     name = 'foo'

#     def bar(self):
#         print("bar")


# 定义元类，控制上面类的创建行为
class PrefixMetaclass(type):  # 规范: 元类以Metaclass结尾
    """
    func:
        a 给普通类的成员加上 my_ 前缀
        b 给普通类增加一个 echo 方法
    """

    def __new__(cls, name, bases, attrs):
        """创建对象，返回创建后对象"""
        # 提取类的成员，加上 my_ 前缀
        _attrs = (("my_" + name, value) for name, value in attrs.items())

        _attrs = dict((name, value) for name, value in _attrs)  # 转化为字典
        _attrs['echo'] = lambda self, phrase: phrase  # 增加 echo 方法,实例方法
        # 返回创建后的类
        return type.__new__(cls, name, bases, _attrs)


# 使用元类创建一个定制的类
class Foo(object, metaclass=PrefixMetaclass):
    # __metaclass__ = PrefixMetaclass
    name = 'foo'

    def bar(self):
        print("bar")


f = Foo()
print(f.my_name)
f.my_bar()
print(f.echo("metaclass"))
