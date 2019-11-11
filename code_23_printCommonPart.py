#coding:utf-8
'''
@Time: 2019/10/22 15:02
@author: Tokyo
@file: code_23_printCommonPart.py
@desc: 打印两个有序链表的公共部分
'''

class Node(object):
    def __init__(self, num):
        self.ele = num
        self.next = None


def printCommonPart(node1, node2):
    cur1 = node1
    cur2 = node2
    while (cur1 != None and cur2 != None):
        if cur1.ele < cur2.ele:
            cur1 = cur1.next
        elif cur1.ele > cur2.ele:
            cur2 = cur2.next
        else:
            print(cur1.ele, end=" ")
            cur1 = cur1.next
            cur2 = cur2.next
    print("")





if __name__ == '__main__':
    a = Node(2)
    b = Node(3)
    a.next = Node(5)
    a.next.next = Node(8)
    b.next = Node(4)
    b.next.next = Node(5)
    b.next.next.next = Node(8)
    printCommonPart(a, b)
    printgongong(a, b)