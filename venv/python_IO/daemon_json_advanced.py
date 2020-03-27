#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
python的class对象的实例不可以直接进行JSON序列化

可使用json.dumps()的参数来定制序列化，达到序列化class的目的
"""

import json


class Student:
    """定义用来序列化的类"""

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 25, 90)
# 直接序列化类的实例，返回错误
# print(json.dumps(s))  # TypeError: Object of type 'Student' is not JSON
# serializable


# json.dumps() 的default参数指定转换为可序列化为JSON对象的函数


def student2dict(std):
    """Student类实例的转换函数，返回一个可以序列化的dict"""
    return {
        # key需要与类属性一一对应
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


# Student的实例s被default指定的转换函数调用，返回一个可序列化为JSON的dict，
# 再被转化为JSON
cls2json = json.dumps(s, default=student2dict)  # student2dict只适用于Student类
print(cls2json)

# 需要一个通用转化函数，输入实例，返回可以序列化的dict


# class实例的__dict__属性，是一个字典，存储实例的成员及其值
def serialize_instance(obj): return obj.__dict__


print(json.dumps(s, default=serialize_instance))


"""
JSON反序列化为class的实例时，json.loads() 方法首先转换出一个 dict 对象，
然后，需要给 object_hook 参数传入函数负责把dict转换为 类实例。
"""

# json.loads() 的 object_hook参数


def unserialize_object(d):
    """将JSON的反序列化结果转为class的实例 """
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age":20, "score": 88, "name": "Bob"}'
# object_hook 参数指定将反序列化结果转为类实例的函数
obj = json.loads(json_str, object_hook=unserialize_object)
print(obj)
