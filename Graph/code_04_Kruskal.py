#coding:utf-8
'''
@Time: 2019/11/7 20:33
@author: Tokyo
@file: code_04_Kruskal.py
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


def mysets(nodes):
    set_map = {}
    for cur in nodes:
        node_set = []
        node_set.append(cur)
        set_map[cur] = node_set

def isSameSet(from_node, to_node, set_map):
    fromSet = set_map[from_node]
    toSet = set_map[to_node]
    return  fromSet == toSet


def union(from_node, to_node, set_map):
    fromSet = set_map[from_node]
    toSet = set_map[to_node]
    for tonode in toSet:
        fromSet.append(tonode)
        set_map[tonode] = fromSet


if __name__ == '__main__':
