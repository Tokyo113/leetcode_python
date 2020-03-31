#coding:utf-8
'''
@Time: 2020/3/26 11:49
@author: Tokyo
@file: code_02_LongestSubII.py
@desc:
给定两个字符串str1和str2,输出两个字符串的最长公共子串，如果最长公共子串为空，输出-1。
输入描述:
输入包括两行，第一行代表字符串srr1，第二行代表字符串str2。\left( 1\leq length(str1),length(str2) \leq 5000 \right)(1≤length(str1),length(str2)≤5000)
输出描述:
输出包括一行，代表最长公共子串。
示例1
输入
复制
1AB2345CD
12345EF
输出
复制
2345


本题是求子串，不是子序列！！！
同样也是先求dp表，然后反推子串
'''

def substr(s1,s2):
    '''
    i,j表示以是s1[i],s2[j]结尾的子串最长长度是多少
    :param s1:
    :param s2:
    :return:
    '''
    if s1 == '' or s2 == '':
        return -1
    n,m = len(s1),len(s2)
    dp = [[0 for i in range(m)] for i in range(n)]
    dp[0][0] = 1 if s1[0] == s2[0] else 0
    maxlen = 1
    for j in range(1,m):
        dp[0][j] = 1 if s1[0]==s2[j] else 0
    for i in range(1,n):
        dp[i][0] = 1 if s1[i] == s2[0] else 0
    for i in range(1,n):
        for j in range(1,m):
            if s1[i] == s2[j]:
                dp[i][j] += dp[i-1][j-1]+1
                maxlen = max(maxlen,dp[i][j])
            else:
                dp[i][j] = 0
    cur = 0
    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] == maxlen:
                cur = i

    return s1[cur-maxlen+1:cur+1]



if __name__ == '__main__':

    s1 = 'A1234B12345CD'
    s2 = '12345'
    print(substr(s1,s2))



