#coding:utf-8
'''
@Time: 2019/10/29 19:02
@author: Tokyo
@file: code_02_printBinaryTree.py
@desc:
'''

class Node(object):
    def __init__(self, num):
        self.left = None
        self.right = None
        self.ele = num

def printTree(head):
    print("Binary Tree:")
    printInorder(head, 0, "H", 17)
    print("")

def printInorder(head, height, to, length):
    if head is None:
        return
    printInorder(head.right, height + 1, "v", length)
    val = to + str(head.ele) + to
    lenM = len(val)
    lenL = (length - lenM) // 2
    lenR = length - lenM - lenL
    val = getSpace(lenL) + val + getSpace(lenR)
    print(getSpace(height * length) + val)
    printInorder(head.left, height + 1, "^", length)


def getSpace(num):
    space = " "
    buf = ""
    for i in range(num):
        buf += space

    return buf


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.right.left = Node(5)
    head.right.right = Node(6)
    head.left.left.right = Node(7)
    printTree(head)

    head = Node(1)
    head.left = Node(1)
    head.right = Node(1)
    head.left.left = Node(1)
    head.right.left = Node(1)
    head.right.right = Node(1)
    head.left.left.right = Node(1)
    printTree(head);