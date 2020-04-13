#coding:utf-8
'''
@Time: 2020/4/3 13:47
@author: Tokyo
@file: code.py
@desc:
'''

def findNum(arr):
    if arr is None or arr == []:
        return -1
    import math

    for i in range(1,len(arr)):
        dif = arr[i]-arr[i-1]
        if dif <= 0:
            return -1
        if i == 1:
            res = dif
        else:
            res = math.gcd(res,dif)
    return res


def check(x, y, k):
    res = 0
    while x != 0:
        res += x % 10
        x = x / 10
    while y != 0:
        res += y % 10
        y /= 10
    print(res)
    return True if res <= k else False
if __name__ == '__main__':
    # print(findNum([5,5,5]))
    print(check(0,1,1))

