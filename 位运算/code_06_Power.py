#coding:utf-8
'''
@Time: 2019/12/5 20:39
@author: Tokyo
@file: code_06_Power.py
@desc:

判断一个32位正数是不是2的幂、4的幂

'''

def is2Power(num):
    return num&(num-1) == 0

def is4Power(num):
    return (num&(num-1) == 0) and num&(0x55555555) != 0


if __name__ == '__main__':
    print(is2Power(256))
    print(is4Power(4))