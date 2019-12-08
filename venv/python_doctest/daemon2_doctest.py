#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
python doctest
Python文档测试 - 注释文档里的示例进行测试.
"""


class Dict(dict):
    """
    Simple dict but also support access as dict_name.key style.
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
