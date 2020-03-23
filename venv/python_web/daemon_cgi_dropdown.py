#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
dropdown.html的后端CG1脚本，处理post提交的表单数据
"""

import cgi
import sys
import codecs
sys.stdout = codecs.getwriter("utf8")(sys.stdout.buffer)


# 创建FieldStorage()实例
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('dropdown'):
    dropdown_value = form.getvalue('dropdown')
else:
    dropdown_value = "没有内容"

print("Content-type:text/html")
print("")
print("""
      <html>
      <head>
        <meta charset="utf-8">
        <title>py3 CGI 测试</title>
      </head>
      <body>
      """)
print("<h2>选中的选项是：%s</h2>" % dropdown_value)
print("""
      </body>
      </html>
      """)
