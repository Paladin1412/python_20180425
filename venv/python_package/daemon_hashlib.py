#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/8/3 21:24
# @Author : merlinhuang
# @File   : daemon_hashlib.py

import hashlib

"""
Python内置的hashlib模块为我们提供了多种安全方便的摘要方法
hashlib模块支持md5(),sha1(), sha224(), sha256(), sha384(), sha512(), blake2b()，
blake2s()，sha3_224(), sha3_256(), sha3_384(), sha3_512(), shake_128(), shake_256()等多种hash构造方法
"""



# 通过构造函数获取一个hash对象
md5 = hashlib.md5()
# 使用update方法添加消息
md5.update(b'python is powerful, ')
# 继续追加
md5.update(b'you should use it.')

# digest()方法获得 bytes 类型的摘要值
md5_result = md5.digest()
print(md5_result)

# hexdigest()方法获得 str 类型的16进制表示的摘要值
md5_result = md5.hexdigest()
print(md5_result)

# digest_size 属性，消息摘要值的长度
print(md5.digest_size)

# block_size 属性，摘要值的内部块大小
print(md5.block_size)


# 简洁用法

print(hashlib.md5(b"python is powerful, you should use it.").hexdigest())
print(hashlib.sha256(b"python is powerful, you should use it.").hexdigest())



###  hashlib.new(name[, data])
# name是某个算法的字符串名称
# data是可选的bytes类型待摘要的数据

h = hashlib.new('sha256', b'tencent is lalala')
h_result = h.hexdigest()
print(h_result)


### hashlib模块的常量属性

# hashlib.algorithms_guaranteed  所有平台中，模块支持的hash算法列表
print(hashlib.algorithms_guaranteed)

# hashlib.algorithms_available   当前Python解释器环境中，模块支持的hash算法列表
print(hashlib.algorithms_available)

# hash.name hash对象使用的摘要算法名称
print(md5.name)
print(h.name)

# hash.copy() 哈希对象的拷贝
h_copy = h.copy()
print(h_copy.hexdigest())
h_copy.update(b"xiaomi is bababa")
print(h_copy.hexdigest())

