#coding:utf-8
'''
@Time: 2019/11/17 11:32
@author: Tokyo
@file: ConvertToLetterString.py
@desc:
规定1和A对应、2和B对应、3和C对应...
那么一个数字字符串比如"111"，就可以转化为"AAA"、"KA"和"AK"。
给定一个只有数字字符组成的字符串str，返回有多少种转化结果

'''

def convertLetterString(strs):
    if len(strs) == 0:
        return 0
    return process(strs, 0)

def process(strs, i):
    if i == len(strs):
        return 1

    # 如果以0开头，此路不通，为0
    if strs[i] == '0':
        return 0

    if strs[i] == '1':
        res = process(strs, i+1)
        if i+1 < len(strs):
            res += process(strs, i+2)
        return res

    elif strs[i] == '2':
        res = process(strs, i+1)
        if i+1 < len(strs) and int(strs[i+1]) < 7:
            res += process(strs, i+2)
        return res

    else:  # 3~9
        res = process(strs, i+1)
        return res



def convertDP(strs):
    if strs is None or strs == '':
        return 0

    dp = [0 for i in range(len(strs) + 1)]
    dp[-1] = 1
    for i in range(len(strs) - 1, -1, -1):
        dp[i] += dp[i + 1]
        if i + 1 < len(strs):
            if strs[i] == '1':
                dp[i] += dp[i + 2]
            elif strs[i] == '2' and int(strs[i + 1]) <= 5:
                dp[i] += dp[i + 2]
    return dp[0]










if __name__ == '__main__':
    a = '12322'
    print(convertLetterString(a))
    print(convertDP(a))