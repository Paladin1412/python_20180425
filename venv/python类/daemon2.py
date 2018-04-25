#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/4/22 17:59
# @Author : Merlinhuang
# @File   : daemon2.py



"""
类的封装

"""

class JieCheng(object):
    """求阶乘"""

    def __init__(self, number):
        self.number = number

    def factorial(self, num):
        """求单个数字的阶乘，返回这个数字的阶乘"""
        factor = 1
        for i in range(1, num + 1):
            factor = factor * i
        return factor

    def sum_factorial(self):
        """求前n个数字阶乘和，以公式的形式返回结果"""

        # 存储前n个数的和
        sum = 0
        if self.number < 0:
            print("负数没有阶乘！请重新输入!")
            # exit(0)
        elif self.number == 0:
            print("0! = 1")
        else:
            for number in range(0, self.number + 1):
                # 传递给阶乘函数：1 - max_number
                sum += self.factorial(number)
            # 格式化输出
            if self.number == 1:
                print("0! + 1! = {0}".format(sum))
            if self.number == 2:
                print("0! + 1! + 2! = {0}".format(sum))
            if self.number > 2:
                print("0! + 1! + ... + {0}! + {1}! = {2}".format(self.number - 1, self.number, sum))


def main():
    while 1:
        max_number = input("请输入一个数字: ")
        # 过滤出负数、0、正数，其他均为非法字符
        if (max_number[0:1] == "-" and max_number[1:2].isdigit()) or \
                max_number.isdigit():
            max_number = int(max_number)

            # 实例化一个阶乘
            jiecheng = JieCheng(max_number)
            jiecheng.sum_factorial()
            break
        else:
            print("输入有误，请重新输入！")
            continue


if __name__ == "__main__":
    main()


