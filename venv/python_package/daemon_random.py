#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time   : 2018/6/11 21:23
# @Author : merlinhuang
# @File   : daemon_random.py


"""
random模块用于生成伪随机数
"""
import random

#### 基本方法

# 初始化随机数生成器。如果未提供a或者a=None，则使用系统时间为种子。如果a是一个整数，则作为新的种子。
# random.seed(a=None, version=2)

# 返回当前生成器的内部状态
# random.getstate()

# 传入一个先前利用getstate方法获得的状态对象，使得生成器恢复到这个状态。
# random.setstate(state)

# 返回一个不大于K位的Python整数（十进制），比如k = 10，则结果是0 ~ 2^10之间的整数。
# random.getrandbits(k)
print(random.getrandbits(2))


####  针对整数的方法

# [0, stop) 内的一个整数
# random.randrange(stop)
print(random.randrange(10))
# range的范围内随机选择一个整数,前开后闭
# random.randrange(start, stop[, step])
print(random.randrange(2, 101, 2))          # 2 - 100的偶数

# 返回一个a <= N <= b的随机整数N, 等同于randrange(a, b+1)
# random.randint(a, b)
print(random.randint(1, 4))


#### 针对序列类型的方法

# 从非空序列seq中随机选取一个元素. 如果seq为空则弹出IndexError异常.
# random.choice(seq)
seq1 = [1, 3, 5, 7, 9]
print(random.choice(seq1))
string = ['win', 'lose', 'draw']
print(random.choice(string))

# 3.6版本新增, 从population集群中随机抽取K个元素。weights是相对权重列表，cum_weights是累计权重，两个参数不能同时存在。
# random.choices(population, weights=None, *, cum_weights=None, k=1)


# 随机打乱序列x内元素的排列顺序，俗称“洗牌”。只能用于可变的序列
# random.shuffle(x[, random])
seq2 = [1, 3, 5, 7, 9]
random.shuffle(seq2)
print(seq2)

# 从population样本或集合中随机抽取K个不重复的元素形成新的序列。常用于不重复的随机抽样。返回的是一个新的序列，不会破坏原有序列,
# 如果k大于population的长度，则弹出ValueError异常。
# random.sample(population, k)
seq3 = (1, 3, 5, 7, 9, 1, 3, 4)
seq4 = random.sample(seq3, 6)
print(seq4)
print(seq3)

seq5 = random.sample(range(10000), k=10)
print(seq5)


####　真值分布

# 返回一个介于左闭右开[0.0, 1.0)区间的浮点数
# random.random()
print(random.random())
print(random.random())

# 返回一个介于a和b之间的浮点数x, a =< x < b。如果a>b，则是b到a之间的浮点数。这里的a和b都有可能出现在结果中
# random.uniform(a, b)
print(random.uniform(1.0, 1.1))
print(random.uniform(3, 1))


# 返回一个low <= N <=high的三角形分布的随机数。参数mode指明众数出现位置
# random.triangular(low, high, mode)

# β分布。返回的结果在0~1之间。
# random.betavariate(alpha, beta)


# 指数分布
# random.expovariate(lambd)

# 伽马分布
# random.gammavariate(alpha, beta)

# 高斯分布
# random.gauss(mu, sigma)


# 对数正态分布
# random.lognormvariate(mu, sigma)


# 正态分布
# random.normalvariate(mu, sigma)

# 卡帕分布
# random.vonmisesvariate(mu, kappa)

# 帕累托分布
# random.paretovariate(alpha)


# 可选择的生成器
# class random.SystemRandom([seed])
# 使用os.urandom()方法生成随机数的类，由操作系统提供源码，不一定所有系统都支持


# 生成一个包含大写字母A-Z和数字0-9的随机4位验证码的程序
import random

checkcode = ''
# 4个长度
for i in range(4):
    current = random.randrange(0,4)
    # 取字母
    if current != i:
        # 65 - 90 对应 A - z
        temp = chr(random.randint(65,90))
    # 取数字
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print(checkcode)


# 生成指定长度字母数字随机序列的代码

import random, string

def gen_random_string(length):
    # 数字的个数随机产生
    num_of_numeric = random.randint(1,length-1)
    # 剩下的都是字母
    num_of_letter = length - num_of_numeric
    # 随机生成数字
    numerics = [random.choice(string.digits) for i in range(num_of_numeric)]
    # 随机生成字母
    letters = [random.choice(string.ascii_letters) for i in range(num_of_letter)]
    # 结合两者
    all_chars = numerics + letters
    # 洗牌
    random.shuffle(all_chars)
    # 生成最终字符串
    result = ''.join([i for i in all_chars])
    return result

if __name__ == '__main__':
    print(gen_random_string(12))