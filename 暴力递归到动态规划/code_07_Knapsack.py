#coding:utf-8
'''
@Time: 2019/11/17 12:32
@author: Tokyo
@file: code_07_Knapsack.py
@desc:
给定两个长度都为N的数组weights和values，weights[i]和values[i]分别代表
i号物品的重量和价值。给定一个正数bag，表示一个载重bag的袋子，你装的物
品不能超过这个重量。返回你能装下最多的价值是多少？
暴力递归
然后改成动态规划
'''

def Knapsack1(weights, values, bag):
    return process(weights,values, 0, bag)

def process(weights, values, i, res):
    if res < 0:
        return -1
    elif res == 0:
        return 0
    if i == len(weights):
        return 0
    p1 = process(weights,values,i+1, res)
    p2 = process(weights,values,i+1,res-weights[i])
    if p2 == -1:
        return p1
    else:
        return max(p1,p2+values[i])


def eee(weights, values, bag):
    return ppp(weights,values,0,0)

def ppp(weights, values, i,alreadyweight):
    if i == len(weights):
        return 0
    if weights[i]+alreadyweight > bag:
        return ppp(weights,values,i+1, alreadyweight)
    else:
        return max(ppp(weights, values,i+1,alreadyweight),
                   values[i]+ppp(weights,values,i+1,weights[i]+alreadyweight))

def Knapsack(weights, values, bag):
    if len(weights) == 0 or len(values) == 0 or bag == 0:
        return 0

    def process(i,alreadyWeights):
        if i == len(weights):
            return 0
        if weights[i] + alreadyWeights > bag:
            return process(i+1, alreadyWeights)
        else:
            return max(values[i]+process(i+1, alreadyWeights+weights[i]),
                       process(i+1, alreadyWeights))




    return process(0, 0)



def Knapsack2(weights, values, bag):
    if weights == [] or values == [] or bag == 0:
        return 0


    def process(i, alreadyweight, alreadyvalue):
        if i == len(weights):
            return alreadyvalue
        if alreadyweight + weights[i] > bag:
            return process(i+1, alreadyweight, alreadyvalue)
        else:
            return max(process(i+1, alreadyweight, alreadyvalue), process(i+1, alreadyweight+weights[i], alreadyvalue+values[i]))

    return process(0,0,0)


def KnapsackDP(weights,values,bag):
    '''
    由暴力递归改为动态规划
    :param weights:
    :param values:
    :param bag:
    :return:
    '''
    dp = [[0 for i in range(bag+1)]for i in range(len(weights)+1)]
    for i in range(len(weights)-1, -1, -1):
        for res in range(1,bag+1):
            p1 = dp[i+1][res]
            p2 = dp[i+1][res-weights[i]] if res-weights[i] >= 0 else -1
            if p2 == -1:
                dp[i][res] = p1
            else:
                dp[i][res] = max(p1, values[i]+p2)
    return dp[0][bag]

if __name__ == '__main__':
    weights = [3,2,4,7]
    values = [5,6,3,19]
    bag =4
    print(Knapsack(weights,values,bag))
    print(Knapsack2(weights,values,bag))
    print(Knapsack1(weights,values,bag))
    print(eee(weights,values,bag))
    print(KnapsackDP(weights,values,bag))
