#coding:utf-8
'''
@Time: 2019/11/8 9:16
@author: Tokyo
@file: code_06_Graph.py
@desc:
'''

class Graph(object):
    def __init__(self):
        self.nodes = {}
        self.edges = []


class Node(object):
    def __init__(self, val):
        self.value = val
        self.in_num = 0
        self.out_num = 0
        self.nexts = []
        self.edges = []


class Edge(object):
    def __init__(self, val, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = val

    def __lt__(self, other):
        return self.weight < other.weight