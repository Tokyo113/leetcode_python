#coding:utf-8
'''
@Time: 2020/4/10 12:15
@author: Tokyo
@file: code_07_数组中的最长连续序列.py
@desc:
leetcode 128
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

可以用并查集做
'''
class Element():
    def __init__(self,val):
        self.val = val

class UnionSet():
    def __init__(self,arr):
        self.elementMap = {}
        self.sizeMap = {}
        self.fatherMap = {}
        for i in arr:
            element = Element(i)
            self.elementMap[i] = element
            self.fatherMap[element] =element
            self.sizeMap[element] = 1
    def findHead(self,a):
        if a in self.elementMap:
            element = self.elementMap[a]
            stack = []
            while element != self.fatherMap[element]:
                stack.append(element)
                element = self.fatherMap[element]

            while stack != []:
                self.fatherMap[stack.pop()] = element

            return element


    def isSameSet(self,a,b):
        if a in self.elementMap and b in self.elementMap:
            if self.findHead(a) == self.findHead(b):
                return True
        return False


    def merge(self,a,b):
        if a in self.elementMap and b in self.elementMap:
            if not self.isSameSet(a,b):
                aF = self.findHead(a)
                bF = self.findHead(b)
                big = aF if self.sizeMap[aF]>=self.sizeMap[bF] else bF
                small = bF if big == aF else aF
                self.fatherMap[small] = big
                self.sizeMap[big] += self.sizeMap[small]
                self.sizeMap.pop(small)





def longestSeq(arr):
    if arr is None or arr == []:
        return 0
    unionSet = UnionSet(arr)
    for i in arr:
        if i-1 in unionSet.elementMap and not unionSet.isSameSet(i,i-1):
            unionSet.merge(i,i-1)
        if i+1 in unionSet.elementMap and not unionSet.isSameSet(i,i+1):
            unionSet.merge(i,i+1)

    maxlen = 0
    for k,v in unionSet.sizeMap.items():
        maxlen = max(maxlen,v)
    return maxlen


if __name__ == '__main__':
    arr = [100,4,200,3,1,2]
    print(longestSeq(arr))