#coding:utf-8
'''
@Time: 2020/2/14 12:28
@author: Tokyo
@file: code_09_TopK++.py
@desc:
进阶版：
实现一个结构，随时可以返回此时结构中出现次数最多的topK个字符串
用户有两种操作，add(), getTopK()
分别是向结构中添加字符串以及返回此时的topK


思路：
思路与上题一致，但不能使用系统提供的堆结构了，
需要自己定义堆结构，然后进行调整等
'''

class TopKHeap(object):
    def __init__(self, K):
        self.timesMap = {}
        self.indexMap = {}
        self.heapsize = K
        self.heap = []
        self.index = 0

    def add(self, str):
        strIndex = -1
        if self.timesMap.get(str) != None:
            # 词频表记录
            self.timesMap[str] += 1
            strIndex = self.indexMap.get(str)
        else:
            self.timesMap[str] = 1
            self.indexMap[str] = -1

        if strIndex == -1:          # 该str不在堆中
            times = self.timesMap.get(str)
            if self.index < self.heapsize: # 堆没有满

                # 堆中存放的是[str, times]
                self.heap.append([str, times])

                self.heapInsert(self.index)
                self.indexMap[str] = self.index
                self.index += 1
            else:  # 堆满了，看能不能加进去
                if times > self.heap[0][1]:
                    self.heap[0] = [str, times]
                    self.heapify(0,self.heapsize)
        else:  # 已经在堆中,出现次数加1，然后heapify
            self.heap[strIndex][1] += 1
            self.heapify(strIndex, self.heapsize)




    def getTopK(self):
        print([i for i in self.heap])

    def heapInsert(self, i):
        father = (i-1)>>1
        while father >= 0 and self.heap[i][1] < self.heap[father][1]:

            self.indexMap[self.heap[father][0]] = i
            self.indexMap[self.heap[i][0]] = father
            self.heap[i], self.heap[father] = self.heap[father], self.heap[i]


    def heapify(self, i, size):
        '''
        小根堆中某个位置i的值变大，进行向下调整
        :param i:
        :param size:
        :return:
        '''

        left = 2*i+1
        while left < size:
            smallest = left +1 if (left+1) < size and self.heap[left][1] > self.heap[left+1][1] else left
            smallest = i if self.heap[i][1] < self.heap[smallest][1] else smallest
            if smallest == i:
                break
            else:
                self.indexMap[self.heap[i][0]] = smallest
                self.indexMap[self.heap[smallest][0]] = i
                self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
                i = smallest
                left = 2*i+1


if __name__ == '__main__':

    record = TopKHeap(3)

    record.add("zuo")
    record.getTopK()
    record.add("cheng")
    record.add("cheng")
    record.getTopK()
    record.add("Yun")
    record.add("Yun")

    record.getTopK()
    record.add('tokyo')
    record.add('tokyo')
    record.add('tokyo')
    record.add('Yun')
    record.getTopK()


