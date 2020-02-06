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


if __name__ == '__main__':
    weights = [3,2,4,7]
    values = [5,6,3,19]
    bag = 11
    print(Knapsack(weights,values,bag))
    print(Knapsack2(weights,values,bag))
