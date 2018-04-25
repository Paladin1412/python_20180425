#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/3/28 10:27
# @Author : merlinhuang
# @File   : test1.py


# name = input("Please input your name: ")
# print("hello world {0}".format(name))
# data.str_print("Dear {0}, hello world {0}".format(name))
#
# c = 12.354
# print(round(c,1))
# a = 12
# b = "hell world"
# c = 11.23233
# d = True
# e = None
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
#

a = " i am python "
print(a.strip())
print(a.lstrip())
print(a.replace("am", "learning"))
print(a.find("am"))
lang = "python"
time = 3
print("{0} is my favorite language, and i have learned {1} years.".format(lang, time))
print("%s is my favorite language, and i have learned %d years." % (lang, time))

str1 = "192.168.9.37"
print(str1.split("."))

str2 = "coohx  merlin  dev    ops   devops  linux"
print(str2.split(maxsplit=2))

str3 = ["192", "168", "9", "37"]
print(".".join(str3))
str4 = "abcdefg"
print(str4[0:3])
print(str4[0:])
print(str4[:4])
print(str4[:-1])
print(str4[-1:])
print(str4[:])
print(str4[0::2])

print(str4.startswith("abc"))
print(str4.endswith("efg"))

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# 删除列表元素‘ducati’
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'honda']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)
# print(motorcycles.pop(2))
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'honda']
print(motorcycles.index("yamaha"))

cars = ['bmw', 'audi', 'toyota', 'tesla']
for car in cars:
    cars[cars.index(car)] = car.title()
print(cars)
cars.reverse()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

print(sorted(cars))
print(cars)

print(sorted(cars, reverse=True))
print(cars)

members = ('merlin', 'sky', 'kaiter', 'zhenpin', 'wheez',)
print(members.count("sky"))
print(members[3])


b=["a",20,10,55,90]
print(type(b[0]))




