#coding:utf-8
'''
@Time: 2020/3/12 23:12
@author: Tokyo
@file: code_20_NumDinstinct.py
@desc:
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

示例 1:

输入: S = "rabbbit", T = "rabbit"
输出: 3
解释:

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
示例 2:

输入: S = "babgbag", T = "bag"
输出: 5
解释:

如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。
(上箭头符号 ^ 表示选取的字母)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

动态规划
从左往右模型
1.s[i]!=t[j]，匹配不上，i+= 1直接过
2.若相等：
    要么i+=1，j+=1，匹配上了，看后续有几个
    要么只是i+=1,继续用后面的匹配
basecase:
j匹配完了
i匹配完了j没完
'''

def numDistinct(s, t):
    if s is None or t is None:
        return 0
    return process(s,t, 0, 0)

def process(s,t, i, j):
    # basecase,
    # j只要配完了，就返回1
    if j == len(t):
        return 1
    # j没配完，但i已经没了，返回0
    if i == len(s):
        return 0

    cnt = 0
    if s[i] == t[j]:
        cnt = process(s,t,i+1,j+1)+process(s,t,i+1,j)
    else:
        cnt = process(s,t,i+1,j)
    return cnt

def numDistinctDP(s,t):
    if s is None or t is None:
        return 0
    dp = [[0 for i in range(len(t)+1)] for i in range(len(s)+1)]
    for i in range(0, len(s)+1):
        dp[i][len(t)] = 1
    for j in range(0,len(t)):
        dp[len(s)][j] = 0
    for i in range(len(s)-1, -1, -1):
        for j in range(len(t)):
            dp[i][j] = dp[i+1][j]
            if s[i] == t[j]:
                dp[i][j] += dp[i+1][j+1]
    return dp[0][0]

def numDistinct(s, t):
    '''
    使用空间压缩技巧，更快
    一维数组
    :param s:
    :param t:
    :return:
    '''
    if s is None or t is None:
        return 0
    dp = [0 for i in range(len(t) + 1)]
    dp[len(t)] = 1
    for i in range(len(s) - 1, -1, -1):
        for j in range(0, len(t)):
            if s[i] == t[j]:
                dp[j] += dp[j + 1]
    return dp[0]

if __name__ == '__main__':
    s = "babgbag"
    t = 'bag'
    print(numDistinct(s,t))
    s1 = 'rabbbit'
    s2 = 'rabit'
    print(numDistinct(s1,s2))
    print(numDistinctDP(s1,s2))