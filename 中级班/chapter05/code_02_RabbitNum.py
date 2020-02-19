#coding:utf-8
'''
@Time: 2020/2/19 12:31
@author: Tokyo
@file: code_02_RabbitNum.py
@desc:
斐波那契套路同类题：
要求时间复杂度O(logN)
假设起初第一年有1只兔子，每年生出两只小兔子，小兔子过两年开始成熟
也开始生出小兔子，求第N年有多少只兔子
F(N) = F(N-1)+2*F(N-2)
这个是二阶的
进阶：
若兔子寿命为5年，求第N年有多少只？
F(N) = F(N-1)+2*F(N-2)-F(N-5)
五阶的
五阶也一样，公式是一样的，前面的系数不影响
求出五阶行列式即可
'''

def rabit1(N):
    if N == 1:
        return 1
    if N == 2:
        return 3
    return rabit1(N-1)+2*rabit1(N-2)


def rabit2(N):
    if N <= 0:
        return
    if N == 1:
        return 1
    if N == 2:
        return 3
    arr = [[1,1], [2,0]]
    pp = matrixPower(arr, N-2)
    return 3*pp[0][0]+pp[1][0]

def matrixPower(arr, n):
    res = [[0 for i in range(len(arr))] for i in range(len(arr))]
    for i in range(len(arr)):
        res[i][i] = 1
    t = arr
    while n !=0:
        if n&1 == 1:
            res = matrixMultiple(res, t)
        t = matrixMultiple(t,t)
        n = n >>1

    return res


def matrixMultiple(a, b):
    if len(a[0]) != len(b):
        print("Dimension error")
        return
    res = [[0 for i in range(len(b[0]))] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k]*b[k][j]

    return res



if __name__ == '__main__':
    print(rabit1(22))
    print(rabit2(22))
