#coding:utf-8
'''
@Time: 2020/3/26 10:33
@author: Tokyo
@file: code_01_LongestSubstr.py
@desc:
给定两个字符串str1和str2，输出连个字符串的最长公共子序列。如过最长公共子序列为空，则输出-1。
输入描述:
输出包括两行，第一行代表字符串str1，第二行代表str2。\left( 1\leq length(str1),length(str2) \leq 5000\right)(1≤length(str1),length(str2)≤5000)
输出描述:
输出一行，代表他们最长公共子序列。如果公共子序列的长度为空，则输出-1。
示例1
输入
复制
1A2C3D4B56
B1D23CA45B6A
输出
123456


简化问题：
先求最长公共子序列的长度
'''


def substr(s1,s2):
    '''
    先得到最长子序列的长度，然后由dp反推子序列
    :param s1:
    :param s2:
    :return:
    '''
    if s1 == '' or s2 == '':
        return -1
    n = len(s1)
    m = len(s2)
    dp = [[0 for i in range(m)] for i in range(n)]
    dp[0][0] = 1 if s1[0] == s2[0] else 0
    for i in range(1,n):
        dp[i][0] = 1 if s1[i] == s2[0] else dp[i-1][0]
    for j in range(1,m):
        dp[0][j] = 1 if s1[0] == s2[j] else dp[0][j-1]

    for i in range(1,n):
        for j in range(1,m):
            if s1[i] == s2[j]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
    printMatrix(dp)
    res = dp[n-1][m-1]
    final = []
    i1,i2 = n-1,m-1
    while res > 0:
        if s1[i1] == s2[i2]:
            final.append(s1[i1])
            i1 -= 1
            i2 -=1
            res -= 1
        else:
            if dp[i1-1][i2-1] == dp[i1][i2]:
                i1 -= 1
                i2 -= 1
            elif dp[i1][i2-1] == dp[i1][i2]:
                i2 -= 1
            else:
                i1 -= 1
    print(final)
    return ''.join(final[::-1])








def printMatrix(arr):
    for i in arr:
        print(i)




if __name__ == '__main__':
    s1 = '12345'
    s2 = 'asdgr'
    print(substr(s1,s2))