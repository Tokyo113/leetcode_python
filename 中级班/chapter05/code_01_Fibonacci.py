#coding:utf-8
'''
@Time: 2020/2/19 11:27
@author: Tokyo
@file: code_01_Fibonacci.py
@desc:
求斐波那契数列的第N项
通过本题介绍同类题目的套路，斐波那契套路，
可以将时间复杂度由O(N)降低到O(logN)
1,1,2,3,5,8,13,......
F(N) = F(N-1)+F(N-2)
'''

def fib1(N):
    '''
    原始方法，O（N）
    :param N:
    :return:
    '''
    if N == 1 or N == 2:
        return 1
    return fib1(N-1)+fib1(N-2)

def fib2(N):
    '''
    O(logN)
    |F3,F2|=|F2,F1|*[[a,b],
                        [c,d]]
    所以，F（N）=（2*2行列式）^(n-2)然后取a+c
    :param N:
    :return:
    '''
    if N <= 0:
        return
    if N == 1 or N == 2:
        return 1
    arr = [[1,1], [1,0]]
    pp = matrixPower(arr, N-2)
    return pp[0][0]+pp[1][0]

def matrixPower(arr, n):
    res = [[0 for i in range(len(arr[0]))] for i in range(len(arr))]
    for i in range(len(arr)):
        res[i][i] = 1
    t = arr
    while n != 0:
        if n&1 == 1:
            res = matrixMultiple(res, t)
        t = matrixMultiple(t,t)
        n = n >> 1

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
    print(fib1(12))
    print(fib2(12))