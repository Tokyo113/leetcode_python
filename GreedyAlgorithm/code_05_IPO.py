#coding:utf-8
'''
@Time: 2019/11/11 18:28
@author: Tokyo
@file: code_05_IPO.py
@desc:
输入：
正数数组costs
正数数组profits
正数k
正数m
含义：
costs[i]表示i号项目的花费
profits[i]表示i号项目在扣除花费之后还能挣到的钱(利润)
k表示你只能串行的最多做k个项目
m表示你初始的资金
说明：
你每做完一个项目，马上获得的收益，可以支持你去做下一个项目。
输出：
你最后获得的最大钱数。
'''


import heapq


def ipo(costs, profits, k, m):
    costHeap = []
    profitHeap = []
    count = 0
    for i in range(len(costs)):
        heapq.heappush(costHeap, [costs[i], profits[i]])

    while count < k:
        while costHeap != [] and costHeap[0][0] <= m:
            project = heapq.heappop(costHeap)
            heapq.heappush(profitHeap, [-project[1], project[0]])

        if profitHeap == []:
            break
        ele = heapq.heappop(profitHeap)
        count += 1
        m += -ele[0]

    return m








def findMaxCapital(k, W, costs, profits):
    cost_heap = [(costs[i], profits[i]) for i in range(len(costs))]
    # 默认为小根堆
    # 使用前必须前经过heapify
    # 所有项目扔到被锁池中，花费组织的小根堆
    heapq.heapify(cost_heap)
    profit_heap = []
    for i in range(k):
        while cost_heap != [] and cost_heap[0][0] <= W:
            pro = heapq.heappop(cost_heap)
            heapq.heappush(profit_heap, (-pro[1], pro[0]))
        if len(profit_heap) == 0:
            break
        W += -heapq.heappop(profit_heap)[0]
    return W



def getmax(k, W, costs, profits):

    min_heap = []
    for i in range(len(costs)):
        heapq.heappush(min_heap, (costs[i], profits[i]))

    max_heap = []
    for i in range(k):
        while len(min_heap) > 0 and min_heap[0][0] <= W:
            p = heapq.heappop(min_heap)
            heapq.heappush(max_heap, (-p[1], p[0]))

        if len(max_heap) > 0:
            W += -heapq.heappop(max_heap)[0]

    return W












if __name__ == '__main__':
    costs = [1, 1, 2,4,7]
    profits = [1, 1.5,3,5,4]
    print(findMaxCapital(3,1,costs,profits))
    print(getmax(3,1,costs,profits))
    print(ipo(costs,profits,3,1))



