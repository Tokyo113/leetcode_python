#coding:utf-8
'''
@Time: 2020/2/13 16:58
@author: Tokyo
@file: code_06_rotateMatrix.py
@desc:
给定一个正方形矩阵，只用有限几个变量，实现矩阵中每个位置的数顺时针转动
90度，比如如下的矩阵
0 1 2 3
4 5 6 7
8 9 10 11
12 13 14 15
矩阵应该被调整为：
12 8 4 0
13 9 5 1
14 10 6 2
15 11 7 3

'''


def rotateMatrix(arr):
    n = len(arr)
    m = len(arr[0])
    lr,lc = 0, 0
    rr, rc = n-1, m-1
    while lr < rr:
        rotateEdge(arr, lr,lc,rr,rc)
        lr += 1
        lc += 1
        rr -= 1
        rc -= 1

def rotateEdge(arr, lr,lc, rr,rc):


    for i in range(rc-lc):

        pp = arr[lr][lc+i]
        arr[lr][lc+i] = arr[rr-i][lc]
        arr[rr-i][lc] = arr[rr][rc-i]
        arr[rr][rc-i] = arr[lr+i][rc]
        arr[lr+i][rc] = pp
    return



def printMatrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end="\t")
        print("")


if __name__ == '__main__':
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13,14,15,16]]

    printMatrix(a)
    print("=================")
    rotateMatrix(a)


    printMatrix(a)
