#coding:utf-8
'''
@Time: 2019/11/21 11:51
@author: Tokyo
@file: code_06_LongestConsecutiveSequence.py
@desc:

给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
'''

class Element(object):
    def __init__(self, val):
        self.val = val



class unionFind(object):
    def __init__(self, lists):
        self.elementMap = {}
        self.fatherMap = {}
        self.sizeMap = {}

        for i in lists:
            element = Element(i)
            self.elementMap[i] = element
            self.fatherMap[element] = element
            self.sizeMap[element] = 1


    def findHead(self, element):
        path = []
        while element != self.fatherMap.get(element):
            path.append(element)
            element = self.fatherMap.get(element)

        while path != []:
            self.fatherMap[path.pop()] = element

        return element

    def isSameSet(self, a, b):
        if self.elementMap.get(a) != None and self.elementMap.get(b) != None:
            return self.findHead(self.elementMap.get(a)) == self.findHead(self.elementMap.get(b))
        return False
    def union(self, a, b):
        if self.elementMap.get(a) != None and self.elementMap.get(b) != None:
            aF = self.findHead(self.elementMap.get(a))
            bF = self.findHead(self.elementMap.get(b))
            big = aF if self.sizeMap.get(aF) >= self.sizeMap.get(bF) else bF
            small = bF if big == aF else aF
            self.fatherMap[small] = big
            self.sizeMap[big] = self.sizeMap[big] + self.sizeMap[small]
            self.sizeMap.pop(small)


def longestConsecutiveQuence(arr):
    if arr == []:
        return 0
    a = unionFind(arr)
    for i in range(len(arr)):
        if a.elementMap.get(arr[i]+1) != None and not a.isSameSet(arr[i], arr[i]+1):

            a.union(arr[i], arr[i] + 1)
        if a.elementMap.get(arr[i]-1) != None and not a.isSameSet(arr[i], arr[i]-1):
            a.union(arr[i], arr[i] - 1)
    length = 0
    for i in a.sizeMap.values():
        length = max(i, length)
    return length

def method2(arr):
    arr = set(arr)
    res = 0
    for x in arr:
        if x - 1 not in arr:
            y = x+1
            while y in arr:
                y += 1
            res = max(res, y-x)
    return res


if __name__ == '__main__':
    a = [100, 4, 200, 1, 3, 2]
    print(longestConsecutiveQuence(a))

    print(method2(a))

