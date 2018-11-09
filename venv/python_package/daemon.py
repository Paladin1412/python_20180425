#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/4/24 21:16
# @Author : merlinhuang
# @File   : daemon.py

from datetime import datetime
print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)
print(datetime.now().microsecond)


import time
# 时间戳
print(time.time())
# 从时间戳得到一个时间对象
time_str = datetime.fromtimestamp(time.time())
print(time_str)
print(type(time_str))
# 将时间对象转为时间字符串
print(datetime.strftime(time_str, "%Y-%m-%d %H:%M:%S"))

import subprocess
# 等待子进程退出，返回退出信息
child1 = subprocess.call(["ipconfig"])
# returncode
print(child1)

# Popen创建子进程后，主程序不会等待子进程执行完成
# 返回Popen对象
child2 = subprocess.Popen(["ipconfig"])
print(child2)
# 输出子进程的PID
print(child2.pid)
# communicate()方法与子进程交互，向标准输入发送数据，从标准输出和标准错误读取返回信息。返回一个元组(stdout, stderr)
print(child2.communicate())



import os

# 执行系统命令
r = os.system("ipconfig")
print(r)

# popen() 从命令打开一个管道，返回一个文件对象,使用文件read()方法读取命令结果
re = os.popen("ipconfig", "r", 10).read()
print(re)

# 文件和目录操作

# 返回当前目录
print(os.getcwd())

# 改变路径
print(os.chdir("D:\\"))
print(os.getcwd())

# 列出执行路径下的文件名&目录名到一个list中

path = "F:\python_project\\"
dir = os.listdir(path)
print(dir)
for file in dir:
    print(file)