#coding:utf-8
'''
@Time: 2019/11/28 17:45
@author: Tokyo
@file: code_12_MaxDistanceTree.py
@desc:
二叉树节点间的最大距离问题
从二叉树的节点a出发，可以向上或者向下走，但沿途的节点只能经过一次，到达节点b时路
径上的节点个数叫作a到b的距离，那么二叉树任何两个节点之间都有距离，求整棵树上的最
大距离。

'''

class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val



def getMaxDistance(head):
    return process(head)[0]


def process(head):
    '''
    向子树要最大距离和高度信息
    :param head:
    :return:
    '''
    if head is None:
        return 0, 0

    left = process(head.left)
    right = process(head.right)

    height = 1 + max(left[1], right[1])
    maxDistance = max(left[0], right[0], left[1]+right[1]+1)

    return maxDistance, height

def juli(head):
    if head is None:
        return 0
    return process1(head)[1]

def process1(node):
    if node is None:
        return 0,0
    left = process1(node.left)
    right = process1(node.right)
    height = max(left[0], right[0])+1
    dis = max(left[1], right[1], right[0]+left[0]+1)
    return height, dis



if __name__ == '__main__':

    head1 = Node(1)
    head1.left = Node(2)
    head1.right = Node(3)
    head1.left.left = Node(4)
    head1.left.right = Node(5)
    head1.right.left = Node(6)
    head1.right.right = Node(7)
    head1.left.left.left = Node(8)
    head1.right.left.right = Node(9)
    print(getMaxDistance(head1))

    head2 = Node(1)
    head2.left = Node(2)
    head2.right = Node(3)
    head2.right.left = Node(4)
    head2.right.right = Node(5)
    head2.right.left.left = Node(6)
    head2.right.right.right = Node(7)
    head2.right.left.left.left = Node(8)
    head2.right.right.right.right = Node(9)
    print(getMaxDistance(head2))
    print(juli(head2))