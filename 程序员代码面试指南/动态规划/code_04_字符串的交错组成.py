#coding:utf-8
'''
@Time: 2020/3/30 10:05
@author: Tokyo
@file: code_04_字符串的交错组成.py
@desc:
给定三个字符串str1、str2 和aim,如果aim包含且仅包含来自str1和str2的所有字符，而且在aim中属于str1的字符之间保持原来在str1中的顺序属于str2的字符之间保持原来在str2中的顺序，那么称aim是str1和str2的交错组成。实现一个函数，判断aim是否是str1和str2交错组成，如果是请输出“YES”，否则输出“NO”。

输入描述:
输出三行，分别表示三个字符串str1，str2和aim。1 \leq length\left ( str1 \right ),length\left ( str2 \right ) \leq 5000 ,1 \leq length\left(aim \right) \leq100001≤length(str1),length(str2)≤5000,1≤length(aim)≤10000 ， length()length()表示字符串长度。
输出描述:
输出“YES”或者“NO”。（不包含引号）
'''


def crossStr(s1,s2,aim):
    if len(aim) != len(s1)+len(s2):
        return False
    return process(s1,s2,aim,0,0,0)

def process(s1,s2,aim,cur,i1,i2):
    if i1 == len(s1) and i2 == len(s2):
        return True if cur == len(aim) else False
    if i1 == len(s1):
        return process(s1,s2,aim,cur+1,i1,i2+1) if aim[cur] == s2[i2] else False
    if i2 == len(s2):
        return process(s1,s2,aim,cur+1,i1+1,i2) if aim[cur] == s1[i1] else False
    if aim[cur] == s1[i1] and aim[cur] == s2[i2]:
        return process(s1,s2,aim,cur+1,i1+1,i2) or process(s1,s2,aim,cur+1,i1,i2+1)
    if aim[cur] == s1[i1]:
        return process(s1,s2,aim,cur+1,i1+1,i2)
    if aim[cur] == s2[i2]:
        return process(s1,s2,aim,cur+1,i1,i2+1)
    return False


def crossStr2(s1,s2,aim):
    if len(aim) != len(s1)+len(s2):
        return False
    n,m = len(s1),len(s2)
    dp = [[0 for i in range(m+1)] for i in range(n+1)]
    dp[0][0] = True
    for i in range(1,n+1):
        dp[i][0] = dp[i-1][0] if aim[i-1] == s1[i-1] else False
    for j in range(1,m+1):
        dp[0][j] = dp[0][j-1] if aim[j-1] == s2[j-1] else False

    for i1 in range(1,n+1):
        for i2 in range(1,m+1):
            if aim[i1+i2-1] == s1[i1-1] and aim[i1+i2-1] == s2[i2-1]:
                dp[i1][i2] = dp[i1-1][i2] or dp[i1][i2-1]
            elif aim[i1+i2-1] == s1[i1-1]:
                dp[i1][i2] = dp[i1-1][i2]
            elif aim[i1+i2-1] == s2[i2-1]:
                dp[i1][i2] = dp[i1][i2-1]
            else:
                dp[i1][i2] = False
    return dp[n][m]


def crossStr3(s1,s2,aim):
    if len(aim) != len(s1)+len(s2):
        return False
    n,m = len(s1),len(s2)
    dp = [0 for i in range(m+1)]
    dp[0] = True

    for j in range(1,m+1):
        dp[j] = dp[j-1] if aim[j-1] == s2[j-1] else False

    for i1 in range(1,n+1):
        for i2 in range(0,m+1):
            if i2 == 0:
                dp[0] = dp[0] if aim[i1-1] == s1[i1-1] else False
            else:
                if aim[i1+i2-1] == s1[i1-1] and aim[i1+i2-1] == s2[i2-1]:
                    dp[i2] = dp[i2] or dp[i2-1]
                elif aim[i1+i2-1] == s1[i1-1]:
                    dp[i2] = dp[i2]
                elif aim[i1+i2-1] == s2[i2-1]:
                    dp[i2] = dp[i2-1]
                else:
                    dp[i2] = False
    return dp[m]

if __name__ == '__main__':
    print(crossStr('ab','','ab'))
    print(crossStr2('abc', '12', 'c1a2b'))
    print(crossStr3('abc', '12', 'c1a2b'))