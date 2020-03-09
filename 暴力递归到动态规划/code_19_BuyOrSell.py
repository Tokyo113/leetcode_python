#coding:utf-8
'''
@Time: 2020/3/9 15:31
@author: Tokyo
@file: code_19_BuyOrSell.py
@desc:
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

从左往右的尝试模型：
三个参数：i，k交易次数，当前状态，（买or卖）
起始状态：0，k，只能买

注意一个问题：
总是报超出内存限制
原因在于k可能给的非常大，这样递归状态就太多了，
dp数组就算空间压缩还是超出限制
每一次交易至少两天，当k大于数组长度一半时，
就相当于k没有限制，此时直接过一遍最大和就好了


'''
def onlyTwoSell(prices):
    '''
    特例
    如果只允许交易两次
    :param prices:
    :return:
    '''
    if prices is None or prices == []:
        return 0


    def oneSell(prices):
        if prices is None or prices == []:
            return 0
        res = 0
        minP = prices[0]
        for i in prices:
            minP = min(minP, i)
            res = max(res, i - minP)
        return res


    res = 0
    for i in range(len(prices) + 1):
        left = prices[:i]
        right = prices[i:]
        res = max(oneSell(left) + oneSell(right), res)
    return res


def maxProfit(k,prices):
    if prices is None or prices == []:
        return 0

    return process(prices, 0, k, False)

def process(prices, i, cnt, state):
    '''

    :param prices:
    :param i:
    :param cnt: 剩余可以交易的次数
    :param state: 当前是否持有股票
    :return:
    '''
    if cnt < 0:
        return 0
    if i == len(prices):
        return 0
    if state:
        keep = process(prices, i + 1, cnt, True)
        sell = process(prices, i + 1, cnt, False) + prices[i]
        return max(keep, sell)
    else:
        buy = process(prices, i + 1, cnt - 1, True) - prices[i]
        keep = process(prices, i + 1, cnt, False)
        return max(keep, buy)



def maxProfitDP(k, prices):
    '''
    动态规划版本
    :param k:
    :param prices:
    :return:
    '''
    if prices is None or prices == []:
        return 0
    dpTrue = [[0 for i in range(k+1)] for i in range(len(prices)+1)]
    dpFalse = [[0 for i in range(k + 1)] for i in range(len(prices) + 1)]

    for i in range(len(prices)-1, -1, -1):
        for cnt in range(k+1):
            dpTrue[i][cnt] = max(dpTrue[i+1][cnt], dpFalse[i+1][cnt]+prices[i])
            if cnt >= 1:
                dpFalse[i][cnt] = max(dpFalse[i+1][cnt], dpTrue[i+1][cnt-1]-prices[i])

    return dpFalse[0][k]



def maxProfitDP2(k, prices):
    '''
    进一步压缩空间，还是超出内存限制
    :param k:
    :param prices:
    :return:
    '''
    if prices is None or prices == []:
        return 0
    if k>len(prices)//2:
        return noLimitProfit(prices)
    dp = [[0 for i in range(k + 1)] for i in range(2)]


    for i in range(len(prices) - 1, -1, -1):
        for cnt in range(k + 1):
            dp[0][cnt] = max(dp[0][cnt], dp[1][cnt] + prices[i])
            if cnt >= 1:
                dp[1][cnt] = max(dp[1][cnt], dp[0][cnt - 1] - prices[i])

    return dp[1][k]

def noLimitProfit(arr):
    res = 0
    for i in range(1, len(arr)):
        res += arr[i]-arr[i-1] if arr[i]>arr[i-1] else 0
    return res
if __name__ == '__main__':
    price = [3,3,5,0,0,3,1,4]
    print(maxProfit(2,price))
    print(maxProfitDP(2,price))
    print(maxProfitDP2(2,price))



