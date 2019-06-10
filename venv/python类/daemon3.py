#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/4/23 20:47
# @Author : merlinhuang
# @File   : daemon3.py

import codecs


class Student(object):
    """一个描述学生对象的类，拥有id、name、score三个属性"""

    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score



class InitStduents():
    """初始化学生的操作"""

    def __init__(self):
        """构造学生"""
        # 将所有学生信息放在一个列表中
        self.students = list()
        self.init()

    def init(self):
        """根据学生类创建学生对象们，并存储在列表中"""
        self.students.append(Student(1001, "aaa", 59))
        self.students.append(Student(1002, "bbb", 96))
        self.students.append(Student(1003, "ccc", 87))
        self.students.append(Student(1004, "ddd", 89))
        self.students.append(Student(1005, "eee", 33))
        self.students.append(Student(1006, "fff", 85))
        self.students.append(Student(1007, "ggg", 78))
        self.students.append(Student(1008, "hhh", 97))
        self.students.append(Student(1009, "iii", 31))
        self.students.append(Student(1010, "jjj", 93))

    def sort(self):
        """对存储学生对象的列表进行排序，根据key指定的student.score进行排序，返回一个排好序的列表"""
        return sorted(self.students, key=lambda student: student.score)

    def writeFile(self, newStudents):
        """将排好序的列表信息写入文件"""
        with codecs.open("sortStudent.txt", "w")as f:
            for i in newStudents:
                f.write("id = {0}".format(i.id))
                f.write("\t")
                f.write("name = {0}".format(i.name))
                f.write("\t")
                f.write("score = {0}".format(i.score))
                f.write("\n")


def main():
    """入口"""
    # 初始化学生列表
    students = InitStduents()
    # 对学生列表进行排序
    newStudents = students.sort()
    # 将排好序的学生列表写入文件
    students.writeFile(newStudents)


if __name__ == "__main__":
    main()
