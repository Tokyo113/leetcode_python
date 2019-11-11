#coding:utf-8
'''
@Time: 2019/11/4 20:33
@author: Tokyo
@file: code_07_isFull.py
@desc:满二叉树
'''


class Node(object):
    def __init__(self, num):
        self.right = None
        self.left = None
        self.ele = num


def isFull(head):

    height, nodes = process(head)
    return nodes == (2 ** height) - 1


def process(head):
    if head is None:
        return 0, 0

    data_left = process(head.left)
    data_right = process(head.right)
    height = max(data_left[0], data_right[0]) + 1
    nodes = data_left[1] + data_right[1] + 1

    return height, nodes



def full(head):
    return aaa(head)

def aaa(head):
    if head is None:
        return 0, 0, True
    isf = False
    left = aaa(head.left)
    right = aaa(head.right)
    nodes = left[0] + right[0] + 1
    level = max(right[1], left[1]) + 1

    if nodes == (2 ** level -1):
        isf = True
    return nodes, level, isf




if __name__ == '__main__':
    head = Node(5)
    head.left = Node(3)
    head.right = Node(10)
    head.right.left = Node(7)
    head.right.right = Node(8)
    # head.right.left.right = Node(7)
    # head.left.left = Node(2)
    # head.left.right = Node(4)
    print(isFull(head))
    print(full(head))