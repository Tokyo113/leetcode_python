#coding:utf-8
'''
@Time: 2019/10/21 21:25
@author: Tokyo
@file: code_22_reverseLinkedlist.py
@desc:
'''

class Node(object):
    def __init__(self, num):
        self.ele = num
        self.next = None


def reverseLinkedlist(head):
    pre = None
    while head != None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre



class DoubleNode(object):
    def __init__(self, num):
        self.ele = num
        self.pre = None
        self.next = None


def reverseDoubleList(head):
    pre = None
    while head != None:
        next = head.next
        head.next = pre
        head.pre = next
        pre = head
        head = next
    return pre



def printLinkedlist(head):
    cur = head
    while (cur != None):
        print(cur.ele, end=" ")
        cur = cur.next
    print("")
if __name__ == '__main__':
    a = DoubleNode(1)
    a.next = DoubleNode(2)
    a.next.next = DoubleNode(-9)
    a.next.next.next = DoubleNode(8)

    head = Node(1)
    head.next = Node(9)
    head.next.next = Node(5)
    head.next.next.next = Node(2)
    printLinkedlist(a)
    b = reverseDoubleList(a)
    printLinkedlist(b)

