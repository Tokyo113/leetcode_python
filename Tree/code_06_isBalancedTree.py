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


def pingheng(head):
    if head is None:
        return True
    return process1(head)[1]

def process1(head):
    if head is None:
        return 0 ,True

    isBt = True
    l = process1(head.left)
    r = process1(head.right)
    if not l[1] or not r[1] or abs(l[0]-r[0])>1:
        isBt = False
    height = max(l[0], r[0])+1
    return height, isBt




if __name__ == '__main__':

    head = Node(5)
    head.left = Node(3)
    head.right = Node(10)
    head.right.left = Node(7)
    head.right.right = Node(7)
    head.right.left.right = Node(7)
    head.left.left = Node(2)
    head.left.right = Node(4)
    print(isBalancedTree(head))
    print(pingheng(head))





