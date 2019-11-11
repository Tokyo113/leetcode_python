#coding:utf-8
'''
@Time: 2019/10/23 16:45
@author: Tokyo
@file: code_27_findfirstIntersectNode.py
@desc:
两个单链表相交的一系列问题
【题目】给定两个可能有环也可能无环的单链表，头节点head1和head2。请实
现一个函数，如果两个链表相交，请返回相交的 第一个节点。如果不相交，返
回null
【要求】如果两个链表长度之和为N，时间复杂度请达到O(N)，额外空间复杂度
请达到O(1)。
'''



class Node(object):
    def __init__(self, num):
        self.ele = num
        self.next = None





def hasLoop_hash(head):
    map = {}
    cur = head
    while (cur != None):
        node = map.get(cur)
        if node != None:
            return cur
        else:
            map[cur] = 1
            cur = cur.next
    return None


def getLoopNode(head):
    """
    判断链表是否有环并返回入环节点
    :param head:
    """
    if head is None or head.next is None or head.next.next is None:
        return None
    fast = head.next.next
    slow = head.next
    while (fast != slow):
        if fast.next is None or fast.next.next is None:
            return None
        fast = fast.next.next
        slow = slow.next
    fast = head
    while (fast != slow):
        fast = fast.next
        slow = slow.next
    return fast

def noloop(head1, head2):
    """
    两个无环链表求交点
    :param head1:
    :param head2:

    """
    end1 = head1
    end2 = head2
    n = 0    # 两个链表长度之差
    while(end1.next != None):
        end1 = end1.next
        n += 1
    while (end2.next != None):
        end2 = end2.next
        n -= 1
    if end1 is end2:
        end1 = head1 if n >= 0 else head2
        end2 = head1 if end1 == head2 else head2
        n = abs(n)
        while(n > 0):

            end1 = end1.next
            n -= 1
        while (end1 != end2):
            end1 = end1.next
            end2 = end2.next
        return end1
    else:
        return None

def bothloop(head1, head2, loop1,loop2):
    if loop1 is loop2:
        # 不需要考虑loop后面的环，转化为无环链表求交点
        end1, end2 = head1, head2
        n = 0
        while end1.next != loop1:
            end1 = end1.next
            n += 1
        while end2.next != loop2:
            end2 = end2.next
            n -= 1
        end1 = head1 if n > 0 else head2
        end2 = head2 if end1 == head1 else head1
        n = abs(n)

        while(n>0):
            end1 = end1.next
            n -= 1
        while (end1 != end2):
            end1 = end1.next
            end2 = end2.next
        return end1

    else:
        cur = loop1.next
        while (cur != loop1):
            if cur is loop2:
                # 第三种情况,交点就是loop1或loop2
                return loop1
            else:
                cur = cur.next
        return None



def getInserctNode(head1, head2):
    if head1 is None or head2 is None:
        return None

    loop1 = getLoopNode(head1)
    loop2 = getLoopNode(head2)

    # 判断是否有环，分情况讨论
    if loop1 is None and loop2 is None:
        return noloop(head1, head2)
    elif loop1 != None and loop2 != None:
        return bothloop(head1, head2, loop1, loop2)
    else:
        return None


def lpp(head):
    if head is None or head.next is None or head.next.next is None:
        return None

    fast, slow = head.next.next, head.next
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


def findfirstnode(head1, head2):
    if head1 is None or head2 is None:
        return None
    loop1 = lpp(head1)
    loop2 = lpp(head2)
    if loop1 is None and loop2 is None:
        loop1, loop2 = head1, head2
        n = 0
        while loop1.next != None:
            loop1 = loop1.next
            n += 1
        while loop2.next != None:
            loop2 = loop2.next
            n -= 1
        if loop1 is loop2:
            loop1 = head1 if n > 0 else head2
            loop2 = head2 if loop1 == head1 else head1
            n = abs(n)
            while n > 0:
                loop1 = loop1.next
                n -= 1

            while loop1 != loop2:
                loop1 = loop1.next
                loop2 = loop2.next
            return loop1

        else:
            return None
    elif loop1 != None and loop2 != None:
        if loop2 is loop1:
            end1, end2 = head1, head2
            n = 0
            while end1 != loop1:
                end1 = end1.next
                n += 1
            while end2 != loop2:
                end2 = end2.next
                n -= 1

            end1 = head1 if n > 0 else head2
            end2 = head2 if end1 == head1 else head1
            n = abs(n)
            while n > 0:
                end1 = end1.next
                n -= 1
            while end1 != end2:
                end1 = end1.next
                end2 = end2.next
            return end1


        else:
            cur = loop1.next
            while cur !=loop1:
                if cur == loop2:
                    return cur
                cur = cur.next
            return None

    else:
        return None




if __name__ == '__main__':
    # 1,2,3,4,5,6,7
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next =Node(3)
    head1.next.next.next =Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)
    # print(hasLoop_hash(head1))
    # print(getLoopNode(head1))
    #
    # # 0->9->8->6->7->null
    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next.next.next.next.next # 8->6
    # print(getInserctNode(head1, head2).ele)

    #
    # # 1->2->3->4->5->6->7->4...
    # head1 = Node(1)
    # head1.next = Node(2)
    # head1.next.next = Node(3)
    # head1.next.next.next = Node(4)
    # head1.next.next.next.next = Node(5)
    # head1.next.next.next.next.next = Node(6)
    # head1.next.next.next.next.next.next = Node(7)
    # head1.next.next.next.next.next.next = head1.next.next.next  # 7->4
    # print(hasLoop_hash(head1).ele)
    # print(getLoopNode(head1).ele)

    # 0->9->8->2...
    # head2 = Node(0)
    # head2.next = Node(9)
    # head2.next.next = Node(8)
    # head2.next.next.next = head1.next # 8->2
    # print(getInserctNode(head1, head2).ele)
    #
    #
    # # 0->9->8->6->4->5->6..
    # head2 = Node(0)
    # head2.next = Node(9)
    # head2.next.next = Node(8)
    # head2.next.next.next = head1.next.next.next.next.next # 8->6
    print(getInserctNode(head1, head2).ele)
    print(findfirstnode(head1, head2).ele)

