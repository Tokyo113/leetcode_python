#coding:utf-8
'''
@Time: 2020/2/22 12:50
@author: Tokyo
@file: code_19_CBTNodeNum.py
@desc:

求完全二叉树节点的个数
'''
class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def count(head):
    '''
    直接遍历，并非最优解
    :param head:
    :return:
    '''
    if head is None:
        return 0
    res = []

    def process(head):
        if head is None:
            return
        res.append(head.val)
        process(head.left)
        process(head.right)

    process(head)
    return len(res)



def countNode(head):
    '''
    最优解,O(logN*logN)=O(h^2)
    h是二叉树的高度
    :param head:
    :return:
    '''
    if head is None:
        return 0

    return process(head, 1, totalLevel(head, 1))

def process(node, cur, h):
    '''
    计算node为头的CBT子树有多少节点
    :param node:
    :param cur:
    :param h:
    :return:
    '''
    if cur == h:
        return 1
    if totalLevel(node.right, cur+1) == h:
        return 2**(h-cur)+process(node.right, cur+1, h)
    else:
        return 2**(h-cur-1)+process(node.left, cur+1, h)



def totalLevel(node, level):


    while node != None:
        node = node.left
        level += 1
    return level-1








if __name__ == '__main__':
    head = Node(5)
    head.left = Node(3)
    head.right = Node(10)
    head.right.left = Node(7)
    head.left.left = Node(2)
    head.left.right = Node(4)

    print(count(head))
    print(countNode(head))