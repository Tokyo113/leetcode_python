#coding:utf-8
'''
@Time: 2019/11/11 16:38
@author: Tokyo
@file: code_04_lessmoneySplitGold.py
@desc:
一块金条切成两半，是需要花费和长度数值一样的铜板的。比如长度为20的金
条，不管切成长度多大的两半，都要花费20个铜板。
一群人想整分整块金条，怎么分最省铜板?
例如,给定数组{10,20,30}，代表一共三个人，整块金条长度为10+20+30=60。
金条要分成10,20,30三个部分。 如果先把长度60的金条分成10和50，花费60；
再把长度50的金条分成20和30，花费50；一共花费110铜板。
但是如果先把长度60的金条分成30和30，花费60；再把长度30金条分成10和20，
花费30；一共花费90铜板。
输入一个数组，返回分割的最小代价。
'''

import queue

def lessmoney(arr):
    pQ = queue.PriorityQueue()
    for i in range(len(arr)):
        pQ.put(arr[i])
    summ = 0
    while pQ.qsize() > 1:
        res = pQ.get() + pQ.get()
        pQ.put(res)
        summ += res
    return summ

import heapq
def GoldSplit(arr):
    heapq.heapify(arr)
    sum = 0
    while len(arr)> 1:
        res = heapq.heappop(arr) + heapq.heappop(arr)
        heapq.heappush(arr, res)
        sum += res

    return sum





if __name__ == '__main__':
    arr1 = [6,7,8,9]
    arr2 = [3,5,2,7,0,1,6,4]
    # print(lessmoney(arr1))
    # print(GoldSplit(arr1))

    # print(GoldSplit(arr2))
    # print(lessmoney(arr2))

