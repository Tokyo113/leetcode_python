#coding:utf-8
'''
@Time: 2019/10/20 16:34
@author: Tokyo
@file: code_17_RotateMatrix.py
@desc:转圈打印矩阵
'''

def rotateMatrix(arr):
    """
    左上角（lr, lc）, 右下角（rr, rc）
    :param arr:
    """
    lr, lc = 0, 0
    rr, rc = len(arr)-1, len(arr[0])-1
    while(lr <= rr and lc <= rc):
        printedge(arr, lr, lc, rr, rc)
        lr += 1
        lc += 1
        rr -= 1
        rc -= 1
    print("")

def printedge(arr, lr, lc, rr, rc):
    # 先考虑边界条件，只有一行或一列
    if lr == rr:
        for i in range(lc, rc+1):
            print(arr[lr][i], end=" ")
    elif lc == rc:
        for i in range(lr, rr+1):
            print(arr[i][lc], end=" ")
    else:
        curC = lc
        curR = lr
        while (curC < rc):
            print(arr[lr][curC], end=" ")
            curC += 1
        while (curR < rr):
            print(arr[curR][curC], end=" ")
            curR += 1
        while (curC > lc):
            print(arr[curR][curC], end=" ")
            curC -= 1
        while (curR > lr):
            print(arr[curR][curC], end=" ")
            curR -= 1

if __name__ == '__main__':
    a = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    b = [[1,2,3,4,5]]
    c = [[1],[2],[3]]
    rotateMatrix(a)
    rotateMatrix(b)
    rotateMatrix(c)
