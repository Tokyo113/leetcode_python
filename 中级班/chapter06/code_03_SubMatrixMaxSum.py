#coding:utf-8
'''
@Time: 2020/2/22 10:17
@author: Tokyo
@file: code_03_SubMatrixMaxSum.py
@desc:
给定一个整型矩阵，返回子矩阵的最大累计和。

'''

def matrixMaxSum(arr):
    if arr is None or arr == []:
        return None
    max1 = float('-inf')
    for i in range(len(arr)):
        res = [0 for i in range(len(arr[0]))]
        for j in range(i, len(arr)):
            cur = 0

            for k in range(len(arr[0])):
                res[k] += arr[j][k]
                cur += res[k]
                max1 = max(max1, cur)
                if cur < 0:
                    cur = 0


    return max1

if __name__ == '__main__':
    arr = [ [-90, 48, 78], [64, -40, 64], [-81, -7, 66]]
    print(matrixMaxSum(arr))





