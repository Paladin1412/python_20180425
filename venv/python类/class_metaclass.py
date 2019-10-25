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
# metaclass是类的模板，必须从‘type’类派生
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


# 定义类的时候，使用元类来定制类
class Foo(object, metaclass=PrefixMetaclass):  # 关键字参数metaclass指定元类
    # __metaclass__ = PrefixMetaclass  # python2 语法
    name = 'foo'

    def bar(self):
        print("bar")


f = Foo()
# 类Foo的属性名被元类修改
# f.name  # 报错，AttributeError: 'Foo' object has no attribute 'name'
print(f.my_name)
# 类Foo方法名被元类修改
f.my_bar()
# 元类给类Foo增加了echo方法
print(f.echo("hello metaclass"))


# 有继承的例子
class Bar(Foo):
    """继承Foo"""
    name = "bar"
    pass


b = Bar()
# print(b.name)  # 报错，类Bar没有这个属性
# 类的属性被父类的元类修改,即元类会隐式的继承到子类
print(b.my_name)
b.my_bar()
print(b.echo("hello bar metaclass"))
