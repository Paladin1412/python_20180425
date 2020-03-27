#!/usr/bin/env python3
# -*- coding: utf-8 -*-


r"""
JSON 模块
    python对象与JSON格式的转换
"""


import json


data = {
    "name": "bob",
    "age": 28,
    "score": 98
}

# json.dumps() 将python对象转换为json串,返回一个str
json_str = json.dumps(data, indent=4)  # indent 参数，输出格式化的json串
print(json_str)
print(type(json_str))

print(json.dumps([1, 2, 3, "python"]))
print(json.dumps([1, 2, 3, "python"]).__class__)


# json.loads() 将json字符串解码为python对象
# 自定义一个json串
json_str = '{"a": 1, "b": 2, "c": 3,  "d": 4, "e": [11, 22, 33]}'
obj = json.loads(json_str)
print(obj)
print(type(obj))  # class

print(json.loads("[1, 2, 4]").__class__)
print(json.loads("null"))
print(json.loads("false"))


# json.dump()  将python数据类型转换并保存到json文件内

pythonData = {
    'success': True,
    'message': 'hello',
    'site': [
        "bj",
        "sz",
        "xa",
    ],
    'addr': {
        'a': 1,
        'b': 2,
    },
}

f = open('p2j.json', 'w')
# 把 python数据转换为json串后写入到文件中
json.dump(pythonData, f)  # 序列化
f.close()


# json.load() 从json格式的文件中读取数据并转换为python的类型

f = open('./p2j.json', 'r')
j2p_obj = json.load(f)  # 反序列化
f.close()
print(j2p_obj)
print(j2p_obj.__class__)


# ## json 不支持 bytes 类型，需要先将bytes类型转换成str格式

string = "python to json"
js = json.dumps(string)
print(js)

# 将bytes类型转换为json格式
byte = b'python bytes to json'
# js = json.dumps(byte) # TypeError: Object of type 'bytes' is not JSON serializable
# 先将 bytes 转为 str 类型，再转 json
byte = byte.decode()  # 解码为str
js = json.dumps(byte)
print(js)


# ensure_ascii 参数
dict_obj = {
    "name": '小明',
    "age": 20
}
print(json.dumps(dict_obj, ensure_ascii=False))  # 非ASCII字符原样输出
print(json.dumps(dict_obj, ensure_ascii=True))  # 非ASCII字符被转义
