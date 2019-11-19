#coding:utf-8
'''
@Time: 2019/11/19 11:27
@author: Tokyo
@file: code_02_bitMap.py
@desc:
'''


def bitMap():
    # 整型数组
    arr = [0 for i in range(10)]
    # 想取得178位的状态
    i=178

    numIndex = 178/32
    bitIndex = 178%32

    # 拿到第178位的状态
    s = (arr[numIndex]>>(bitIndex)) & 1

    # 把178位的状态改为1
    arr[numIndex] = arr[numIndex] | (1<<bitIndex)

    # 把178位的状态改为0
    arr[numIndex] = arr[numIndex] & (~(1<<bitIndex))



