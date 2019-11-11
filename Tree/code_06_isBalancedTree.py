#coding:utf-8
'''
@Time: 2019/11/4 15:24
@author: Tokyo
@file: code_06_isBalancedTree.py
@desc:
'''

class Node(object):
    def __init__(self, num):
        self.right = None
        self.left = None
        self.ele = num



def isBalancedTree(head):
    return process(head)[0]


def process(head):
    if head is None:
        return True, 0

    leftData = process(head.left)
    rightData = process(head.right)

    height = max(leftData[1], rightData[1])+1

    isBance = leftData[0] and rightData[0] and (abs(leftData[1]-rightData[1]) <= 1)
    return isBance, height




if __name__ == '__main__':

    head = Node(5)
    head.left = Node(3)
    head.right = Node(10)
    head.right.left = Node(7)
    head.right.right = Node(7)
    head.right.left.right = Node(7)
    # head.left.left = Node(2)
    # head.left.right = Node(4)
    print(isBalancedTree(head))
    print(isbbbb(head))





