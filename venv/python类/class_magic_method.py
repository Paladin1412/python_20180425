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

    def __new__(cls):  # 类方法
        """先调用__new__创建实例"""
        if 'key' in A._dict:
            print("EXISTS")
            # 新创建的实例都指向第一个实例,每次都返回首次创建的实例
            return A._dict['key']
        else:
            print("NEW")
            # 只在创建第一个实例时执行一次
            return object.__new__(cls)  # 返回实例

    def __init__(self):  # 实例方法
        """再调用__init__初始化实例"""
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
        return "Foo object (name: %s)" % self.name


Foo('coohx')  # <__main__.Foo object at 0x0215A190>
# 打印输出__str__方法返回的内容
print(Foo('coohx'))  # Foo object (name: coohx)


# __repr__()
class Foo:
    """__str__ && __repr__"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Foo object (name: %s). __str__" % self.name

    def __repr__(self):
        return "Foo object (name: %s). __repr__" % self.name


# 直接调用时返回__repr__方法的返回值
Foo('coohx')  # Foo object (name: coohx). __repr__
# 打印时输出__str__方法返回的内容
print(Foo('coohx'))  # Foo object (name: coohx). __str__


# 通常__str__ 和 __repr__ 方法的代码是一样的
class Foo:
    """__str__ && __repr__"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Foo object (name: %s)" % self.name

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
        if isinstance(n, slice):  # 参数为切片对象
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

        if isinstance(n, int):  # 参数为int
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


# __getattr__() & __getattribute__() & __setattr__() & __delattr__() 方法
"""
定制属性的访问
__getattr__(self,name)：如果name被访问，同时它不存在的时候，此方法被调用。
__getattribute__(self,name)：当name被访问时自动被调用（注意：这个仅能用于新式类），无论name是否存在，都要被调用。
__setattr__(self,name,value)：如果要给name赋值，就调用这个方法。
__delattr__(self,name)：如果要删除name，这个方法就被调用。
"""


# __getattr__()
# 调用类中不存在的属性时(不存在于对象的的__dict__中)，python会调用 __getattr__() 方法的返回值，尝试获得属性；
# 已有的属性不会再 __getattr__()中查找;
# __getattr__默认返回 None
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __getattr__(self, attr):
        """外部调用类不存在的属性时，python解释器会调用__getattr__()的返回值"""
        # 对'z'属性进行单独处理
        if attr == 'z':
            return self.x**2 + self.y**2
        # 其他不存在的属性，__getattr__()默认返回 None


p = Point(10, 5)
print(p.z)  # 不存在的属性，到__getattr__()中查找
print(p.w)  # None __getattr__()默认返回 None


# __getattr__() 只响应几个特定的属性，需要加入异常处理，按照约定抛出AttributeError错误
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __getattr__(self, attr):
        """外部调用类不存在的属性时，python解释器会调用__getattr__()的返回值"""
        # 对'z'属性进行单独处理
        if attr == 'z':
            return self.x**2 + self.y**2
        if attr == 'len':
            # 返回函数/方法
            return lambda: 25

        # 只响应上面两个属性，其他属性都抛出异常
        # raise AttributeError('Point object has no attribute %s' % attr)


p = Point(4, 6)
print(p.z)
print(p.len())  # __getattr__返回值为函数
print(p.w)  # 非特定的属性，抛出 AttributeError 错误
print(p.__dict__)


# __getattribute__()
# 只要访问实例的属性，该方法就会被调用，不管属性是否存在
# 当同时定义__getattribute__() 和 __getattr__()时，访问实例属性时，不会调用__getattr__()，除非__getattribute__()中显式调用了__getattr__()，
# 或者前者返回AttributeError异常；
# 为了避免无限递归，__getattribute__()要调用基类的__getattribute__()方法返回属性值
class Point(object):
    """test for __getattribute__()"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __getattribute__(self, name):
        print("access attr via getattribute")  # 定制属性的访问过程，打印需要的信息
        return object.__getattribute__(self, name)  # 避免无限递归
        # return self.__dict__[name]  # 访问self.__dict__,要继续调用__getattribute__(),会导致无限递归（死循环）

    def __getattr__(self, name):
        if name == 'z':
            return self.x**2 + self.y**2


p = Point(3, 4)
print(p.x)  # 访问存在的属性 access attr via getattribute
print(p.y)
print(p.a)  # 访问不存在的属性， 先调用__getattribute__(),报AttributeError异常，然后通过调用__getattr__(),返回默认值None
# access attr via getattribute
# None


# __setattr__ __delattr__()
class Point(object):
    """
    实现：
    __setattr__(self, name, value)  设置实例属性时调用
    __delattr__(self, name)  删除实例的属性时调用
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __getattr__(self, attr):
        """属性不存在时，调用"""
        if attr == 'z':
            return 0
        raise AttributeError("Point object has no attribute %s" % attr)

    def __setattr__(self, name, value):
        """给实例的属性设置值时，调用"""
        # 设置属性及其值, 涉及到实例的所有属性的设置
        print("set attr via __setattr__")
        # self.__dict__[name] = value  # 将属性和值保存到__dict__中
        # 调用基类的同名方法实现
        return object.__setattr__(self, name, value)

    def __delattr__(self, name):
        """删除实例属性值"""
        print("del attr via __delattr__")
        return object.__delattr__(self, name)


p = Point()
print(p.z)
p.len = 15
print(p.len)
del p.len  # 调用 __delattr__() 方法
# print(p.len)  # 报错，属性已经被删除


# __call__()方法，使实例可被调用
class Point:

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __call__(self, z):
        """直接对实例进行调用"""
        return self.x + self.y + z


p = Point(2, 3)
# 使用 callable 判断对象是否能被调用，能被执行的对象就是一个Callable对象
print(callable(p))  # True
# 直接调用实例
print(p(7))


# __module__ 和 __class__
# Python内建，无需自定义。
# __module__ 表示当前操作的对象在属于哪个模块。
# __class__ 表示当前操作的对象属于哪个类。
class Foo:

    pass


obj = Foo()
print(obj.__module__)  # __main__
print(obj.__class__)  # <class '__main__.Foo'>


# __del__() 析构方法，当对象在内存中被释放时，自动触发此方法
# 此方法一般无须自定义，因为Python自带内存分配和释放机制，除非你需要在释放的时候指定做一些动作。
# 析构函数的调用是由解释器在进行垃圾回收时自动触发执行的。
class Foo:

    def __del__(self):
        print("我被回收了！")  # 定制回收


obj = Foo()
del obj  # 我被回收了！


# __dict__ 列出类或对象的所有成员， python自建，无需用户自定义
class Province:
    """example for __dict__"""
    country = 'China'

    def __init__(self, name, count):
        self.name = name
        self.count = count

    @staticmethod
    def func():
        print('func')


# 获取类的成员
print(Province.__dict__)
# 获取对象obj1的成员
obj1 = Province('ShanXi', 360000)
print(obj1.__dict__)


# __len__()
# 在Python中，如果你调用内置的len()函数试图获取一个对象的长度，在后台，其实是去调用该对象的__len__()方法
print(len('ABC'))
print('ABC'.__len__())  # 等价


# __add__: 加运算 __sub__: 减运算 __mul__: 乘运算 __div__: 除运算 __mod__: 求余运算 __pow__: 幂运算
class Vector:
    """example for arithmetic"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(3, 4)
v2 = Vector(1, -2)
print(v1 + v2)  # 实例


# __author__ 代表作者信息
__author__ = "merlin"
print(__author__)
