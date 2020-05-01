#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
urllib提供了一系列用于操作URL的功能。
    get
    post
"""


# 请求模块
from urllib import request, parse
import json



# 设置代理,默认使用系统环境变量http_proxy代理
enable_proxy = False  # 代理开关

# 创建代理的Handler
# proxy_handler = request.ProxyHandler({
    # "https": "http://web-proxy.tencent.com:8080/",
    # "http": "http://web-proxy.tencent.com:8080/"
    # # "https": "http://127.0.0.1:12639/",
    # # "http": "http://127.0.0.1:12639/"
# })
# # 空代理
# null_proxy_handler = request.ProxyHandler({})

# if enable_proxy:
    # # 通过urllib.request.build_opener()方法使用代理对象Handler，并创建opener对象
    # opener = request.build_opener(proxy_handler)
# else:
    # opener = request.build_opener(null_proxy_handler)
# # 构建全局opener，所有的urlopen()请求，都使用自定义代理
# #request.install_opener(opener)


# request.urlopen() 打开网页
with request.urlopen("https://yesno.wtf/api") as f:
    data = f.read()  # 读取HTTP响应报文
    print('Status', f.status, f.reason)

    for k, v in f.getheaders():
        print("%s: %s" % (k, v))  # 输出HTTP响应头

    print('Data: ', data.decode('utf-8'))  # HTTP报文主体
    print(json.loads(data))


response = request.urlopen("http://www.baidu.com")
print(type(response))
print(response.msg)
print(response.status)
print(response.reason)
print(response.debuglevel)

print(response.getheaders())
print(response.getheader('Cache-Control'))

# info()方法, 返回网页的当前环境有关信息
print(response.info())
# getcode()方法, 返回网页状态码，若为200则正确，若为其他则错误
print(response.getcode())
# geturl()方法, 返回网页的url
print(response.geturl())
# urllib.request.quote() 对网址进行编码
print(request.quote("https://www.baidu.com"))
# urllib.request.unquote()  对网址进行解码
print(request.unquote('https%3A//www.baidu.com'))
print(request.unquote('https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F'))


# 模拟浏览器发送GET请求
# 使用 Request 对象添加HTTP头，伪装浏览器
url = "https://www.douban.com/search?q="
url2 = 'https://yesno.wtf/api?answer=yes&forced=false&image=https://yesno.wtf/assets/yes/2.gif'
url3 = "http://api.om.oa.com/cgi-bin/svr_mgt/cgi-bin/api/api_get_host_by_ip.cgi?dept_id=-1&client_id=114&client_password=apd@OM114&ip_list=121.51.52.103"
key = request.quote('罪恶都市')  # 中文字段，需要编码
url_all = url + key

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# 构造get请求对象,添加HTTP头，伪装浏览器
#req = request.Request(url_all, headers=header)
req = request.Request(url3, headers=header)


with request.urlopen(req) as f:  # 爬取网页
    data = f.read()
    print("Data: \n", data.decode('utf-8'))
    # print(json.loads(data))
with open('./dbsearch.html', 'wb') as fw:  # 将返回内容写入文件
    fw.write(data)


# POST方法，模拟微博登陆
print('Login to weibo.cn...')
email = "18588232937"
passwd = "hx202823"
login_data = parse.urlencode([  # 登录数据，用dict存储，parse.urlencode将其转为url参数
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
]
)
print(type(login_data))

# 构造HTTP请求
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')  # 类似referer,只保留<schema,host,port>
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

# data 参数传入POST方法的参数，data编码为bytes类型
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status: ', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))

    print('Data: ', f.read().decode('utf-8'))
