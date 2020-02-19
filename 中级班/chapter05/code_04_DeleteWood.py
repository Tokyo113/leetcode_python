#coding:utf-8
'''
@Time: 2020/2/19 16:31
@author: Tokyo
@file: code_04_DeleteWood.py
@desc:
在迷迷糊糊的大草原上，小红捡到了n根木棍，第i根木棍的长度为i，
小红现在很开心。想选出其中的三根木棍组成美丽的三角形。
但是小明想捉弄小红，想去掉一些木棍，使得小红任意选三根木棍都不能组成
三角形。
请问小明最少去掉多少根木棍呢？
给定N，返回至少去掉多少根？
'''

def triangleWood(n):
    '''
    小于等于n的斐波那契数列有几项
    :param n:
    :return:
    '''
    if n < 4:
        return 0
    num = 3
    fib1 = 2
    fib2 = 3
    while fib2+fib1<=n:
        fib2 += fib1
        fib1 = fib2-fib1
        num += 1
    # num是至多保留几根，n-num是至少去掉几根
    return n-num


if __name__ == '__main__':
    print(triangleWood(8))
