#coding:utf-8
'''
@Time: 2019/11/13 19:51
@author: Tokyo
@file: code_06_MedianQuick.py
@desc:
'''
import heapq
class MedianHolder(object):
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []


    def addNumber(self, num):
        if len(self.maxHeap) == 0 or -num >= self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        if len(self.maxHeap) == len(self.minHeap) + 2:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        if len(self.minHeap) == len(self.maxHeap) + 2:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))



    def getMedian(self):
        maxHeapSize = len(self.maxHeap)
        minHeapSize = len(self.minHeap)

        if maxHeapSize + minHeapSize == 0:
            return None

        # maxHeapHead = -self.maxHeap[0]
        # minHeapHead = self.minHeap[0]
        if (minHeapSize + maxHeapSize) % 2 == 0:
            return (-self.maxHeap[0]+self.minHeap[0])/2
        else:
            return -self.maxHeap[0] if maxHeapSize>minHeapSize else self.minHeap[0]


def getMedianofArray(arr):
    if arr == []:
        return None

    arr.sort()
    mid = int((len(arr)-1) / 2)
    if len(arr) % 2 == 0:
        return (arr[mid] + arr[mid+1])/2
    else:
        return arr[mid]


def generateRandomArray(maxSize, maxValue):
    import random
    random_list = []
    for i in range(int((maxSize+1)*random.random())):
        random_list.append(int((maxValue+1)*random.random())-int(maxValue*random.random()))
    return random_list
if __name__ == '__main__':
    testTime = 5000
    maxSize = 100
    maxValue = 100
    err = False
    for i in range(0, testTime):
        arr1 = generateRandomArray(maxSize, maxValue)
        medianHolder = MedianHolder()
        for i in range(len(arr1)):
            medianHolder.addNumber(arr1[i])

        if medianHolder.getMedian() != getMedianofArray(arr1):
            err = True
            print(arr1)
            print(len(arr1))
            print(medianHolder.getMedian())
            print("Answer:", getMedianofArray(arr1))
            break

    print("Nice!" if not err else "Fucking fucked")
