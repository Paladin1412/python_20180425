#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/5/8 21:26
# @Author : merlinhuang
# @File   : daemon.py
import logging

# 默认级别为warning，打印warning以上的级别
"""
logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")
"""

# 自定义日志级别，debug时，全部打印

# 定义为DEBUG
# logging.basicConfig(level=logging.DEBUG)
#
# logging.debug("This is debug message")
# logging.info("This is info message")
# logging.warning("This is warning message")
# logging.error("This is error message")
# logging.critical("This is critical message")

# logging用法
# 创建一个logging对象，然后引用

# 以指定的参数，创建logger对象，如果参数为空则返回root logger
# logger = logging.getLogger("app")
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# print(logger)
#
# def log():
#     print("It is creating a logger..")
#
# def main():
#     # 调用logger对象的info()函数，打印info信息
#     logger.info("开始执行main函数")
#     print("###"*10)
#     log()
#     logger.info("调用log()函数")
#     try:
#         error = 2/0
#         file = open("daemon.py", "r")
#     except Exception as e:
#         # 调用error()函数，打印error信息
#         logger.error("除数不能为零")
#     finally:
#         # 调用warning()函数，打印warning信息
#         logger.warning("文件没有正常关闭")
#
# main()

# 自定义日志输出格式

logging.basicConfig(level=logging.DEBUG,
                    # format字段设置日志信息格式，使用 %-style格式字符串设置LogRecord的一些属性来实现格式化的日志信息
                    # %(asctime)s 打印时间
                    # %(filename)s: 打印当前执行程序名
                    # %(lineno)d: 打印日志的当前程序行号
                    # %(levelname)s: 打印日志级别名称
                    # %(message)s: 打印日志信息，默认有这个字段
                    format='%(asctime)s %(filename)s-%(name)s line:%(lineno)d  %(levelname)s: %(message)s',
                    # 自定义日志时间格式
                    datefmt='%Y/%m/%d  %H:%M:%S',
                    # 指定日志文件名
                    filename='myapp.log',
                    filemode='w')

"""
level: 设置日志级别，默认为logging.WARNING
filename: 指定日志文件名。
filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
    %(levelname)s: 打印日志级别名称
    %(filename)s: 打印当前执行程序名
    %(funcName)s: 打印日志的当前函数
    %(lineno)d: 打印日志的当前程序行号
    %(asctime)s: 打印日志的时间
    %(thread)d: 打印线程ID
    %(process)d: 打印进程ID
    %(message)s: 打印日志信息
datefmt: 指定时间格式，同time.strftime()
stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略

"""
# 创建一个日志对象,root logger的子类,不指定是默认返回root logger
logger = logging.getLogger()
# logger.info("开始执行main函数")
# logger.debug("debug...")

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


