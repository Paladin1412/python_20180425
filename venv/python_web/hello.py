#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auhtor: @merlinhuang
#
"""
web server 的WSGI处理函数
"""


# environ 包含HTTP请求信息的dict对象
def application(environ, start_response):
    """csgi handler"""
    # 发送http响应
    start_response('200 OK', [('Content-Type', 'text/html')])  # http header
    # 'PATH_INFO'为存储http请求路径信息的系统环境变量
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]  # http body
