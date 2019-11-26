#coding:utf-8
'''
@Time: 2019/11/21 10:24
@author: Tokyo
@file: code_05_UnionFind.py
@desc:
'''

class Element(object):
    def __init__(self, val):
        self.val = val




class UnionFindSet(object):
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
            # 路径经过的点进入栈，每个点的father改为当前集合的头部
            path.append(element)
            element = self.fatherMap.get(element)

        while path != []:
            self.fatherMap[path.pop()] = element

        return element




    def isSameSet(self, val1, val2):
        if self.elementMap.get(val1) != None and self.elementMap.get(val2) != None:
            return self.findHead(self.elementMap.get(val1)) == self.findHead(self.elementMap.get(val2))
        return False


    def union(self, a, b):
        if self.elementMap.get(a) != None and self.elementMap.get(b) != None:
            aF = self.findHead(self.elementMap.get(a))
            bF = self.findHead(self.elementMap.get(b))
            big = aF if self.sizeMap.get(aF) >= self.sizeMap.get(bF) else bF
            small = bF if aF == big else aF
            self.fatherMap[small] = big

            self.sizeMap[big] = self.sizeMap.get(big) + self.sizeMap.get(small)
            self.sizeMap.pop(small)


class bingchaji(object):
    def __init__(self, lists):
        self.elementMap = {}
        self.fatherMap = {}
        self.sizeMap = {}

        for i in lists[0]:
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

    def isSameSet(self, a,b):
        if self.elementMap.get(a) != None and self.elementMap.get(b) != None:
            return self.findHead(self.elementMap.get(a)) == self.findHead(self.elementMap.get(b))
        return False

    def union(self, a, b):
        if self.elementMap.get(a) !=None and self.elementMap.get(b) != None:
            aF = self.findHead(self.elementMap.get(a))
            bF = self.findHead(self.elementMap.get(b))
            big = aF if self.sizeMap.get(aF) > self.sizeMap.get(bF) else bF
            small = bF if big == aF else aF

            self.fatherMap[small] = big

            self.sizeMap[big] = self.sizeMap.get(big) + self.sizeMap.get(small)
            self.sizeMap.pop(small)
def findCircleNum(M):
    if M == []:
        return 0

    a = bingchaji(M)

    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 1:
                if not a.isSameSet(i, j):
                    a.union(i, j)

    return len(a.sizeMap)


if __name__ == '__main__':
    a = ["A", 'B', 'C', 'D', 'E', 'F', 'G']
    unionfind = UnionFindSet(a)

    print(unionfind.isSameSet('A', 'B'))
    unionfind.union('A', 'B')
    print(unionfind.isSameSet('A', 'B'))
    unionfind.union('C', 'B')
    print(unionfind.isSameSet('A', 'C'))
    unionfind.union('C', 'D')
    print(unionfind.isSameSet('A', 'D'))

    M = [[1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]

    s  = findCircleNum(M)
    print(s)




