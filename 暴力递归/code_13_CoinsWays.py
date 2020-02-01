#coding:utf-8
'''
@Time: 2019/12/11 16:28
@author: Tokyo
@file: code_13_CoinsWays.py
@desc:
给定数组 arr，arr 中所有的值都为正数且不重复。每个值代表一种面值的货币，每种面值
的货币可以使用任意张，再给定一个整数 aim，代表要找的钱数，求组成 aim 的方法数

'''

def coinWay1(arr, aim):
    if arr is None or len(arr) == 0:
        return 0
    return way1(arr, 0, aim)

def way1(arr, index, rest):

    if index == len(arr):
        return 1 if rest == 0 else 0

    res = 0
    k = 0
    while arr[index]*k <= rest:
        res += way1(arr, index+1, rest-arr[index]*k)
        k += 1

    return res


def coinWay2(arr, aim):
    '''
    无斜率优化的动态规划
    :param arr:
    :param aim:
    :return:
    '''
    N = len(arr)
    dp = [[0 for i in range(aim+1)] for i in range(N+1)]
    # basecase
    dp[N][0] = 1
    for i in range(1,aim+1):
        dp[N][i] = 0

    for index in range(N-1, -1, -1):
        for rest in range(aim+1):
            k = 0
            while (k*arr[index]<=rest):
                dp[index][rest] += dp[index+1][rest-k*arr[index]]
                k += 1

    return dp[0][aim]

def coinWays3(arr, aim):
    '''
    带斜率优化的DP
    :param arr:
    :param aim:
    :return:
    '''
    N = len(arr)
    dp = [[0 for i in range(aim+1)]for i in range(N+1)]

    dp[N][0] = 1
    for i in range(1,aim+1):
        dp[N][i] = 0

    for index in range(N-1, -1, -1):
        for rest in range(0,aim+1):
            dp[index][rest] += dp[index+1][rest]
            if rest-arr[index] >= 0:
                dp[index][rest] += dp[index][rest-arr[index]]

    return dp[0][aim]




import random
def generateRandArr(maxSize, maxValue):

    rand_arr = []
    for i in range(int((maxSize+1)*random.random())):
        rand_arr.append(int((maxValue+1)*random.random()))

    return rand_arr


if __name__ == '__main__':
    # maxSize = 5
    # maxValue = 5
    # testTimes = 1000
    # for i in range(testTimes):
    #     arr = generateRandArr(maxSize, maxValue)
    #     aim = int(random.random()*2*maxValue)+maxValue
    #     a = coinWay1(arr,aim)
    #     b = coinWay2(arr, aim)
    #
    #     if a != b:
    #         print("fuck!!!")
    #         break
    #
    # print("Wow,bbd")

    arr = [1,2,3,4,5,6,7,10]
    a = coinWays3(arr, 12)
    b = coinWay2(arr, 12)
    print(a,b)


