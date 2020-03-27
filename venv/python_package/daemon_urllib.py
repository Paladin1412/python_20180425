#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
urllib提供了一系列用于操作URL的功能。
    get
    post
"""


# 请求模块
from urllib import request
import json


# request.urlopen() 打开网页
with request.urlopen("https://yesno.wtf/api") as f:
    data = f.read()  # 读取HTTP响应报文
    print('Status', f.status, f.reason)

    for k, v in f.getheaders():
        print("%s: %s" % (k, v))  # 输出HTTP响应头

    print('Data: ', data.decode('utf-8'))  # HTTP报文主体
    print(type(json.loads(data)))


response = request.urlopen("http://www.baidu.com")
print(type(response))
print(response.msg)
print(response.status)
print(response.reason)
print(response.debuglevel)

print(response.getheaders())
print(response.getheader('Cache-Control'))

# info()方法, 返回网页的当前环境有关信息
print(response.info())
# getcode()方法, 返回网页状态码，若为200则正确，若为其他则错误
print(response.getcode())
# geturl()方法, 返回网页的url
print(response.geturl())
# urllib.request.quote() 对网址进行编码
print(request.quote("https://www.baidu.com"))
# urllib.request.unquote()  对网址进行解码
print(request.unquote('https%3A//www.baidu.com'))


# 模拟浏览器发送GET请求
# 使用 Request 对象添加HTTP头，伪装浏览器
url = "https://www.douban.com/search?q="
key = request.quote('罪恶都市')  # 中文字段，需要编码
url_all = url + key

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
req = request.Request(url_all, headers=header)  # 构造get请求

with request.urlopen(req) as f:  # 爬取网页
    data = f.read()
    # print("Data: \n", data.decode('utf-8'))

with open('./dbsearch.html', 'wb') as fw:  # 将返回内容写入文件
    fw.write(data)

