#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/5/9 20:48
# @Author : merlinhuang
# @File   : daemon1.py

"""
通过代码配置日志模块
"""

import logging

# 创建Logger
logger = logging.getLogger(__name__)

# 设置最低的日志级别
logger.setLevel(logging.INFO)

# 创建Handler

# 控制台日志
# 创建一个console handler，并设置日志级别为Debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 文件日志
# 最低级别warning
fh = logging.FileHandler("test.log", 'w', encoding='utf-8')
fh.setLevel(logging.WARNING)



# 创建Formatter
# 直接实例化
formatter = logging.Formatter(
    '%(asctime)s %(name)s %(filename)s line: %(lineno)d %(levelname)s: %(message)s')

# 添加formatter到handler
ch.setFormatter(formatter)
fh.formatter = formatter

# 配置Logger

# 添加handler到logger
logger.addHandler(ch)
logger.addHandler(fh)

# 程序中调用logger进行日志记录
def log():
    print("It is creating a logger..")

def main():
    # 调用logger对象的info()函数，打印info信息
    logger.info("开始执行main函数")
    print("###"*10)
    log()
    logger.info("调用log()函数")
    try:
        error = 2/0
        file = open("daemon.py", "r")
    except Exception as e:
        # 调用error()函数，打印error信息
        logger.error("除数不能为零")
    finally:
        # 调用warning()函数，打印warning信息
        logger.warning("文件没有正常关闭")

main()


