#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
实例的属性和类属性的区别
"""

class Student(object):
    """test class"""
    def __init__(self, name):
        self.name = name


s1 = Student('Bob')
# 通过实例变量，给实例绑定一个新的属性
s1.score = 90


# 类属性，归类所有，类的所有实例都可以访问到
class Student(object):
    name = 'Student'


s2 = Student()
# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(s2.name)

# 打印类的name属性
print(Student.name)

# 给实例绑定name属性
s2.name = 'merlin'
print(s2.name)  # 由于实例属性优先级高于类属性，因此，实例会屏蔽掉类的name属性

# 类属性还可以正常访问
print(Student.name)

# 删除实例的name属性，再次访问实例的name属性，会找不到，类的属性就会被调用
del s2.name
print(s2.name)


# example1.
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：

class Student(object):
    """学生类"""
    count = 0

    def __init__(self, name):
        self.name = name
        # 每创建一个实例，类属性自动加1
        Student.count +=1

s3 = Student('Bart')
s4 = Student('Denis')
print(Student.count)

