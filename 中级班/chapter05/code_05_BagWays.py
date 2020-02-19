#coding:utf-8
'''
@Time: 2020/2/19 16:59
@author: Tokyo
@file: code_05_BagWays.py
@desc:
牛牛准备参加学校组织的春游, 出发前牛牛准备往背包里装入一些零食, 牛牛的背包容
量为w。
牛牛家里一共有n袋零食, 第i袋零食体积为v[i]。
牛牛想知道在总体积不超过背包容量的情况下，他一共有多少种零食放法(总体积为0也
算一种放法)。
'''

def bagWays1(v, w):
    if w <= 0 or v is None or v == []:
        return 0
    return process(v,w,0, 0)

def process(v,w,i, weight):
    if i == len(v):
        return 1 if weight <= w else 0
    if v[i]+weight > w:
        return process(v,w,i+1, weight)
    else:
        return process(v,w,i+1, v[i]+weight)+process(v,w,i+1, weight)

def bagWays2(v,w):
    if w <= 0 or v == []:
        return 0
    return process1(v,0,w)

def process1(v,i,res):
    if res < 0:
        return 0
    if i == len(v):
        return 1
    return process1(v,i+1, res-v[i])+process1(v,i+1, res)



def bagWaysDP(v,w):
    if w <= 0 or v == []:
        return 0
    dp = [[0 for i in range(w+1)]for i in range(len(v)+1)]
    for col in range(w+1):
        dp[len(v)][col] = 1

    for i in range(len(v)-1, -1, -1):
        for col in range(w+1):
            dp[i][col] += dp[i+1][col]
            dp[i][col] += dp[i+1][col-v[i]] if col-v[i] >= 0 else 0

    return dp[0][w]


if __name__ == '__main__':
    v = [4,3,2,9,11,23,1,5]
    w = 21
    print(bagWays1(v,w))
    print(bagWays2(v, w))
    print(bagWaysDP(v,w))

