#coding:utf-8
'''
@Time: 2020/2/14 18:12
@author: Tokyo
@file: code_02_minPathSum.py
@desc:
动态规划的空间压缩技巧
给你一个二维数组matrix，其中每个数都是正数，要求从左上角走到右下角。每
一步只能向右或者向下，沿途经过的数字要累加起来。最后请返回最小的路径和。

本题思路：
暴力递归--->动态规划--->压缩空间技巧
类似题目：
leetcode62
注意深拷贝和浅拷贝的问题
对于二维数组，只使用copy还是会改变原数组，相当于浅拷贝
内层list还是指向同一引用reference

'''

def minPathSum1(arr):
    if arr is None or arr == []:
        return
    n = len(arr)
    m = len(arr[0])
    return process(arr, n-1, m-1)

def process(arr, i, j):
    if i == 0 and j == 0:
        return arr[i][j]
    if i == 0:
        return arr[i][j]+process(arr,i,j-1)
    if j == 0:
        return arr[i][j] + process(arr,i-1, j)
    return arr[i][j] + min(process(arr, i-1, j), process(arr, i, j-1))


def minPathSumDP(arr):
    if arr is None or arr == []:
        return
    n = len(arr)
    m = len(arr[0])

    dp = [[0 for i in range(m)]for i in range(n)]
    dp[0][0] = arr[0][0]
    for col in range(1, m):
        dp[0][col] = arr[0][col] + dp[0][col-1]
    for row in range(1, n):
        dp[row][0] = arr[row][0]+ dp[row-1][0]

    for i in range(1, n):
        for j in range(1,m):
            dp[i][j] =arr[i][j]+ min(dp[i-1][j],dp[i][j-1])

    return dp[n-1][m-1]


def minPathSumDPII(arr):
    if arr is None or arr == []:
        return
    n = len(arr)
    m = len(arr[0])
    dp = arr[0]

    for col in range(1, m):
        dp[col] += dp[col-1]
    for i in range(1,n):
        for j in range(m):
            if j == 0:
                dp[j] += arr[i][j]
            else:
                dp[j] = arr[i][j]+min(dp[j-1], dp[j])
    return dp[m-1]


if __name__ == '__main__':
    m = [[1, 3, 5, 9],
         [8, 1, 3, 4],
         [5, 0, 6, 1],
         [8, 8, 4, 0]]
    print(minPathSum1(m))
    print(minPathSumDP(m))

    print(minPathSumDPII(m))


