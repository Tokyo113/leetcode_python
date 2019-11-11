#coding:utf-8
'''
@Time: 2019/11/7 22:53
@author: Tokyo
@file: leetcode_0563_tilt.py
@desc:

给定一个二叉树，计算整个树的坡度。

一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。

整个树的坡度就是其所有节点的坡度之和。

示例:

输入:
         1
       /   \
      2     3
输出: 1
解释:
结点的坡度 2 : 0
结点的坡度 3 : 0
结点的坡度 1 : |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1

'''

class Node(object):
    def __init__(self, num):
        self.val = num
        self.left = None
        self.right = None



def tilt(head):
    return process(head)[0]


def process(head):
    if head is None:
        return 0, 0

    left = process(head.left)
    right = process(head.right)
    tilt = left[0] + right[0] + abs(left[1]-right[1])
    sum = left[1] + right[1] + head.val
    return tilt, sum


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    print(tilt(head))



