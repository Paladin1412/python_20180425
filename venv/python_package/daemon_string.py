#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/7/17 21:28
# @Author : merlinhuang
# @File   : daemon_string.py

"""
string模块：包含用于处理文本的常量和类。
自 2.0 开始，之前在 string 模块中实现的函数都迁移到了 str 和 unicode 对象中，作为方法呈现
"""

import string

### 常用方法
str = "Learing python, you can be powerful!"
# 把字符串的首字母大写
print(str.capitalize())

# 将原字符串用空格填充成一个长度为width的字符串，原字符串内容居中
print(str.center(50))
# 指定字符‘-’填充
print(str.center(50, '-'))

# 返回字符串在str中出现的次数
print(str.count('o'))
print(str.count('python'))

# 以指定编码格式编码字符串--> byte
print(type(str.encode(encoding='UTF-8', errors='strict')))

# 以指定编码格式解码字符串
str1 = "中国"
string1 = str1.encode(encoding='utf-8', errors='ignore').decode(encoding='utf-8', errors='strict')
print(string1)

# 判断字符串是否以字符串s是结尾
# str.endswith(s)
print(str.endswith('!'))
print(str.endswith('ful!'))

# 返回字符串s在字符串str中的位置索引，索引从0开始,没有则返回-1
# str.find(s)
print(str.find('L'))
print(str.find('!'))
print(str.find('K'))

# 从右边开始查找字符串s在字符串str中的位置索引
# str.rfind(s)
print("'ABC', A is {0} alpha.".format("ABC".rfind('A')))
print("'ABC', B is {0} alpha.".format("ABC".rfind('B')))
print("'ABC', C is {0} alpha.".format("ABC".rfind('C')))

# 和find()方法一样，但是如果s不存在于str中则会抛出异常
# str.index(s)
print(str.index('you'))

# 从右边开始,返回字符串s在字符串str中的位置索引,但是如果s不存在于str中则会抛出异常
# str.rindex(s)
print("'ABC', A is {0} alpha.".format("ABC".rindex('A')))

# 如果str至少有一个字符并且都是字母或数字则返回True,否则返回False
str2 = "12345667890abcdefghijklmnupqrstwxyz"
print(str2.isalnum())

# 如果str至少有一个字符并且都是字母则返回True,否则返回False
str3 = "asdfASDF"
print(str3.isalpha())

# 如果str只包含数字则返回 True 否则返回 False
str4 = "12334242345"
print("str4 all is digit: {0}".format(str4.isdigit()))

# 如果str存在区分大小写的字符，并且都是小写则返回True 否则返回False
str5 = "asdf"
print("str5 all is lower: ", str5.islower())

# 如果str中只包含空格，则返回 True，否则返回 False
str6 = "    "
print("str6 all is space: ", str6.isspace())

# 如果str是标题化的(单词首字母大写)则返回True，否则返回False
str7 = "Python Won"
print(str7.istitle())

# 如果str存在区分大小写的字符，并且都是大写则返回True 否则返回False
print("ABC".isupper())

# 返回一个原字符串左对齐的并使用空格填充至长度width的新字符串
print("lift just".ljust(20))
print("lift just".ljust(20, '*'))

# 转换str中所有大写字符为小写
print("ABC".lower())

# 去掉str左边的不可见字符
print("   DEL   ".lstrip() + "test")

# 用s将str切分成三部分
# str.partition(s)
print("I am learing python".partition('lear'))
# ('I am ', 'lear', 'ing python')

# 将字符串str中的a替换成b
# str.replace(a, b)
print('Ops should can write pyton'.replace('should', 'must'))

# 返回一个原字符串右对齐的并使用空格填充至长度width的新字符串
# str.rjust(width)
print("right just".rjust(20))
print("right just".rjust(20, '*'))

# 类似于 partition()函数,不过是从右边开始查找
# str.rpartition(s)
print("I am learing python learing!".rpartition('lear'))
# ('I am learing python ', 'lear', 'ing!')
print("I am learing python learing!".partition('lear'))
# ('I am ', 'lear', 'ing python learing!')

# 去掉str右边的不可见字符
# str.rstrip()
print("  ABC   ".rstrip() + "test")


# 以s为分隔符切片str
# str.split(s)
print("192.168.1.2".split('.'))
# ['192', '168', '1', '2']
print("a love b".split('o'))
# ['a l', 've b']


# 按照行分隔，返回一个包含各行作为元素的列表
# str.splitlines()
print(
"""aaaa
bbbb
cccc
""".splitlines())
# ['aaaa', 'bbbb', 'cccc']


# 检查字符串str是否是以s开头，是则返回True，否则返回False
# str.startswith(s)
print("Python is cool".startswith('Python'))

# 去掉字符串两端的空白
# str.strip()
print("  NO SPACE  ".strip())

# 返回"标题化"的str,所有单词都是以大写开始，其余字母均为小写
# str.title()
print("I am learing python learing!".title())

# 返回str所有字符为大写的字符串
# str.upper()
print("asdf".upper())

# 返回长度为 width 的字符串，原字符串str右对齐，前面填充0
# str.zfill(width)
print("zero fill string".zfill(50))

### string模块的字符串常量

# 小写字母'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_lowercase)

# 大写的字母'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.ascii_uppercase)

# ascii_lowercase和ascii_uppercase常量的连接串
print(string.ascii_letters)

# 数字0到9的字符串:'0123456789'
print(string.digits)

# 字符串'0123456789abcdefABCDEF'
print(string.hexdigits)

# 字符串'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(string.letters)

# 小写字母的字符串'abcdefghijklmnopqrstuvwxyz'
# print(string.lowercase)


# 字符串'01234567'
print(string.octdigits)

# 所有标点字符
print(string.punctuation)

# 可打印的字符的字符串。包含数字、字母、标点符号和空格
print(string.printable.encode('utf-8'))

# 大写字母的字符串'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(string.uppercase)

# 空白字符 '\t\n\x0b\x0c\r '
print(string.whitespace.encode('utf-8'))


### string保留的函数
# capwords() 和 maketrans() 这两个函数没有从 string 中移除。

# capwords()函数将字符串中每个字的首字母大写
str = "string is powerful"
str = string.capwords(str)
print(str)


# python2
# maketrans() 函数会先创建一个转换表，然后 translate() 方法会通过查询该转换表，将一个字符转换成另一个字符。这种方式比多次调用 replace() 便捷
# 'abcdefgtest'.translate(string.maketrans('abcdefg', 'ABCDEFG'))


### string 模板 string.Template

from string  import Template

# 自定义模板, $标识模板中的变量
temp = Template('$who like $what')
print(temp.substitute(who='i', what='python'))

# safe_substitute() 方法, 如果没有为模板提供足够的参数值，也不会抛出异常，缺少值的变量表达式会在结果中原样保留
print(temp.safe_substitute(who='jack'))
# jack like $what

# 给变量加上{}, 与周围的字符区分开来
print(Template("${who}LikePython").safe_substitute(who='I'))

# 通过继承string.Template, 重写变量delimiter(定界符)和idpattern(替换格式), 定制不同形式的模板
import string

class MyTemplate(string.Template):
    """重写Template中的属性delimiter和idpattern,自定义高级模板"""
    # 更改定界符为%
    delimiter = '%'
    # 替换模式必须包含下划线
    idpattern = '[a-z]+_[a-z]+'

my_temp = """
    Delimiter: $de
    Replaced: %with_underscored
    Ignored: %notunderscored
"""

substitute = {
    'de': 'not replaced',
    'with_underscored': 'replaced',
    'notunderscored': 'not replaced',
}

# 使用原来的Template模板进行渲染
# 只替换界定符 $ 标识的变量
print(string.Template(my_temp).safe_substitute(substitute))

# 使用重写后的MyTemplate模板模板进行渲染
# 只替换界定符 % 标识的并且变量名必须包含下划线
print(MyTemplate(my_temp).safe_substitute(substitute))
