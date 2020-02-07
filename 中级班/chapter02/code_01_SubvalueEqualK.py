#coding:utf-8
'''
@Time: 2020/2/7 17:26
@author: Tokyo
@file: code_01_SubvalueEqualK.py
@desc:
给定一个数组arr，求差值为k的去重数字对。
eg:
arr = [3,2,5,7,0,0,0]
k = 2
去重数字对就是
(0,2),(3,5),(5,7)

'''


def numPairs(arr, k):
    arr_set = set(arr)
    res = []
    for i in arr_set:
        if i+k in arr_set:
            res.append((i,i+2))
    return res

if __name__ == '__main__':
    arr = [3,5,6,0,1,7,2]
    k = 2
    print(numPairs(arr, k))