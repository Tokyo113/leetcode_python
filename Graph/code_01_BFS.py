#coding:utf-8
'''
@Time: 2019/11/7 16:31
@author: Tokyo
@file: code_01_BFS.py
@desc:图的宽度优先遍历
'''

class Node(object):
    def __init__(self, num):
        self.value = num
        self.in_num = 0
        self.out_num = 0
        self.nexts = []
        self.edge = []



def BFS(node):
    queue = []
    nodeset = set()
    queue.append(node)
    nodeset.add(node)

    while queue != []:
        cur = queue.pop(0)
        print(cur.value, end=" ")

        for next in cur.nexts:
            if (not next in nodeset):
                nodeset.add(next)
                queue.append(next)






if __name__ == '__main__':
    node = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    node3 = Node(4)
    node4 = Node(5)
    node.nexts = [node1, node2,node3]
    node1.nexts = [node]
    node2.nexts = [node]
    node3.nexts = [node, node4]
    node4.nexts = [node3]
    BFS(node)
    print(bfs(node))



