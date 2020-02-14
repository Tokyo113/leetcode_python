#coding:utf-8
'''
@Time: 2020/2/13 16:31
@author: Tokyo
@file: code_05_printMatrixSpiralOrder.py
@desc:
用螺旋的方式打印矩阵，比如如下的矩阵
0 1 2 3
4 5 6 7
8 9 10 11
打印顺序为：0 1 2 3 7 11 10 9 8 4 5 6
'''


def spiralMatrix(arr):
    if arr is None or arr == []:
        return
    n = len(arr)
    m = len(arr[0])
    lr,lc = 0, 0
    rr, rc = n-1, m-1
    while lr <= rr:
        printEdge(lr,lc,rr,rc, arr)
        lr += 1
        lc += 1
        rr -= 1
        rc -= 1
    print('')


def printEdge(lr,lc,rr,rc, arr):

    if lr == rr:
        for i in range(lc, rc+1):
            print(arr[lr][i], end=" ")
        return
    if lc == rc:
        for i in range(lr,rr+1):
            print(arr[i][lc],end=' ')
        return
    for i in range(lc, rc):
        print(arr[lr][i], end=' ')
    for i in range(lr, rr):
        print(arr[i][rc], end=" ")
    for i in range(rc, lc, -1):
        print(arr[rr][i], end=" ")
    for i in range(rr,lr, -1):
        print(arr[i][lc], end=' ')
    return


if __name__ == '__main__':
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    b = [[1, 2, 3, 4, 5]]
    c = [[1], [2], [3]]
    spiralMatrix(a)
    spiralMatrix(b)
    spiralMatrix(c)
