#coding:utf-8
'''
@Time: 2020/2/21 15:47
@author: Tokyo
@file: code_17_biggestSubBST.py
@desc:
找到一棵二叉树中，最大的搜索二叉子树，返回最大搜索二叉子树的节点个数
'''

class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def getBiggestBST(head):
    if head is None:
        return 0
    return process(head)


def process(node):
    '''
    返回四个信息，再整合
    :param node:
    :return: min,max, isBST, maxsize
    '''
    if node is None:
        return None

    left = process(node.left)
    right = process(node.right)
    min1, max1 = node.val, node.val
    isBST = True
    maxSize = 0

    if left != None:
        min1 = min(min1, left[0])
        max1 = max(max1, left[1])

        if left[1] >= node.val or not left[2]:
            isBST = False

    if right != None:
        min1 = min(min1, right[0])
        max1 = max(max1, right[1])

        if right[0] <= node.val or not right[2]:
            isBST = False
    if left != None and right != None:

        maxSize = left[3]+right[3]+1 if isBST else max(left[3], right[3])
    elif left != None:
        maxSize = left[3]+1 if isBST else left[3]
    elif right != None:
        maxSize = right[3]+1 if isBST else right[3]
    else:
        maxSize = 1
    return min1, max1, isBST, maxSize




if __name__ == '__main__':
    head = Node(5)
    head.left = Node(3)
    head.right = Node(9)
    head.left.left = Node(2)
    head.left.left.left = Node(1)
    head.left.right = Node(4)
    head.right.left = Node(7)
    head.right.left.left = Node(6)
    head.right.left.right = Node(8)
    head.right.right = Node(10)

    print(getBiggestBST(head))




