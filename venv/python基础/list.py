#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/4/1 15:16
# @Author : Merlinhuang
# @File   : daemo1.py


# ips = list()
# prefix = "192.168.1."
# ips = [prefix + '2', prefix + '3', prefix + '66',]
# # print(ips)
# ipbak = ips.copy()
# # ips.clear()
# print(ips)
# print(ipbak)


prefix = "192.168.1."
ips = [prefix + '2', prefix + '3', prefix + '66',]
ips2 = [prefix + '21', prefix + '22', prefix + '23',]

ips.extend(ips2)  # 将ips2扩展到ips后面
print(ips)



