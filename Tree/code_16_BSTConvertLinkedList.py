#coding:utf-8
'''
@Time: 2020/2/21 12:24
@author: Tokyo
@file: code_16_BSTConvertLinkedList.py
@desc:
双向链表节点结构和二叉树节点结构是一样的，如果你把last认为是left，
next认为是right的话。
给定一个搜索二叉树的头节点head，请转化成一条有序的双向链表，并返回链
表的头节点。
进阶：改成循环双向链表
二叉树的套路解法
循环双向链表的话
1：还按照普通双向链表做，最后连起来头和尾
2.见方法二，只返回一个节点即可
'''

class Node():
    def __init__(self, num):
        self.left = None
        self.right = None
        self.val = num


def convert(head):
    if head is None:
        return None
    return process(head)[0]

def process(node):
    if node is None:
        return None, None
    left = process(node.left)
    right = process(node.right)
    if left[1] != None:
        left[1].right = node
    if right[0] != None:
        right[0].left = node
    node.left = left[1]
    node.right = right[0]

    head = node if left[0] is None else left[0]
    tail = node if right[1] is None else right[1]
    return head, tail

def treeToDoublyList(root):
    '''
    改为循环双向链表
    :param root:
    :return:
    '''
    if root is None:
        return None

    def process(head):
        if head is None:
            return None
        left = process(head.left)
        right = process(head.right)
        new = head
        if left is None and right is None:
            new.left = head
            new.right = head
        if left != None:
            last = left.left
            last.right = head
            head.left = last
            left.left = head
            head.right = left
            new = left
        if right != None:
            last = right.left
            right.left = head
            head.right = right
            last.right = new
            new.left = last
        return new

    return process(root)


def travelBST(head):
    if head is None:
        return
    stack = []
    while stack != [] or head != None:
        if head != None:
            stack.append(head)
            head = head.left
        else:
            head= stack.pop()
            print(head.val, end=' ')
            head = head.right
    print('')

def travelLinkedList(head):
    if head is None:
        return
    end = None

    while head!= None:
        print(head.val, end=' ')
        end = head
        head = head.right

    print('')
    while end != None:
        print(end.val, end=' ')
        end = end.left


if __name__ == '__main__':

    head =Node(5)
    head.left = Node(2)
    head.right = Node(9)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.left.right.right = Node(4)
    head.right.left = Node(7)
    head.right.right = Node(10)
    head.left.left = Node(1)
    head.right.left.left = Node(6)
    head.right.left.right = Node(8)

    travelBST(head)
    listHead = convert(head)
    travelLinkedList(listHead)




