#coding:utf-8
'''
@Time: 2019/11/11 18:28
@author: Tokyo
@file: code_05_IPO.py
@desc:
'''


import heapq





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



