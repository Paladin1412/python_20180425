#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/10/30 22:15
# @Author : merlinhuang
# @File   : daemon_json.py



"""
json是一种轻量级的数据交换格式
json的数据要求用双引号将字符串引起来，并且不能有多余的逗号。
"""
import json

### python数据类型与json字符串之间的转换

# json.dumps()将python数据类型编码转换成json字符串

m = {'success': True, 'message': 'hello'}
json_str = json.dumps(m)
print(json_str)
print(type(json_str))
# 将python dict 转化为 object, 将True 转为 true
# {"success": true, "message": "hello"}
# <class 'str'>


# json.loads()将json字符串解码成python对象

import json

# 自定义一个json串
jsonData = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'
text = json.loads(jsonData)
print(text)
print(type(text))
# json 的object被转化为 python的dict
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# <class 'dict'>


### python数据类型和 json文件的转换

# json.dump()  将python数据类型转换并保存到json文件内

import json

pythonDate = {'success': True, 'message': 'hello'}
f = open('b.json', 'w')
# 把 python数据转换为json串后写入到文件中
json.dump(pythonDate, f)
f.close()


# json.load() 从json格式的文件中读取数据并转换为python的类型

import json

jsonData = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
f = open('a.json', 'w')
json.dump(jsonData, f)
f.close()

f_temp = open("a.json", 'r')
# 从json文件中读取，转换为python的类型
dict11 = json.load(f_temp)
f_temp.close()
print(dict11)
print(type(dict11))
# 结果为python的字典类型
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


### json 不支持 bytes 类型，需要先将bytes类型转换成str格式

string = "python to json"
js = json.dumps(string)
print(js)

# 将 bytes 类型转换为json格式
byte = b'python bytes to json'
# 报错：Object of type 'bytes' is not JSON serializable
# js = json.dumps(byte)
# 先将 bytes 转为 str 类型，再转 json
js = json.dumps(byte.decode())
print(js)
print(type(js))
print(json.loads(js))

#　测试返回
ff = open("test.json", 'r')
str = json.load(ff)
ff.close()
print(str["error"])