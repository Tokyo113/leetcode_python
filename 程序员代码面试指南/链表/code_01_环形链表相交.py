#coding:utf-8
'''
@Time: 2020/4/9 10:41
@author: Tokyo
@file: code_01_环形链表相交.py
@desc:
链表相交的一系列问题：
1.如何判断两个单链表是否相交（无环链表和环形链表不可能相交）
2.如何判断链表是否有环，返回入环节点
3.如何判断两个环形链表是否相交？
关键第三个问题
'''

class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

def hasLoop(head):
    if head is None or head.next is None or head.next.next is None:
        return None
    fast,slow = head.next.next,head.next
    while fast != slow:
        if fast.next is None or fast.next.next is None:
            return None
        fast = fast.next.next
        slow = slow.next
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast





def loopList(head1,head2):
    '''
    环形链表有三种情况
    1.不相交
    2.相交于入环节点之前
    3.在环内相交
    :param head1:
    :param head2:
    :return:
    '''
    if head1 is None or head2 is None:
        return None
    loop1 = hasLoop(head1)
    loop2 = hesLoop(head2)
    if loop1 == loop2:
        # 1.是否在入环节点之前相交,入环节点必然是同一个
        # 转化为两个单链表求交点
        cur1,cur2 = head1,head2
        d = 0
        while cur1 != loop1 or cur2 != loop2:
            if cur1 != loop1:
                d += 1
                cur1 = cur1.next
            if cur2 != loop2:
                d -= 1
                cur2 = cur2.next

        big = head1 if d>=0 else head2
        short = head2 if big == head1 else head1
        cur1,cur2 = big,short
        d = abs(d)
        while cur1 != cur2:
            if d>0:
                d -= 1
                cur1 = cur1.next
            else:
                cur1 = cur1.next
                cur2 = cur2.next
        return cur1
    else:
        cur1 = loop1.next
        while cur1 != loop1:
            if cur1 == loop2:
                return cur1
            cur1 = cur1.next
        return None




