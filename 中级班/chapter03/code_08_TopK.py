#coding:utf-8
'''
@Time: 2020/2/14 12:14
@author: Tokyo
@file: code_08_TopK.py
@desc:
给定一个字符串类型的数组arr，求其中出现次数最多的前K个

可以直接使用系统提供的小根堆
小根堆大小适中维持在K个即可
'''
import heapq
def findTopK(arr, K):
    if arr is None or arr == []:
        return
    timesMap = {}
    heap = []

    for i in arr:
        if timesMap.get(i) != None:
            timesMap[i] += 1
        else:
            timesMap[i] = 1

    for str, time in timesMap.items():
        if len(heap) < K:
            heapq.heappush(heap, [time, str])
        else:
            if time > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, [time, str])
    res = [i[1] for i in heap]
    return res


if __name__ == '__main__':
    strs = ['abc', 'hello', 'tokyo', 'hello', 'tokyo', 'kkk',
            'tokyo', 'aa', 'abc', 'abc']
    print(findTopK(strs, 3))


