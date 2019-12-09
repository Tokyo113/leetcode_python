#coding:utf-8
'''
@Time: 2019/12/6 10:51
@author: Tokyo
@file: code_07_AddMinusMultipleDivide.py
@desc:
给定两个有符号32位整数a和b，不能使用算术运算符，分别实现a和b的加、减、乘、除运
算
【要求】
如果给定a、b执行加减乘除的运算结果就会导致数据的溢出，那么你实现的函数不必对此
负责，除此之外请保证计算过程不发生溢出
'''


def add(a, b):
    sum1 = a
    while b != 0:
        sum1 = a^b
        b = (a&b)<<1
        a = sum1


    return sum1

def minus(a,b):
    '''
    减法就是加上相反数
    :param a:
    :param b:
    :return:
    '''
    return add(a,add(~b, 1))


def multi(a,b):
    res = 0

    while b !=0:
        if b&1 != 0:
            res = add(res,a)
        a = a << 1
        b = b >> 1

    return res

def isNeg(a):
    return a<0

def negNum(a):
    return add(~a,1)


def div(a,b):
    x = negNum(a) if isNeg(a) else a
    y = negNum(b) if isNeg(b) else b
    res = 0
    for i in range(31,-1, -1):
        if ((x>>i) >= y):
            res |= (1<<i)
            x = minus(x,y<<i)
    return negNum(res) if isNeg(a)^isNeg(b) else res






if __name__ == '__main__':
    print(add(1,1))
    print(minus(8,9))
    print(multi(4,5))
    print(div(5,5))