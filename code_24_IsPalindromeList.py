#coding:utf-8
'''
@Time: 2019/10/22 16:41
@author: Tokyo
@file: code_24_IsPalindromeList.py
@desc:判断一个链表是否是回文结构
'''

class Stack(object):
    def __init__(self):
        self.__stack = []

    def push(self, num):
        self.__stack.append(num)

    def pop(self):
        if self.__stack == []:
            raise Exception("the stack is empty")
        return self.__stack.pop()

    def peek(self):
        if self.__stack == []:
            raise Exception("the stack is empty")
        return self.__stack[-1]

    def is_empty(self):
        return self.__stack == []

    def size(self):
        return len(self.__stack)


class Node(object):
    def __init__(self, num):
        self.ele = num
        self.next = None


def IsPalindromeList1(head):
    """
    使用栈结构，额外空间复杂度O（N）
    :param head:
    :return:
    """
    stack = Stack()
    cur = head
    while cur != None:
        stack.push(cur.ele)
        cur = cur.next
    cur = head
    while cur != None:
        res = stack.pop()
        if cur.ele != res:
            return False
        else:
            cur = cur.next
    return True

def IsPalindromeList2(head):
    """
    同样栈结构，额外空间N/2，少一半
    :param head:
    使用快慢指针，注意两个指针的起始位置
    """
    if head is None or head.next is None:
        return True
    fast = head
    slow = head.next
    stack = Stack()

    while(fast.next != None and fast.next.next != None):
        slow = slow.next
        fast = fast.next.next
    # 退出循环后，slow的位置就在链表中间后一个节点
    while slow is not None:
        stack.push(slow.ele)
        slow = slow.next

    while not stack.is_empty():
        if head.ele != stack.pop():
            return False

        head = head.next
    return True


def IsPalindromeList3(head):
    if head is None or head.next is None:
        return True
    fast = head
    slow = head
    # find the mid
    while (fast.next is not None and fast.next.next is not None):
        fast = fast.next.next
        slow = slow.next
    # reverse the right part of the Linkedlist
    pre = None
    while(slow != None):
        next = slow.next
        slow.next = pre
        pre = slow
        slow = next
    slow = pre   # the last node
    left = head  # the first node of left part
    res = True
    while (slow != None and left != None):
        if slow.ele == left.ele:
            slow = slow.next
            left = left.next
        else:
            res = False
            break
    # recover the Linkedlist
    head1 = pre
    pre = None
    while(head1 != None):
        next = head1.next
        head1.next = pre
        pre = head1
        head1 = next
    return res







def printLinkedlist(head):
    cur = head
    while (cur != None):
        print(cur.ele, end=" ")
        cur = cur.next
    print("")


if __name__ == '__main__':
    a = Node(None)
    printLinkedlist(a)
    print(IsPalindromeList1(a))
    print(IsPalindromeList2(a))
    print(IsPalindromeList3(a))
    print("="*50)
    b = Node(1)
    b.next = Node(2)
    printLinkedlist(b)
    print(IsPalindromeList1(b))
    print(IsPalindromeList2(b))
    print(IsPalindromeList3(b))
    print("=" * 50)
    c = Node(1)
    c.next = Node(5)
    c.next.next = Node(1)
    printLinkedlist(c)
    print(IsPalindromeList1(c))
    print(IsPalindromeList2(c))
    print(IsPalindromeList3(c))
    print("=" * 50)
    d=Node(2)
    d.next = Node(5)
    d.next.next = Node(5)
    d.next.next.next = Node(2)
    printLinkedlist(d)
    print(IsPalindromeList1(d))
    print(IsPalindromeList2(d))
    print(IsPalindromeList3(d))
    print("=" * 50)
