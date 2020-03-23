#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
python cgi get/psot方法处理
url实例，psot方法
"""


import cgi
# import cgitb
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)


# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取cgi数据，可以处理get和post数据
site_name = form.getvalue('name')
site_url = form.getvalue('url')

print("Content-type: text/html")
print("")
print("""
      <html>
      <head>
      <meta charset="utf-8">
      <title>一个CGI get测试实例</title>
      </head>
      <body>
     """)
print("<h2>%s业务：%s<h2/>" % (site_name, site_url))
print("""
      <body/>
      <html/>
      """)
