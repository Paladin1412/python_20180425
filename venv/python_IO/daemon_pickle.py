#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
序列化：
    把变量从内存中变成可存储或传输的过程称之为序列化，在python中叫pickling.
反序列化：
    反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpicking.
python 提供了 pickle 模块来实现序列化。
"""


import pickle


d = dict(name='Bob', age=20, score=90)
# 将对象d序列化

# pickle.dumps()方法 把任意对象序列化成一个bytes,可以 写到磁盘
serialization_date = pickle.dumps(d)
print(serialization_date)


# pickle.dump() 直接把对象序列化后写入一个file-like Object
f = open('dump.txt', 'wb')
pickle.dump(d, f)  # dump.txt文件被写入序列化后的对象内部信息
f.close()


# 反序列化

# pickle.loads() 对应 pickle.dumps(), 从bytes反序列化出对象，读取到内存
un_serialization_date = pickle.loads(serialization_date)
print(un_serialization_date)

# pickle.load() 方法 从一个file-like Object 中直接反序列化出对象
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
