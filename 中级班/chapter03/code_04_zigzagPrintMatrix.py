#coding:utf-8
'''
@Time: 2020/2/13 12:51
@author: Tokyo
@file: code_04_zigzagPrintMatrix.py
@desc:
用zigzag的方式打印矩阵，比如如下的矩阵
0 1 2 3
4 5 6 7
8 9 10 11
打印顺序为：0 1 4 8 5 2 3 6 9 10 7 11
'''

def zigzagPrint(arr):
    if arr is None or arr == []:
        return
    n = len(arr)
    m = len(arr[0])
    reverse = False
    ar,ac = 0, 0
    br,bc = 0, 0
    while ar != n:
        printEdge(arr, ar,ac,br,bc, reverse)
        if ac < m-1:
            ac += 1
        else:
            ar += 1
        if br < n-1:
            br += 1
        else:
            bc += 1
        reverse = ~reverse

def printEdge(arr, ar,ac,br,bc,reverse):
    if reverse:
        while ar <= br:
            print(arr[ar][ac], end=' ')
            ar += 1
            ac -= 1
    else:
        while br >= ar:
            print(arr[br][bc], end=" ")
            br -= 1
            bc += 1


if __name__ == '__main__':
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    zigzagPrint(a)








