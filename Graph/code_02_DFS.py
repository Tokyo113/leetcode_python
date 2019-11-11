#coding:utf-8
'''
@Time: 2019/11/7 18:35
@author: Tokyo
@file: code_02_DFS.py
@desc:
'''

class Node(object):
    def __init__(self, num):
        self.value = num
        self.in_num = 0
        self.out_num = 0
        self.nexts = []
        self.edge = []



def DFS(node):
    if node is None:
        return None

    stack = []
    node_set = set()

    stack.append(node)
    node_set.add(node)
    print(node.value, end=" ")
    while stack != []:
        cur = stack.pop()
        for i in cur.nexts:
            if not i in node_set:
                stack.append(cur)
                stack.append(i)
                node_set.add(i)
                print(i.value, end=" ")
                break




if __name__ == '__main__':
    node = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    node3 = Node(4)
    node4 = Node(5)
    node5 = Node(6)
    node.nexts = [node3, node2,node1]
    node1.nexts = [node]
    node2.nexts = [node]
    node3.nexts = [node, node4]
    node4.nexts = [node3, node5]
    node5.nexts = [node4]
    DFS(node)
    print("")
    print(dfs(node))

