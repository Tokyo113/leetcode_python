#coding:utf-8
'''
@Time: 2020/2/9 17:34
@author: Tokyo
@file: code_10_ParentheseLengthII.py
@desc:
给你一个左括号和右括号组成的字符串，请找到最长的有效括号子串（连续的）
'''

def maxLength(str):
    maxlen = 0
    pre = 0
    res = [0 for i in range(len(str))]
    for i in range(1,len(str)):
        if str[i] == ')':
            pre = i - res[i-1]-1
            if pre >= 0 and str[pre] == '(':
                res[i] = 2+ res[i-1]
                res[i] += res[pre-1] if pre-1 >= 0 else 0

        maxlen = max(maxlen, res[i])

    return maxlen


if __name__ == '__main__':
    str = ')()()()(()))('
    print(maxLength(str))