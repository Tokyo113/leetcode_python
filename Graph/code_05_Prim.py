#coding:utf-8
'''
@Time: 2019/11/7 21:40
@author: Tokyo
@file: code_05_Prim.py
@desc:
'''

import queue
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

    def __lt__(self, other):
        # 重定义比较器
        return self.weight < other.weight


def primMst(graph):
    priorityQueue = queue.PriorityQueue
    set_node = set()
    result = set()
    # 考虑森林的情况，几个图不连通
    for node in graph.nodes.values():
        # 任选一个点开始
        if not node in set_node:
            set_node.add(node)
            # 解锁相连的边
            for edge in node.edges:
                priorityQueue.put(edge)


            while not priorityQueue.empty():
                # 弹出最小的边
                edge = priorityQueue.get()
                # 边的另一个节点
                toNode = edge.to_node
                if not toNode in set_node:
                    set_node.add(toNode)
                    result.add(edge)
                    # 解锁该点连接的边
                    for nextEdge in toNode.edges:
                        priorityQueue.put(nextEdge)

    return result


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)


    que = queue.PriorityQueue()
    que.put(9)
    que.put(2)
    que.put(4)
    que.put(7)
    que.put(5)

    que.put(3)
    print(que.get())
    print(que.get())


