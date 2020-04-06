#coding:utf-8
'''
@Time: 2020/4/6 20:54
@author: Tokyo
@file: leetcode_261_以图判树.py
@desc:
给定从 0 到 n-1 标号的 n 个结点，和一个无向边列表（每条边以结点对来表示），请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。

示例 1：

输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
输出: true
示例 2:

输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
输出: false
注意：你可以假定边列表 edges 中不会出现重复的边。由于所有的边是无向边，边 [0,1] 和边 [1,0] 是相同的，因此不会同时出现在边列表 edges 中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/graph-valid-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

法一.并查集
法二.BFS
'''


def validTree(n, edges):
    if n-1 != len(edges):
        return False
    import collections
    nodeMap = collections.defaultdict(list)
    queue = [0]
    res = []
    has = [0]
    for i in edges:
        nodeMap[i[0]].append(i[1])
        nodeMap[i[1]].append(i[0])

    while queue != []:
        pp = queue.pop()
        res.append(pp)

        for i in nodeMap[pp]:
            if i not in has:
                queue.append(i)
                has.append(i)

    return len(res) == n

class Element():
    def __init__(self,val):
        self.val = val

class UnionSet():
    def __init__(self,n):
        self.fatherMap = {}
        self.sizeMap = {}
        self.elementMap = {}
        for i in range(n):
            element = Element(i)
            self.elementMap[i] = element
            self.fatherMap[element] = element
            self.sizeMap[element] = 1

    def findHead(self,a):
        if a in self.elementMap:
            pp = self.elementMap[a]
            stack = []
            while pp != self.fatherMap[pp]:
                stack.append(pp)
                pp = self.fatherMap[pp]

            while stack != []:
                self.fatherMap[stack.pop()] = pp
            return pp
    def isSameSet(self,a,b):
        if a in self.elementMap and b in self.elementMap:
            if self.findHead(a) == self.findHead(b):
                return True
        return False
    def Union(self,a,b):
        if a in self.elementMap and b in self.elementMap:
            if not self.isSameSet(a,b):
                aF = self.findHead(a)
                bF = self.findHead(b)
                big = aF if self.sizeMap[aF] >= self.sizeMap[bF] else bF
                small = bF if big == aF else aF
                self.fatherMap[small] = big
                self.sizeMap[big] += self.sizeMap[small]
                self.sizeMap.pop(small)

def validTree2(n,edges):
    '''
    并查集
    :param n:
    :param edges:
    :return:
    '''
    if n-1 != len(edges):
        return False
    union = UnionSet(n)
    for i in edges:
        if union.isSameSet(i[0],i[1]):
            return False
        union.Union(i[0],i[1])
    return True






if __name__ == '__main__':
    arr =  [[0,1], [0,2], [0,3],  [1,4]]
    print(validTree(5,arr))
    print(validTree2(5,arr))