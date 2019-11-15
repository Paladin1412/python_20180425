#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
python unittest

"""

import unittest  # 导入py测试工具


# 测试用例，用来对字符串的一些方法进行测试
class TestStringMethods(unittest.TestCase):
    """
        定义测试类，继承自 unittest.TestCase,
        类名包含要Test字样，并且与被测试对象相关
    """

    def test_upper(self):
        """测试方法，方法名必须以test开头，会自动执行"""
        # 调用断言方法，进行测试，判断程序运行结果是否与预期一致
        self.assertEqual('foo'.upper(), 'FOO')  # 判断两个值是否相等

    def test_isuppper(self):
        self.assertTrue('FOO'.isupper())  # 判断值是否为True
        self.assertFalse('Foo'.isupper())  # 判断值是否为True

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):  # 检测异常
            # 使用非字符串参数对字符串进行分隔，触发TypeError
            s.split(2)


# setUp 和 tearDown
"""
setUp()  在每个测试方法执行前被调用
tearDown()  在每个测试方法执行后被调用
"""


class TestStringMethod(unittest.TestCase):
    """ unit test class"""

    def setUp(self):  # 在每个测试方法执行前被调用
        print("doing before unittest, begin test...")

    def tearDown(self):  # 在每个测试方法执行后被调用
        print("doing after unittest, test done.")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isuppper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)  # error seq


if __name__ == '__main__':
    # 自动执行测试
    unittest.main()
