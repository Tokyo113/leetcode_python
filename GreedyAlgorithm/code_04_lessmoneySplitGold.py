#coding:utf-8
'''
@Time: 2019/11/11 16:38
@author: Tokyo
@file: code_04_lessmoneySplitGold.py
@desc:
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
    print(lessmoney(arr1))
    print(lessmoney(arr2))
    print(GoldSplit(arr1))
    print(GoldSplit(arr2))
