#coding:utf-8
'''
@Time: 2020/4/12 16:45
@author: Tokyo
@file: code02.py
@desc:
'''


def getArr(n,k):

    arr = [1 for i in range(k)]
    print(arr)
    curSum = k
    for i in range(k,n+1):
        arr.append(curSum)
        curSum += arr[-1]
        curSum -= arr.pop(0)
    print(arr)
    return arr[-1]

if __name__ == '__main__':
    print(getArr(4,2))