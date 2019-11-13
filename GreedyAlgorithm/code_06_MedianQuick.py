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
        maxHeapHead = -self.maxHeap[0]
        minHeapHead = self.minHeap[0]
        if maxHeapSize + minHeapSize == 0:
            return None
        if (minHeapSize + minHeapSize) % 2 == 0:
            return (maxHeapHead+minHeapHead)/2
        return maxHeapHead if maxHeapSize>minHeapSize else minHeapHead



if __name__ == '__main__':
    a = [1,4,7,-5,2,-10, 2,5,6,-1,9]
    s = MedianHolder()
    for i in range(len(a)):
        s.addNumber(a[i])
    b = sorted(a)
    print(s.getMedian())
    print(b)