#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
cgi get cookie
"""


import os
import sys
import codecs
from http import cookies
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)


print("Content-type: text/html")
print("")

print("""
      <html>
      <head>
        <meta charset="utf-8">
        <title>Cookie get</title>
      </head>
      <body>
      <h1>读取cookie信息</h1>
      """)

if 'HTTP_COOKIE' in os.environ:
    # Cookie信息存储在CGI的环境变量HTTP_COOKIE中
    cookie_sting = os.environ.get('HTTP_COOKIE')
    c = cookies.SimpleCookie()
    c.load(cookie_sting)  # load from a string (HTTP header)

    try:
        data1 = c['name'].value
        data2 = c['_addr'].value
        print("Cookie date: " + data1 + ";" + data2 + "<br>")
    except KeyError:
        print("Cookie 没有设置或者已经过时<br>")

print("""
        </body>
        </html>
      """)
