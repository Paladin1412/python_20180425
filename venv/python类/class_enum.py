#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2019/10/10 9:42
# @Author : merlinhuang
# @File   : class_enum.py

"""
enum 提供了 Enum/IntEnum/unique 三个工具，用法也非常简单，
可以通过继承 Enum/IntEnum 定义枚举类型，其中 IntEnum 限定枚举成员必须为（或可以转化为）整数类型，
而 unique 方法可以作为修饰器限定枚举成员的值不可重复。
"""


from enum import Enum, unique, IntEnum


# 使用Enum, 定义枚举类
class Color(Enum):
    """枚举类，继承自Enum"""
    # 枚举成员
    RED = 1
    GREEN = 2
    BLUE = 3


# 枚举类型不可实例化
# 获取枚举成员
print(Color.RED)
# Color.RED
print(type(Color.RED))
# <enum 'Color'>
print(isinstance(Color.GREEN, Color))  # 枚举成员本身也是枚举类型
# True

# 枚举类型不可实例化，不可更改。
# Color.RED = 2  # 报错: Cannot reassign members.


# #定义枚举
# 枚举成员名不允许重复
class Color(Enum):
    red = 0
    green = 2
    # red = 3  # TypeError: Attempted to reuse key: 'red'


# 成员值允许相同，第二个成员的名称被视作第一个成员的别名
class Color(Enum):
    red = 1
    green = 2
    blue = 1  # 值与第一个成员值相同，此成员名为第一个成员的别名


print(Color.red)
# Color.red
print(Color.blue)  # 获取到是第一个成员
# Color.red
print(Color(1))  # 通过成员值获取枚举成员时，只能获取到第一个成员
# Color.red


# #unique 限制枚举成员的值不可重复
@unique
class Color(Enum):
    """使用enum提供的 unique 限制枚举成员值不能重复"""
    red = 1
    green = 2
    # blue =1  # 报错：ValueError: duplicate values found in <enum 'Color'>: blue -> red
    blue = 10


# #枚举取值

# 可以通过成员名来获取成员，也可以通过成员值来获取成员
# 成员名获取成员
print(Color.blue)
print(Color['blue'])
# 成员值获取成员
print(Color(10))

# 每个成员都有名称属性和值属性
member = Color.green
print(member.name)  # 名称属性 green
print(member.value)  # 值属性 2


# 支持迭代的方式遍历成员，按定义的顺序，如果有值重复的成员，只获取重复的第一个成员
class Color(Enum):
    """迭代枚举类"""
    red = 1
    green = 2
    blue = 1


for color in Color:
    print(color)

# 枚举类的特殊属性 __members__ 是一个将名称映射到成员的有序字典，也可以用来完成遍历
for m in Color.__members__:
    print(m)  # 默认遍历key，即成员名

for m, v in Color.__members__.items():
    print("name：%s, member: %s" % (m, v))  # name：red, member: Color.red


# #枚举比较
# 枚举成员可以通过 is 同一性比较，或者通过 == 等值比较

print(Color.red is Color.red)
print(Color.red is not Color.blue)  # False，blue和red成员值重复

print(Color.blue == Color.red)
print(Color.red != Color.green)
# 枚举成员不能进行大小比较
# print(Color.red < 3)  # TypeError: '<' not supported between instances of 'Color' and 'int'
# print(Color.red < Color.green)  # TypeError: '<' not supported between instances of 'Color' and 'Color'


# #由于枚举成员本身也是枚举类型，因此可以通过枚举成员找到其他成员
print(isinstance(Color.red, Color))  # True

print(Color.red)
print(Color.red.green)  # 通过 Color.red 找到 Color.green
# 但是要谨慎使用这一特性，因为可能与成员原有的命名空间中的名称冲突


class Attr(Enum):
    """成员的名称属性、值属性与成员名冲突"""
    name = 'Name'
    value = 'Value'


# 想使用成员Attr.name找到成员Attr.value，但是此处是调用了成员Attr.name的值属性
print(Attr.name.value)  # Name
# 想使用成员Attr.value找到成员Attr.name，但是此处是调用了成员Attr.value的名称属性
print(Attr.value.name)  # value


# #扩展枚举 IntEnum
# IntEnum 是 Enum 的扩展，不同类型的整数枚举也可以相互比较
from enum import IntEnum


class Shape(IntEnum):
    """继承自 IntEnum 的枚举类"""
    circle = 1
    square = 2


class Request(IntEnum):
    post = 1
    get = 2


print(Shape.circle == 1)  # True
print(Shape.circle < Shape.square)  # True
print(Shape.circle == Request.post)  # True
print(Shape.square >= Request.get)  # True

