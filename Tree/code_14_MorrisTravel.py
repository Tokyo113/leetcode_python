#coding:utf-8
'''
@Time: 2019/12/2 16:40
@author: Tokyo
@file: code_14_MorrisTravel.py
@desc:
'''
import sys
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def morris(head):
    if head is None:
        return
    cur = head
    mostRight = None
    while cur != None:
        mostRight = cur.left
        if mostRight != None:
            while mostRight.right != None and mostRight.right != cur:
                mostRight = mostRight.right
            if mostRight.right is None:
                # 第一次来到这里
                mostRight.right = cur
                cur = cur.left
                continue
            else:
                # 第二次来这里
                mostRight.right = None
        cur = cur.right

def morrisPre(head):
    '''
    对每个节点都在第一次到达它时打印
    第二次到达时不管
    :param head:
    :return:
    '''
    if head is None:
        return
    cur = head

    while cur != None:
        mostRight = cur.left
        if mostRight != None:
            while mostRight.right != None and mostRight.right != cur:
                mostRight = mostRight.right
            if mostRight.right is None:
                print(cur.val, end=' ')
                mostRight.right = cur
                cur = cur.left
                continue
            else:
                mostRight.right = None
        else:
            print(cur.val, end=' ')
        cur = cur.right

def morrisIn(head):
    '''
    中序遍历
    第二次到节点时才打印
    只能到一次的直接打印
    :param head:
    :return:
    '''
    if head is None:
        return
    cur = head
    while cur != None:
        mostRight = cur.left

        if mostRight != None:
            while mostRight.right != None and mostRight.right != cur:
                mostRight = mostRight.right

            if mostRight.right is None:
                mostRight.right = cur
                cur = cur.left
                continue
            else:
                mostRight.right = None
        print(cur.val, end=' ')
        cur = cur.right

def morrisPos(head):
    '''
    后序遍历
    第二次到达时逆序打印其左子树的右边界
    :param head:
    :return:
    '''
    if head is None:
        return
    cur = head
    while cur != None:
        mostRight = cur.left
        if mostRight != None:
            while mostRight.right != None and mostRight.right != cur:
                mostRight = mostRight.right

            if mostRight.right is None:
                mostRight.right = cur
                cur = cur.left
                continue
            else:
                mostRight.right = None
                printEdge(cur.left)
        cur = cur.right
    # 最后打印整棵树的右边界
    printEdge(head)
    print("")


def printEdge(head):
    '''
    逆序打印head为头节点的树的右边界
    :param head:
    :return:
    '''
    tail = reverseEdge(head)
    cur = tail
    while cur != None:
        print(cur.val, end=" ")
        cur = cur.right

    reverseEdge(tail)

def reverseEdge(head):
    pre = None
    while head != None:
        next = head.right
        head.right = pre
        pre = head
        head = next

    return pre


def isBst(head):
    '''
    判断搜索二叉树
    :param head:
    :return:
    '''
    if head is None:
        return True
    cur = head
    minvalue = sys.float_info.min
    while cur != None:
        mostRight = cur.left
        if mostRight != None:
            while mostRight.right != None and mostRight.right != cur:
                mostRight = mostRight.right
            if mostRight.right is None:
                mostRight.right = cur
                cur = cur.left
                continue
            else:
                mostRight.right = None
        if cur.val <= minvalue:
            return False
        else:
            minvalue = cur.val
        cur = cur.right
    return True





if __name__ == '__main__':

    head = Node(4)
    head.left = Node(2)
    head.right = Node(6)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.right.left = Node(5)
    head.right.right = Node(7)

    print('In Order:', end=" ")
    morrisIn(head)
    print("")
    print('Pre Order:', end=" ")
    morrisPre(head)
    print("")
    print('Pos Order:', end=" ")
    morrisPos(head)
    # morrisPos(head)
    print("")
    print(isBst(head))

