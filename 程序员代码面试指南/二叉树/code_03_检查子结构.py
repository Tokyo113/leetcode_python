#coding:utf-8
'''
@Time: 2020/4/9 11:40
@author: Tokyo
@file: code_03_检查子结构.py
@desc:
'''


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def subTree(head1, head2):
    '''
    遍历t1每个节点判断是否满足
    O(N*M)
    :param head1:
    :param head2:
    :return:
    '''
    if head1 is None or head2 is None:
        return False

    def process(node1, node2):
        if node1.val != node2.val:
            return False
        if node2 is None:
            return True
        if node1 is None:
            return False
        return process(node1.left,node2.left) and process(node1.right,node2.right)


    queue = []
    queue.append(head1)
    while queue != []:
        pp = queue.pop(0)
        if process(pp, head2):
            return True
        if pp.left != None:
            queue.append(pp.left)
        if pp.right != None:
            queue.append(pp.right)
    return False
