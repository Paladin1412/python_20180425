#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
输出CGI环境变量
"""


import os
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)  # 标准输出指定为utf8


print("Content-type: text/html")
print("")
print("""
      <html>
      <head>
        <meta charset="utf-8">
        <title>cgi environ</title>
      </head>
      <body>
""")
print("<h2>环境变量</h2>")  # cgi返回str类型，python的stdout编码时为ascii，会乱码
print("<ul>")

for key in os.environ.keys():
    # environ 包含所有http请求环境变量的字典
    print(
        "<li><span style='color:green'>%30s </span>: %s </li>" %
        (key, os.environ[key]))
print("""
      </ul>
      </body>
      </html>
      """)
