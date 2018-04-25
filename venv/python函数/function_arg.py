#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/4/15 17:26
# @Author : Merlinhuang
# @File   : function_arg.py





# 可变数量的参数
# *toppings 实际是一个空元组
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

make_pizza()