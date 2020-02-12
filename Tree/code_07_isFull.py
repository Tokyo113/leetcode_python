#coding:utf-8
'''
@Time: 2019/11/4 20:33
@author: Tokyo
@file: code_07_isFull.py
@desc:
判断是否是满二叉树
使用二叉树的递归套路
返回子树的节点数和层数
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




def manerchashu(head):
    if head is None:
        return True
    res = process1(head)
    return res[1] == 2**res[0]-1

def process1(head):
    if head is None:
        return 0, 0
    l = process1(head.left)
    r = process1(head.right)
    num = l[1]+r[1]+1
    height = max(l[0], r[0])+1

    return height, num


if __name__ == '__main__':
    head = Node(5)
    head.left = Node(3)
    head.right = Node(10)
    head.right.left = Node(7)
    head.right.right = Node(8)
    head.right.left.right = Node(7)
    head.left.left = Node(2)
    head.left.right = Node(4)
    print(isFull(head))
    print(full(head))
    print(manerchashu(head))