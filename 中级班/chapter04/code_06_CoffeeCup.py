#coding:utf-8
'''
@Time: 2020/2/17 10:52
@author: Tokyo
@file: code_06_CoffeeCup.py
@desc:
咖啡杯问题：
给你一个正数数组arr，一个数代表一个咖啡机的工作效率
如arr = [3,2,7]，表示三台咖啡机泡一杯咖啡分别需要3，2，7min
一台咖啡机一次只能冲一杯咖啡
第二个参数表示n个人需要喝咖啡，每个人只喝1杯，所有人喝咖啡的时间不计，n个人存在排队问题，
第三个参数a，只有一台洗咖啡杯的机器，洗一个咖啡杯需要的时间为a
第四个参数，咖啡杯不洗自然挥发也能变干净的时间为b
求全过程从泡咖啡到所有杯子洗干净为止至少需要多少时间

思路：
贪心策略+动态规划
分成两部分分析，第一部分是冲咖啡问题，用小根堆
第二部分暴力递归，每一个人都有两种选择：自然挥发or洗杯子
'''
import heapq
def coffee(arr, n, a, b):
    '''
    咖啡杯问题
    :param arr: 咖啡机效率
    :param n: n个顾客
    :param a: 清洗机洗一个杯子的时间
    :param b: 自然挥发变干净的时间
    :return: 全过程用时最少的时间
    '''
    heap = []
    # drinks 记录第i个人在第几分钟得到并喝完咖啡
    drinks = []
    for i in range(len(arr)):
        heapq.heappush(heap, [0+arr[i], 0, arr[i]])
    for i in range(n):

        pp = heapq.heappop(heap)
        endtime = pp[0]
        drinks.append(endtime)
        heapq.heappush(heap, [endtime+pp[2], endtime,pp[2]])

    return process(drinks, a, b, 0, 0)

def process(arr, a, b, index, washline):
    '''
    返回该种方案下做完所有事情的最早时间
    包括洗完当前咖啡杯并洗完剩下所有咖啡杯
    :param arr:
    :param a:
    :param b:
    :param index:
    :param washline:
    :return:
    '''
    if index == len(arr)-1:
        return min(max(arr[index], washline)+a, arr[index]+b)
    # 1.用洗咖啡机清洗
    # 洗完当前咖啡杯的时间
    wash = max(arr[index], washline)+a
    # 洗完剩下的咖啡杯的时间
    res = process(arr, a, b, index+1, wash)
    # 取max，取瓶颈
    p1 = max(wash, res)

    # 2.自然挥发
    dry = arr[index]+b
    res = process(arr, a,b,index+1, washline)
    p2 = max(dry, res)

    return min(p1, p2)



def coffeeDP(arr, n, a, b):
    '''
    动态规划
    :param arr:
    :param n:
    :param a:
    :param b:
    :return:
    '''
    heap = []
    drinks = []
    for i in range(len(arr)):
        heapq.heappush(heap, [0+arr[i], 0, arr[i]])
    for i in range(n):
        pp = heapq.heappop(heap)
        drinks.append(pp[0])
        heapq.heappush(heap, [pp[0]+pp[2],pp[0], pp[2]])

    dp = [[0 for i in range(drinks[n-1]+n*a)] for i in range(n)]
    for i in range(len(dp[0])):
        dp[n-1][i] = min(max(drinks[n-1], i)+a,drinks[n-1]+b)


    for i in range(n-2, -1, -1):
        for washline in range(drinks[i]+(i+1)*a):
            # 用洗咖啡杯的机器清洗
            wash = max(drinks[i], washline)+a
            next1 = dp[i+1][wash]
            p1 = max(wash,next1)

            # 自然挥发
            dry = drinks[i]+b
            next2 = dp[i+1][washline]
            p2 = max(dry, next2)
            dp[i][washline] = min(p1, p2)
    return dp[0][0]







if __name__ == '__main__':
    arr = [3,2,6]
    n = 10
    a = 4
    b = 15
    print(coffee(arr,n,a,b))
    print(coffeeDP(arr, n, a,b))
