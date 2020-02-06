#coding:utf-8
'''
@Time: 2020/2/5 10:10
@author: Tokyo
@file: code_06_Rand5toRand7.py
@desc:
给定一个函数f，可以1～5的数字等概率返回一个。请加工出1～7的数字等概率
返回一个的函数g。
给定一个函数f，可以a～b的数字等概率返回一个。请加工出c～d的数字等概率
返回一个的函数g。
给定一个函数f1，以p概率返回0，以1-p概率返回1。请加工出等概率返回0和1的
函数g1

这种题的通法：转换为二进制拼，先生成01发生器
'''
import random
def f():
    return int(random.random()*5)+1

def rand01():
    '''
    01发生器，等概率返回0和1
    注意只能利用f函数,1、2 返回0，4、5返回1，3重新来
    :return:
    '''
    while True:
        res = f()
        if res != 3:
            break
    return 0 if res < 3 else 1


def g():
    '''
    利用位运算先生成0~6，再加1
    :return:
    '''
    while True:
        res = (rand01()<<2)+(rand01()<<1)+(rand01())
        if res != 7:
        # 结果是7则重新来
            break
    return res+1


def f1():
    '''
    以p概率返回0，以1-p概率返回1
    you can change p to what you like, but it must be (0,1)
    :return:
    '''
    p = 0.88
    return 0 if random.random()<= p else 1

def g1():
    '''
    f1 生成01和10是等概率的，映射为0和1
    :return:
    '''
    while True:
        res1 = f1()
        if res1 != f1():
            break
    return res1


if __name__ == '__main__':
    print(g())