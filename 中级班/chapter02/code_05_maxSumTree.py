#coding:utf-8
'''
@Time: 2020/2/10 10:40
@author: Tokyo
@file: code_05_maxSumTree.py
@desc:

二叉树每个结点都有一个int型权值，给定一棵二叉树，要求计算出从根结点到
叶结点的所有路径中，权值和最大的值为多少。
'''

class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None






def maxSum(head):
    if head is None:
        return
    return process(head)


def process(node):
    if node.left == None and node.right == None:
        return node.val
    res = float('-inf')
    if node.left != None:
        res = process(node.left)
    if node.right != None:
        res = max(process(node.right), res)
    return node.val+res


if __name__ == '__main__':
    head = Node(-4)
    head.left =Node(-1)
    head.left.right = Node(-5)
    head.right = Node(-7)
    head.right.left = Node(-3)
    print(maxSum(head))
    print(ppp(head))





