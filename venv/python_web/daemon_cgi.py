#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
简单的python cgi 处理程序
"""


import codecs
import sys
# python3 标准输出指定为utf8,避免http服务器编码出错
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

print("Content-type: text/html")  # http header
print("")  # 空行，告诉浏览器结束头部
print('''
      <html>
      <head>
        <meta charset="utf-8">
        <title>Hello web, first CGI program!</title>
      </head>
      <body>
        <h2>Hello World! 测试python cgi中文编码</h2>
      </body>
      </html>
''')
