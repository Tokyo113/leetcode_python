#coding:utf-8
'''
@Time: 2019/11/17 12:32
@author: Tokyo
@file: code_07_Knapsack.py
@desc:
'''


def Knapsack(weights, values, bag):
    if len(weights) == 0 or len(values) == 0 or bag == 0:
        return 0

    def process(i,alreadyWeights):
        if i == len(weights):
            return 0
        if alreadyWeights > bag:
            return 0

        return max(values[i] + process(i+1, alreadyWeights+weights[i]), process(i+1, alreadyWeights))

    return process(0, 0)


def Knapsack2(weights, values, bag):
    if len(weights) == 0 or len(values) == 0 or bag == 0:
        return 0

    def process(i, alreadyweight, alreadyvalue):
        if i == len(weights):
            return alreadyvalue
        if alreadyweight > bag:
            return alreadyvalue

        return max(process(i+1, alreadyweight+weights[i], alreadyvalue+values[i]),
                   process(i+1, alreadyweight, alreadyvalue))
    return process(0, 0, 0)

if __name__ == '__main__':
    weights = [3,2,4,7]
    values = [5,6,3,19]
    bag = 11
    print(Knapsack(weights,values,bag))
    print(Knapsack2(weights,values,bag))