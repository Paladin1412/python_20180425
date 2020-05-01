#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
urllib提供了一系列用于操作URL的功能。
    get
    post
    GET请求是添加在url中发出的,POST是夹在请求体内发出的
"""


# 请求模块
from urllib import request, parse
import json
# import os
# import sys
# import codecs

# os.environ['LANG']='zh_CN.UTF-8'
# sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)


# 模拟浏览器发送GET请求
# 使用 Request 对象添加HTTP头，伪装浏览器
"""
http://api.om.oa.com/cgi-bin/svr_mgt/cgi-bin/api/api_get_host_by_ip.cgi?
    dept_id=-1&client_id=114&client_password=apd@OM114&ip_list=121.51.52.103
"""
url = "http://api.om.oa.com/cgi-bin/svr_mgt/cgi-bin/api/api_get_host_by_ip.cgi"
query_string = {
    "dept_id": -1,
    "client_id": 114,
    "client_password": "apd@OM114",
    "ip_list": "121.51.52.103;121.51.52.102"
}
# 编码get方法要提交的查询参数
query_string = parse.urlencode(query_string)  # urlencode()
url = url + '?' + query_string
print(url)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# 构造get请求对象,添加HTTP头，伪装浏览器
req = request.Request(url, headers=header)

with request.urlopen(req) as f:  # 爬取网页
    data = f.read()
    print("Data: \n", data.decode('utf-8'))
    print(json.loads(data))


# test apdchange system
"""
curl -v
http://apdchange.oa.com/cgi-bin/change_system/cgi-bin/check_diff_totalview.cgi
-d 'data={"plat_id":49,"biz_id":77,"diff_list":[1],"page_index":0,\
    "per_page":60,"query_type":"total","rtx":"merlinhuang","soft_id_list":[]}'
"""
print("begin request api")
real_data = {
    "plat_id": 49,
    "biz_id": 77,
    "diff_list": [1],
    "page_index": 0,
    "per_page": 60,
    "query_type": "total",
    "rtx": "merlinhuang",
    "soft_id_list": []
}
# urlencode()无法处理嵌套字典，将内层转为json串
# real_data = json.dumps(real_data)
real_data = json.dumps(real_data)
print(real_data)
# 嵌套字典
post_data = {
    "data": real_data
}
# print(json.dumps(post_data).encode("utf-8"))
# post_data = json.dumps(post_data)
post_data = parse.urlencode(post_data)  # form-encoded
print(post_data)

# HTTP request
req = request.Request(
    'http://apdchange.oa.com/cgi-bin/change_system/cgi-bin/\
check_diff_totalview.cgi')
req.add_header('Origin', 'http://apdchange.oa.com')
req.add_header(
    'User-Agent',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36')
req.add_header(
    'Referer',
    'http://apdchange.oa.com/cgi-bin/change_system/cgi-bin/index.cgi')
# MIME不是json,是application/x-www-form-urlencoded, 表示浏览器提交 Web
# 表单时使用，表单数据会按照 name1=value1&name2=value2 键值对形式进行编码。
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
# req.add_header('Content-Type', 'application/json')

# data参数传入POST方法的参数，data编码为bytes
with request.urlopen(req, data=post_data.encode('utf-8')) as f:
    data = f.read()
    print('Status ', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data: ', data.decode('utf-8'))
    print(json.loads(data))
