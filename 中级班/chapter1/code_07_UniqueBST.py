#coding:utf-8
'''
@Time: 2020/2/6 22:36
@author: Tokyo
@file: code_07_UniqueBST.py
@desc:
给定一个非负整数n，代表二叉树的节点个数。返回能形成多少种不同的二叉树结构
同样的题换个说法：
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
对于二叉搜索树，一种结构只能有一种填充法，使得中序遍历递增
'''

def uniqueBST(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    res = 0
    for i in range(n):
        res += uniqueBST(i)*uniqueBST(n-i-1)
    return res

def uniqueBST_dp(n):
    if n < 2:
        return 1
    dp = [0 for i in range(n+1)]
    dp[0], dp[1], dp[2] = 1,1,2
    for i in range(3, n+1):
        for k in range(i):
            dp[i] += dp[k]*dp[i-k-1]

    return dp[n]





if __name__ == '__main__':
    print(uniqueBST(3))
    print(uniqueBST_dp(3))
    for i in range(0,13):
        if uniqueBST_dp(i) != uniqueBST(i):
            print('fucking fucked!!!')
            break
    print('wow,succeed!')



