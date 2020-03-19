#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
web server cgi
"""


# 从wsgiref模块导入
from wsgiref.simple_server import make_server
# 导入自定义的application函数
from hello import application


# 创建一个http服务器，IP地址为空，端口是8000，处理函数application
httpd = make_server('', 8000, application)  # http调用cgi
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求
httpd.serve_forever()
