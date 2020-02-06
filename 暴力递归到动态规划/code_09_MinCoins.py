#coding:utf-8
'''
@Time: 2019/12/10 11:16
@author: Tokyo
@file: code_09_MinCoins.py
@desc:

换钱的最少货币数
【题目】
给定数组 arr，arr 中所有的值都为正数且可以重复。每个值代表一枚货币，
再给定一个整数 aim，代表要找的钱数，求组成 aim 的最少硬币数
[2,3,4,5,6,2]
aim = 10
4+6 = 10
2+3+5=10
和背包问题类似
从左往右的尝试模型
'''


def coins(arr, aim):
    return process11(arr, 0,0, 0,aim)

def process11(arr, i, cur_m, cur_num, aim):
    '''
    返回最少硬币数,但是用了3个可变参数，后面有简化方法
    :param arr:
    :param i:
    :param cur_m:
    :param cur_num:
    :param aim:
    :return:
    '''
    if i == len(arr):
        if cur_m == aim:
            return cur_num
        else:
            return -1

    if cur_m + arr[i] > aim:
        return process11(arr, i+1,cur_m, cur_num, aim)
    else:
        p1 = process11(arr, i+1,cur_m+arr[i], cur_num+1, aim)
        p2 = process11(arr, i+1, cur_m, cur_num, aim)
        if p1 == -1 and p2 == -1:
            return -1
        elif p1 == -1:
            return p2
        elif p2 == -1:
            return p1
        else:
            return min(process11(arr, i+1,cur_m+arr[i], cur_num+1, aim),
                       process11(arr, i+1, cur_m, cur_num, aim))





def minCoin1(arr, rest):
    return process1(arr, 0, rest)


def process1(arr, index, rest):
    '''
    返回最少需要的硬币数,暴力递归
    arr[index...] 组成出rest这么多钱，最少的硬币数量返回
    :param arr:
    :param index:
    :param rest:
    :return:
    '''
    if rest < 0:
        return -1
    # 当前需要搞定rest已经为0，需要0枚硬币,直接返回，没必要继续往后走了
    elif rest == 0:
        return 0
    # 此时rest >0 但已经没有硬币了，返回-1
    if index == len(arr):
        return -1
    # 剩下的情况是rest>0，index<len(arr),有钱也有硬币
    # 不要当前位置的硬币
    p1 = process1(arr, index+1, rest)
    # 要当前位置的硬币
    p2 = process1(arr, index+1, rest-arr[index])

    if p1 == -1 and p2 == -1:
        return -1
    elif p1 == -1:
        return p2+1
    elif p2 == -1:
        return p1
    else:
        # 选了当前硬币直接+1即可，没必要再定义一个可变参数（同背包问题）
        return min(p1, 1+p2)


def minCoin2(arr, rest):
    dp = [[-2 for i in range(rest+1)]for i in range(len(arr)+1)]
    return process2(arr, 0, rest, dp)

def process2(arr, index, rest, dp):
    if rest < 0:
        return -1
    if dp[index][rest] != -2:
        return dp[index][rest]


    if rest == 0:
        dp[index][rest] = 0
    elif index == len(arr):
        dp[index][rest] = -1
    else:
        p1 = process2(arr, index+1, rest, dp)
        p2 = process2(arr, index+1, rest-arr[index], dp)

        if p1 == -1 and p2 == -1:
            dp[index][rest] = -1
        else:
            if p1 == -1:
                dp[index][rest] = p2+1
            elif p2 == -1:
                dp[index][rest] = p1
            else:
                dp[index][rest] = min(p1, p2+1)

    return dp[index][rest]


def minCoin3(arr, rest):
    '''
    严格表结构的动态规划
    :param arr:
    :param rest:
    :return:
    '''
    N = len(arr)
    dp = [[-2 for i in range(rest+1)] for i in range(N+1)]
    if rest < 0:
        return -1
    for i in range(N+1):
        dp[i][0] = 0

    for j in range(1,rest+1):
        dp[N][j] = -1

    for i in range(N-1,-1,-1):
        for j in range(1,rest+1):
            p1 = dp[i+1][j]
            p2 = -1
            if j-arr[i] >= 0:
                p2 = dp[i+1][j-arr[i]]

            if p1 == -1 and p2 == -1:
                dp[i][j] = -1
            else:
                if p1 == -1:
                    dp[i][j] = p2 + 1
                elif p2 == -1:
                    dp[i][j] = p1
                else:
                    dp[i][j] = min(p1, p2 + 1)
    return dp[0][rest]

def biaojiegou(arr, rest):
    dp = [[-2 for i in range(rest+1)] for i in range(len(arr)+1)]

    for i in range(len(arr)+1):
        dp[i][0] = 0
    for res in range(1,rest+1):
        dp[len(arr)][res] = -1

    for i in range(len(arr)-1, -1, -1):
        for res in range(1,rest+1):
            p1 = dp[i+1][res]
            p2 = -1 if res < arr[i] else dp[i+1][res-arr[i]]
            if p1 == -1 and p2 == -1:
                dp[i][res] = -1
            elif p1 == -1:
                dp[i][res] = p2+1
            elif p2 == -1:
                dp[i][res] = p1
            else:
                dp[i][res] = min(p1, p2+1)
    return dp[0][rest]




import random
def generateRandomArray(maxSize, maxValue):

    random_list = []
    for i in range(int((maxSize+1)*random.random())):
        random_list.append(int((maxValue+1)*random.random()))
    return random_list

if __name__ == '__main__':
    testTime = 100
    maxSize = 10
    maxValue = 10
    succeed = True
    for i in range(0, testTime):
        arr1 = generateRandomArray(maxSize, maxValue)
        aim = int(random.random()*3*maxValue)+maxValue


        a = minCoin1(arr1,  aim)
        b = minCoin2(arr1,  aim)
        c = biaojiegou(arr1, aim)

        if (a != c) or (a !=b):
            succeed = False
            print(a,b,c)

            break
    print("Nice!" if succeed else "Fucking fucked")


