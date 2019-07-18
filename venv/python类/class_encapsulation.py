#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ProtectMe:
    """封装test"""
    def __init__(self):
        self.me = "coohx"
        self.__name = "merlin"

    def __python(self):
        print("i love python")

    def code(self):
        print("Which language do you like?")
        # 类内部调用私有方法
        self.__python()


if __name__ == "__main__":
    p = ProtectMe()
    print(p.me)
    #print(p.__name)  # 类内部私有方法，不允许外部调用或修改
    p.code()  # 类自己code()方法调用了私有方法__python()，对外部不可见

