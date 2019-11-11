#coding:utf-8
'''
@Time: 2019/10/22 19:53
@author: Tokyo
@file: code_25_smallerequalbigger.py
@desc:
将单向链表按某值划分成左边小，中间相等，右边大的形式
给定一个单链表的头节点head，节点的值类型是整型，再给定一个整
数pivot。实现一个调整链表的函数，将链表调整为左部分都是值小于pivot的
节点，中间部分都是值等于pivot的节点，右部分都是值大于pivot的节点
【进阶】在实现原问题功能的基础上增加如下的要求
【要求】调整后所有小于pivot的节点之间的相对顺序和调整前一样
【要求】调整后所有等于pivot的节点之间的相对顺序和调整前一样
【要求】调整后所有大于pivot的节点之间的相对顺序和调整前一样
【要求】时间复杂度请达到O(N)，额外空间复杂度请达到O(1)。



'''

class Node(object):
    def __init__(self, num):
        self.ele = num
        self.next = None


def smallerequalbigger1(head, num):
    """
    不考虑空间复杂度，直接在数组中进行partition,但是是不稳定的
    :param head:
    :param num:
    """
    if head is None:
        return
    cur = head
    node_list = []
    # put the nodes into list
    while (cur != None):
        node_list.append(cur)
        cur = cur.next
    # partition
    cur = 0
    less, more = -1, len(node_list)
    while cur < more:
        if node_list[cur].ele < num:
            node_list[cur], node_list[less+1] = node_list[less+1], node_list[cur]
            less += 1
            cur += 1
        elif node_list[cur].ele > num:
            node_list[cur], node_list[more-1] = node_list[more-1], node_list[cur]
            more -= 1
        else:
            cur += 1
    # link the nodes as linkedlist
    head_new = node_list[0]
    for i in range(1, len(node_list)):
        node_list[i-1].next = node_list[i]
        if i == len(node_list)-1:
            node_list[i].next = None

    return head_new


def smallerequalbigger2(head, num):
    """
    面试时，额外空间复杂度为O(1)
    而且是稳定的，不会改变元素顺序
    :param head:
    :param num:
    """
    sH, sT = None, None
    eH, eT = None, None
    bH, bT = None, None
    # 每次取一个节点，同时打断之前的链接
    while head != None:
        next = head.next
        head.next = None
        if head.ele < num:
            if sH is None:
                sH = head
                sT = head
            else:
                sT.next = head
                sT = head
        elif head.ele > num:
            if bH is None:
                bH = head
                bT = head
            else:
                bT.next = head
                bT = head
        else:
            if eH is None:
                eH = head
                eT = head

            else:
                eT.next = head
                eT = head
        head = next

    # connect the three part
    # 某一部分可能为空链表，注意分情况
    # connect small and equal
    if sT != None:
        sT.next = eH
        eT = eT if eT != None else sT
    # connect all, eT 不为空意味着小于区或者等于区必然有一个不为空，包含了上面的情况
    if eT != None:
        eT.next = bH

    if sH != None:
        return sH
    else:
        return eH if eH != None else bH




def fenfenfen(head, num):
    if head is None:
        return None
    sH,sT = None, None
    eH, eT = None, None
    bH, bT = None, None

    while head != None:
        next = head.next
        head.next = None
        if head.ele < num:
            if sH is None:
                sH = head
                sT = head
            else:
                sT.next = head
                sT = head
        elif head.ele == num:
            if eH is None:
                eH = head
                eT = head
            else:
                eT.next = head
                eT = head
        else:
            if bH is None:
                bH = head
                bT = head
            else:
                bT.next = head
                bT = head
        head = next


    # join
    if sT !=None:
        if eH != None:
            sT.next = eH
        else:
            eT = sT
    if eT != None:
        eT.next = bH


    if sT != None:
        return sH
    else:
        return eH if eH != None else bH




def printLinkedlist(head):
    cur = head
    while (cur != None):
        print(cur.ele, end=" ")
        cur = cur.next
    print("")


if __name__ == '__main__':
    head1 = Node(7)
    head1.next = Node(9)
    head1.next.next = Node(1)
    head1.next.next.next = Node(8)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(2)
    head1.next.next.next.next.next.next = Node(5)
    printLinkedlist(head1)
    # head_1 = smallerequalbigger1(head1, 5)
    head_2 = fenfenfen(head1, 6)
    # printLinkedlist(head_1)
    printLinkedlist(head_2)

