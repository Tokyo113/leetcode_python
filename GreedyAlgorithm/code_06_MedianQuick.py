#coding:utf-8
'''
@Time: 2019/11/13 19:51
@author: Tokyo
@file: code_06_MedianQuick.py
@desc:
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
从一个数据流中随时可以取得中位数
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


class tokyo(object):
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        if self.maxHeap == []:
            heapq.heappush(self.maxHeap, -num)
        else:
            if num <= -self.maxHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)

            if len(self.maxHeap) == len(self.minHeap)+2:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            elif len(self.minHeap) == len(self.maxHeap)+2:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))



    def getMedian(self):
        if len(self.maxHeap) == 0 and len(self.minHeap) == 0:
            return None
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0]+self.minHeap[0])/2
        else:
            return self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else -self.maxHeap[0]

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
        medianHolder = tokyo()
        for i in range(len(arr1)):
            medianHolder.addNum(arr1[i])

        if medianHolder.getMedian() != getMedianofArray(arr1):
            err = True
            print(arr1)
            print(len(arr1))
            print(medianHolder.getMedian())
            print("Answer:", getMedianofArray(arr1))
            break

    print("Nice!" if not err else "Fucking fucked")
