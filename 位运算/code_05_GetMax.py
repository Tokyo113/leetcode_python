#coding:utf-8
'''
@Time: 2019/12/5 19:53
@author: Tokyo
@file: code_05_GetMax.py
@desc:

给定两个有符号32位整数a和b，返回a和b中较大的。
【要求】
不用做任何比较和判断。
'''


def sign(x):
    return (x>>31)&1


def getMax1(a,b):
    c = a-b
    sca = sign(c)
    scb = flip(sca)
    return  a*sca+b*scb