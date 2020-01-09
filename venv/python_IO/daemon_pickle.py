#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
序列化：
    把Python对象从内存中变成可存储或传输的过程称之为序列化，在python中叫pickling.
反序列化：
    反过来，把对象从序列化的数据重新读到内存里称之为反序列化，即unpicking.
python 提供了 pickle 模块来实现序列化。
"""


import pickle
import math


d = dict(name='Bob', age=20, score=90)
# 将对象d序列化

# pickle.dumps()方法 把任意对象序列化成一个bytes,可以 写到磁盘
serialization_data = pickle.dumps(d)
print(serialization_data)


# pickle.dump() 直接把对象序列化后写入一个file-like Object
f = open('dump.txt', 'wb')
pickle.dump(d, f)  # dump.txt文件被写入序列化后的对象内部信息
f.close()


# 反序列化

# pickle.loads() 对应 pickle.dumps(), 从bytes反序列化出对象，读取到内存
un_serialization_date = pickle.loads(serialization_data)
print(un_serialization_date)

# pickle.load() 方法 从一个file-like Object 中直接反序列化出对象
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)


# pickle 序列化多个对象
f = open('dump.data', 'wb')
pickle.dump([1, 2, 3], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()

f = open('dump.data', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))

# 还可以序列化函数、类、接口等，只是将其名称编码成对应的代码对象
func_pickle = pickle.dumps(math.cos)  # 编码后是函数对象
print(func_pickle)
cos_from_serialization = pickle.loads(func_pickle)  # 反序列化后还原为原数据对象
print(cos_from_serialization(0))
