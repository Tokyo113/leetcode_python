#coding:utf-8
'''
@Time: 2019/11/7 19:17
@author: Tokyo
@file: code_03_TopologySort.py
@desc:
'''


class Graph(object):
    def __init__(self):
        self.nodes = {}
        self.edges = []


class Node(object):
    def __init__(self, value):
        self.value = value
        self.in_num = 0
        self.out_num = 0
        self.nexts = []
        self.edges = []


class Edge(object):
    def __init__(self, weight, from_node, to_node):
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node



def TopologySort(graph):
    inMap = {}
    # 存放所有入度为0的节点
    zeroInQueue = []
    result = []

    for node in graph.nodes.values():
        inMap[node] = node.in_num
        if node.in_num == 0:
            zeroInQueue.append(node)

    while zeroInQueue != []:
        cur = zeroInQueue.pop(0)
        result.append(cur.value)
        for i in cur.nexts:
            inMap[i]= inMap.get(i)-1
            if inMap[i] == 0:
                zeroInQueue.append(i)
    return result






if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.nexts = [node3, node2]
    node1.in_num = 0
    node1.out_num = 2
    node2.nexts = [node3, node4]
    node2.in_num = 1
    node2.out_num = 2
    node3.nexts = [node4]
    node3.in_num = 2
    node3.out_num = 1
    node4.in_num = 2

    graph = Graph()
    graph.nodes = {1:node1, 2:node2, 3:node3, 4:node4}
    res = TopologySort(graph)
    print(res)






