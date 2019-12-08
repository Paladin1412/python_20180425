#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
python doctest
Python文档测试 - 注释文档里的示例进行测试.
"""


class Dict(dict):
    """
    Simple dict but also support access as dict_name.key style.
    ### begin doctest ###
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ... # 测试异常，表示中间异常信息
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    """

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):  # 不存在的属性会在此方法中查找
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':
    # 调用doctest，执行测试
    import doctest
    doctest.testmod(verbose=True)
