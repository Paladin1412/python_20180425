#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auhtor: @merlinhuang
#


# environ 包含HTTP请求信息的dict对象
def application(environ, start_response):
    """csgi handler"""
    # 发送http响应
    start_response('200 OK', [('Content-Type', 'text/html')])  # http header
    return [b'<h1>Hello, web!</h1>']  # http body

