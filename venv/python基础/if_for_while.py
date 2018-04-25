#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/4/4 11:08
# @Author : merlinhuang
# @File   : if_for_while.py


# """
#  题目1：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# """

def analysis():
    while 1:
        strs = input("请输入随机一串字符(quit退出)：")
        if strs.strip() == "quit":
            exit(0)
        num = char = space = other = 0
        for str in strs:
            # number
            if str.isdigit():
                num += 1
            # 字母
            elif str.isalpha():
                char += 1
            # 空格
            elif str.isspace():
                space += 1
            # 特殊字符
            else:
                other += 1
        print("你的输入中数字有{0}个!".format(num))
        print("你的输入中字母有{0}个!".format(char))
        print("你的输入中空格有{0}个!".format(space))
        print("你的输入中特殊字符有{0}个!".format(other))


# """
# 题目2： 0! + 1! +2! + 3! + 4! +………………n!  求和。
# """


def factorial(number):
    """求单个数字的阶乘，返回这个数字的阶乘"""
    factor = 1
    for i in range(1, number + 1):
        factor = factor * i
    return factor


def sum_factorial():
    """求前n个数字阶乘和，以公式的形式返回结果"""
    while 1:
        max_number = input("请输入一个数字: ")
        # 过滤出负数、0、正数，其他均为非法字符
        if (max_number[0:1] == "-" and max_number[1:2].isdigit()) or \
                max_number.isdigit():
            max_number = int(max_number)
            # 存储前n个数的和
            sum = 0
            if max_number < 0:
                print("负数没有阶乘！请重新输入!")
                # exit(0)
                continue
            elif max_number == 0:
                print("0! = 1")
                break
            else:
                for number in range(0, max_number + 1):
                    # 传递给阶乘函数：1 - max_number
                    sum += factorial(number)
                # 格式化输出
                if max_number == 1:
                    print("0! + 1! = {0}".format(sum))
                if max_number == 2:
                    print("0! + 1! + 2! = {0}".format(sum))
                if max_number > 2:
                    print("0! + 1! + ... + {0}! + {1}! = {2}".format(
                        max_number - 1, max_number, sum))
                break
        else:
            print("输入有误，请重新输入！")
            continue
# sum_factorial()

"""
# 9x9 乘法口诀
#
# mutiplicand x mutiplier = mutiplicand *  mutiplier
# mutiplier = 行号 (1:9)
# mutiplicand = (1:行号)
# 1x1=1
# 1x2=2 2x2=4
# 1x3=3 2x3=6 3x3=9
"""
def mutipli_table():
    for mutiplier in range(1, 10):
        """纵向循环行号1-9"""
        for mutiplicand in range(1, mutiplier + 1):
            """横向循环列数"""
            product = mutiplicand * mutiplier
            # 格式化输出
            print("{0}x{1}={2}".format(mutiplicand, mutiplier, product),
                  end = "  ")
            if mutiplicand == mutiplier:
                print("\n")


"""
ABCD乘9=DCBA，A=? B=? C=? D=? 

答案：a=1,b=0,c=8，d=9      1089*9=9801

分析：
A = 1-9(A=1)
B = 0-9
C = 0-9
D = 1-9(D=9)
才有可能是 ABCD * 9 = DCBA
"""

# for A in range(1, 10):
def factor_1089():
    for A in [1]:
        for B in range(0, 10):
            for C in range(0, 10):
                # for D in range(1, 10):
                for D in [9]:
                    if ((A * 1000 + B * 100 + C * 10 + D) * 9) == (
                            D * 1000 + C * 100 + B * 10 + A):
                        print("A = {0}".format(A))
                        print("B = {0}".format(B))
                        print("C = {0}".format(C))
                        print("D = {0}".format(D))
                        print("{0}{1}{2}{3} * 9 = {3}{2}{1}{0}".format(A, B, C, D))


"""
九宫格
        -------------
        | A | B | C |
        | D | E | F |
        | G | H | I |
        -------------
要求：各行各列、斜线对角的3个数相加之和等于15

分析：
A：1-9
B: 1-9 除A
C：1-9 除A、B
...
...
...
"""


def jiu_gong_ge():
    """求解九宫格"""
    # 先生成一个1-9的列表，作为数字的来源
    number = list()
    for num in range(1, 10):
        number.append(num)
    # 保留原始数列
    a = number.copy()
    count= 0
    for A in number:
        # 临时新建一个列表，需要排除A,但是不影响原始列表，原始列表需要下一次循环时保持完整
        a = number.copy()
        # 移除A，作为B的循环
        a.remove(A)
        for B in a:
            # 同B，为C排除A,B
            b = a.copy()
            b.remove(B)
            for C in b:
                c = b.copy()
                c.remove(C)
                for D in c:
                    d = c.copy()
                    d.remove(D)
                    for E in d:
                        e = d.copy()
                        e.remove(E)
                        for F in e:
                            f = e.copy()
                            f.remove(F)
                            for G in f:
                                g = f.copy()
                                g.remove(G)
                                for H in g:
                                    h = g.copy()
                                    h.remove(H)
                                    for I in h:
                                        if (A+B+C == D+E+F == G+H+I == A+D+G ==
                                                B+E+H == C+F+I == A+E+I == C+E+G
                                                == 15):
                                            count += 1
                                            print('''
                                                    第{9}个解：
                                                    -------------
                                                    | {0} | {1} | {2} |
                                                    | {3} | {4} | {5} |
                                                    | {6} | {7} | {8} |
                                                    -------------                               
                                            '''.format(A, B, C, D, E, F, G, H, I, count))

def main():
    # 分析字符串
    # analysis()
    # 求阶乘
    sum_factorial()
    # 求解九宫格
    jiu_gong_ge()
    # 乘法表
    mutipli_table()
    # 1089
    factor_1089()



# __name__是内置变量, 表示当前模块的名字
# 如果一个模块被直接运行, __name__的值为__main__
if __name__ == "__main__":
    main()

