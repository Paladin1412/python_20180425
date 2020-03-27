#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
cgi set cookie
"""


import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)


# 发送MIME类型
print("Content-Type: text/html")
# 在http头部中发送cookie
print('Set-Cookie: name="voip"; expires=Tue, 31 Mar 2020 23:20:09 GMT')
print('Set-Cookie: _addr="sz"')
print("")
print("""
      <html>
      <head>
        <meta charset="utf-8">
        <title>cgi设置cookie</title>
      </head>
      <body>
        <h2>Cookie set ok!</h2>
      </body>
      </html>
      """)
