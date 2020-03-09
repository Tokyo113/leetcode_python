#coding:utf-8
'''
@Time: 2020/3/7 21:19
@author: Tokyo
@file: code_28_deleteNode.py
@desc:
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

'''
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def deleteNode(head):
    if head is None:
        return None
    dum = Node(-1)
    dum.next = head
    pre = dum
    L = head
    while pre != None:
        if pre.next is None:
            break
        L = pre.next
        R = L.next
        while R != None:
            if L.val != R.val:
                break
            R = R.next
        if R != L.next:
            pre.next = R
        else:
            pre = L
    return dum.next

def printLinkedlist(head):
    cur = head
    while (cur != None):
        print(cur.val, end=" ")
        cur = cur.next
    print("")
if __name__ == '__main__':
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    printLinkedlist(deleteNode(head))

