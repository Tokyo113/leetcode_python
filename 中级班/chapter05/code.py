#coding:utf-8
'''
@Time: 2020/3/23 14:36
@author: Tokyo
@file: code.py
@desc:
'''
MOD = 1000000007


def matrixPower(A, n):
    if n == 1:
        return A
    Temp = matrixPower(A, n // 2)
    if n % 2 == 1:
        return matrixMul(matrixMul(Temp, Temp), A)
    return matrixMul(Temp, Temp)


def matrixMul(a, b):
    if len(a[0]) != len(b):
        return
    res = [[0 for i in range(len(b))] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                res[i][j] += a[i][k] * b[k][j]
    return res


N = int(input())
if N == 1:

    print(1 % MOD)
elif N == 2:
    print(2 % MOD)
else:
    res = matrixPower([[1, 1], [1, 0]], N - 2)
    print((2 * res[0][0] + res[1][0]) % MOD)
