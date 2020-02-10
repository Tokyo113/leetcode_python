#coding:utf-8
'''
@Time: 2020/2/9 18:08
@author: Tokyo
@file: code_04_numToString.py
@desc:
将给定的数转换为字符串，原则如下：1对应 a，2对应b，…..26对应z，例如12258
可以转换为"abbeh", "aveh", "abyh", "lbeh" and "lyh"，个数为5，编写一个函
数，给出可以转换的不同字符串的个数
'''

def convertString(str):
    if str == '' or str is None:
        return 0
    return process(str, 0)

def process(str, i):
    if i == len(str):
        return 1
    if str[i] == '0':
        return 0
    if str[i] == '1':
        res = process(str,i+1)
        res += process(str,i+2) if i+2 <= len(str) else 0
    elif str[i] == '2':
        res = process(str,i+1)
        res += process(str,i+2) if i+2 <= len(str) and int(str[i+1]) < 7 else 0
    else:
        res = process(str, i+1)

    return res

def convertDP(str):
    dp = [0 for i in range(len(str)+1)]
    dp[len(str)] = 1

    for i in range(len(str)-1, -1, -1):
        dp[i] = dp[i+1] if str[i] != '0' else 0
        if str[i] == '1' and i+2 <= len(str):
            dp[i] += dp[i+2]
        elif str[i] == '2' and i+2 <= len(str) and int(str[i+1]) < 7:
            dp[i] += dp[i+2]

    return dp[0]




if __name__ == '__main__':
    str = '12258'
    print(convertString(str))
    print(convertDP(str))