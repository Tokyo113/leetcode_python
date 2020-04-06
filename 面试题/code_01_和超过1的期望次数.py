#coding:utf-8
'''
@Time: 2020/4/4 12:06
@author: Tokyo
@file: code_01_和超过1的期望次数.py
@desc:
从(0,1)中随机取数,期望情况下取多少个数才能让和超过1.

做10000次实验，最终结果是e
'''


def possibility():
    import random
    p = 0
    for i in range(10000):
        res = 0
        cnt = 0
        while res<=1:
            res += random.random()
            cnt += 1
        p += cnt
    return p/10000

if __name__ == '__main__':
    a = possibility()
    print(a)

