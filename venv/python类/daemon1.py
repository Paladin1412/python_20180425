#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/4/22 16:00
# @Author : Merlinhuang
# @File   : daemon1.py
"""
访问限制
成员保护
"""

#
# class Student(object):
#     """表示学生群体的一个类"""
#
#     def __init__(self, name, age, job):
#         """初始化属性"""
#         self.name = name
#         self.age = age
#         self.__job = job
#     def print_score(self):
#         """打印学生的分数"""
#         print("{0} : {1}".format(self.name, self.age))
#
#
# student1 = Student("bob", 20, ops)
# print("studennt1's job is {0}".format(student1.name))
# student1.print_score()
#
#
# student1.name = "limei"
# print("studennt1's name is {0}".format(student1.name))


class Student(object):
    """表示学生群体的一个类"""

    def __init__(self, name, age, job):
        """初始化属性"""
        self.name = name
        self.age = age
        # 私有属性，只有实例本身可以访问
        self.__job = job
        # 保护变量，本身及子类可以访问
        self._score = 99

    def print_score(self):
        """打印学生的分数"""
        print("{0} : {1}".format(self.name, self.age))
        print("{0} : {1}".format(self.name, self.__job))
        print("{0} : {1}".format(self.name, self._score))


student1 = Student("bob", 20, "ops")
# 外部不可以访问实例私有属性
# print("studennt1's job is {0}".format(student1.__job))
student1.print_score()
# 外部访问保护变量，但不建议这么做
print(student1._score)

# Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性

print("studennt1's job is {0}".format(student1._Student__job))


# 一种错误写法

student1.__job = "docter"  # 不是在修改私有变量，而是给实例student1新增了一个__name变量
print(student1.__job)  # 运行不报错,输出新的__name变量
print(student1._Student__job)  # 原来的私有变量没有变化
