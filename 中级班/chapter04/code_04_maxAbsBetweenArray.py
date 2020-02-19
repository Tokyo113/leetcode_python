#coding:utf-8
'''
@Time: 2020/2/16 10:01
@author: Tokyo
@file: code_04_maxAbsBetweenArray.py
@desc:
给定一个数组arr长度为N，你可以把任意长度大于0且小于N的前缀作为左部分，剩下的
作为右部分。但是每种划分下都有左部分的最大值和右部分的最大值，请返回最大的，
左部分最大值减去右部分最大值的绝对值。
'''

def maxAbs1(arr):
    if len(arr) <= 1:
        return 0
    if len(arr) == 2:
        return abs(arr[0]-arr[1])
    res = float('-inf')
    for i in range(1, len(arr)):
        ans = abs(max(arr[:i])-max(arr[i:]))
        res = max(ans, res)

    return res

def maxAbs2(arr):
    '''
    通过分析问题待求的标准得到优化
    直接返回arr最大值与首尾相减的最大abs即可
    :param arr:
    :return:
    '''
    if len(arr) <= 1:
        return 0
    maxValue = max(arr)
    return max(maxValue-arr[0], maxValue-arr[-1])

def generateRandomArray(maxValue, maxSize):
    import random
    return [int((maxValue+1)*random.random())- int((maxValue+1)*random.random()) for i in range(int((maxSize+1)*random.random()))]


if __name__ == '__main__':
    testtimes = 100
    maxValue = 50
    maxSize = 10
    succeed = True
    for i in range(testtimes):
        arr = generateRandomArray(maxValue, maxSize)
        a = maxAbs1(arr)
        b = maxAbs2(arr)
        if a != b:
            print(arr)
            print(a, b)
            print('fucked')
            break
