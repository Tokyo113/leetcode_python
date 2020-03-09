#coding:utf-8
'''
@Time: 2020/3/7 15:40
@author: Tokyo
@file: code_08_cuttingRope.py
@desc:

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段
（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m]
可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，
此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

'''


def cuttingRope(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    dp = [0 for i in range(n + 1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    for i in range(4, n+1):
        res = 0
        for j in range(1, i):

            res = max(dp[j] * dp[i - j], res)
        dp[i] = res
    return dp[n]


def baoli(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    res = 0
    for i in range(1, n):
        tmp = cuttingRope(n-i)
        if n-i <= 3:
            tmp = n-i
        if i >= 1 and i <= 3:
            res = max(res, i*tmp)
        else:
            res = max(res, cuttingRope(i)*tmp)
    return res


def greedy(n):
    '''
    贪心算法
    尽可能取长度为3的（长度大于5时）
    :param n:
    :return:
    '''
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    res = 1
    while n >= 5:
        n -= 3
        res *= 3
    return res*n



if __name__ == '__main__':
    print(cuttingRope(10))
    print(baoli(18))
    print(greedy(18))