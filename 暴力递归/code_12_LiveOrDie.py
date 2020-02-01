#coding:utf-8
'''
@Time: 2019/12/11 11:19
@author: Tokyo
@file: code_12_LiveOrDie.py
@desc:
'''


def BobDie1(n,m,i,j,k):
    total = 4**k
    live = process(n,m,i,j,k)
    return live/total


def process(n,m,i,j,step):
    '''
    暴力递归方法，返回走k步后存活的方法数
    :param n:
    :param m:
    :param i:
    :param j:
    :param step:
    :return:
    '''
    if i < 0 or i >= n or j < 0 or j >= m:
        return 0
    # i和j都没越界
    if step == 0:
        return 1

    return process(n,m,i-1, j, step-1)+process(n,m,i+1, j, step-1)\
           +process(n,m,i,j-1, step-1)+process(n,m,i,j+1,step-1)


def BobDie2(n, m, row, col, K):
    if row<0 or row>=n or col<0 or col>=m:
        return 0
    dp = [[[0 for i in range(K + 1)] for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j][0] = 1
    # 按层遍历
    for k in range(1, K + 1):
        for i in range(n):
            for j in range(m):
                dp[i][j][k] = getValue(n,m,i-1,j,k-1, dp)+getValue(n,m,i+1,j,k-1,dp)\
                              +getValue(n,m,i,j+1,k-1,dp)+getValue(n,m,i,j-1,k-1,dp)


    return dp[row][col][K]/(4**K)


def getValue(n, m, i, j, k, dp):
    if i < 0 or i >= n or j < 0 or j >= m:
        return 0
    return dp[i][j][k]





if __name__ == '__main__':
    N = 10
    M = 10
    i = 3
    j = 7
    K = 5
    print(BobDie1(N,M,i,j,K))
    print(BobDie2(N,M,i,j,K))