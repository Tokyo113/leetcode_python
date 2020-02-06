#coding:utf-8
'''
@Time: 2019/12/10 19:49
@author: Tokyo
@file: code_10_CardsInLinePlus.py
@desc:
给定一个整型数组arr，代表数值不同的纸牌排成一条线。玩家A和玩家B依次拿走每张纸
牌，规定玩家A先拿，玩家B后拿，但是每个玩家每次只能拿走最左或最右的纸牌，玩家A
和玩家B都绝顶聪明。请返回最后获胜者的分数。

将暴力递归改为动态规划
'''

def winner(arr):
    if arr is None or arr == []:
        return 0
    return max(f1(arr, 0, len(arr)-1), g1(arr, 0, len(arr)-1))

def f1(arr, L, R):
    if L == R:
        return arr[L]
    return max(arr[L]+g1(arr, L+1, R), arr[R]+g1(arr, L, R-1))

def g1(arr, L, R):
    if L == R:
        return 0
    return min(f1(arr, L+1, R), f1(arr, L, R-1))


def winnerdp(arr):
    if arr is None or arr == []:
        return 0
    dpf = [[0 for i in range(len(arr))] for i in range(len(arr))]
    dpg = [[0 for i in range(len(arr))] for i in range(len(arr))]
    for i in range(len(arr)):
        dpf[i][i] = arr[i]
        dpg[i][i] = 0

    for L in range(len(arr)-2, -1, -1):
        for R in range(L+1, len(arr)):
            dpf[L][R] = max(arr[L]+dpg[L+1][R], arr[R]+dpg[L][R-1])
            dpg[L][R] = min(dpf[L+1][R], dpf[L][R-1])

    return max(dpf[0][len(arr)-1], dpg[0][len(arr)-1])




def playcards(arr):
    if arr == [] or arr is None:
        return 0
    return max(f(arr, 0, len(arr)-1), s(arr, 0, len(arr)-1))


def f(arr, L, R):
    '''
    观察到有两个可变参数，对于f和g分别构造一个二维表
    两个表互相依赖，填充即可
    :param arr:
    :param L:
    :param R:
    :return:
    '''
    if L == R:
        return arr[L]

    return max(arr[L]+s(arr, L+1, R), arr[R]+s(arr, L, R-1))

def s(arr, L, R):
    if L == R:
        return 0
    return min(f(arr, L+1, R), f(arr, L, R-1))

def playCardsDP(arr):
    if arr == [] or arr is None:
        return 0
    N = len(arr)
    dp_f = [[0 for i in range(N)]for i in range(N)]
    dp_s = [[0 for i in range(N)]for i in range(N)]

    # f函数的对角线
    for i in range(N):
        dp_f[i][i] = arr[i]

    for i in range(N-2, -1, -1):
        for j in range(i+1, N):
            dp_f[i][j] = max(arr[j]+dp_s[i][j-1], arr[i]+dp_s[i+1][j])
            dp_s[i][j] = min(dp_f[i][j-1], dp_f[i+1][j])

    return max(dp_f[0][N-1], dp_s[0][N-1])


import random
def generateRandomArr(maxSize, maxValue):
    rand_arr = []
    for i in range(int((maxSize+1)*random.random())):
        rand_arr.append(int((maxValue+1)*random.random()))

    return rand_arr

if __name__ == '__main__':
    maxSize = 10
    maxValue = 100
    testtimes = 100
    for i in range(testtimes):
        arr = generateRandomArr(maxSize, maxValue)
        a = winnerdp(arr)
        b = playCardsDP(arr)

        if a != b:
            print("fuck!!!")
            print(arr)
            break
    print("Wow,succeed!")