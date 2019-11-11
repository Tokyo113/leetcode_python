#coding:utf-8
'''
@Time: 2019/10/23 11:17
@author: Tokyo
@file: code_26_copyListwithRandom.py
@desc:
复制含有随机指针节点的链表

rand指针是单链表节点结构中新增的指针，rand可能指向链表中的任意一个节
点，也可能指向null。给定一个由Node节点类型组成的无环单链表的头节点
head，请实现一个函数完成这个链表的复制，并返回复制的新链表的头节点。
【要求】时间复杂度O(N)，额外空间复杂度O(1)
'''

class Node(object):
    def __init__(self, num):
        self.ele = num
        self.next = None
        self.rand = None


def copyListwithRand1(head):
    """
    法1：哈希表, 额外空间O(N)
    :param head: 
    """
    hashmap = {}
    cur = head
    while (cur != None):
        hashmap[cur] = Node(cur.ele)
        cur = cur.next
    cur = head
    while (cur != None):
        hashmap.get(cur).next = hashmap.get(cur.next)
        hashmap.get(cur).rand = hashmap.get(cur.rand)
        cur = cur.next
    return hashmap.get(head)


def copyListwithRand2(head):
    """
    额外空间复杂度O(1),coding能力！！！
    :param head:
    """
    cur = head
    # copy node and link to every node
    while cur != None:
        next = cur.next
        cur.next = Node(cur.ele)
        cur.next.next = next
        cur = next
    # set copy node rand
    cur = head
    while cur != None:
        next = cur.next.next
        copycur = cur.next
        copycur.rand = cur.rand.next if cur.rand != None else None
        cur = next
    # split
    cur = head
    copyhead = cur.next

    while cur != None:
        next = cur.next.next
        copycur = cur.next
        cur.next = next
        copycur.next = next.next if next != None else None
        cur = next
    return copyhead


def printRandLinkedlist(head):
    cur = head
    print("order:", end=" ")
    while cur is not None:
        print(cur.ele, end=" ")
        cur = cur.next
    print("")
    print("rand:", end=" ")
    cur = head
    while cur is not None:
        print(cur.rand.ele if cur.rand is not None else "-", end=" ")
        cur = cur.next
    print("")



def fuzhi(head):
    if head is None:
        return None
    cur = head
    head1 = head
    while head != None:
        next = head.next
        node = Node(head.ele)
        head.next = node
        node.next = next
        head = next

    while cur != None:
        next = cur.next.next
        copynode = cur.next
        copynode.rand = cur.rand.next if cur.rand != None else None
        cur = next

    new_head = head1.next
    while head1 != None:
        next = head1.next.next
        copynode = head1.next
        head1.next = next
        copynode.next = next.next if next != None else None
        head1 = next
    return new_head




'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None
        cur = head
        
        while cur != None:
            next1 = cur.next
            cur.next = Node(cur.val, None, None)
            cur.next.next = next1
            cur = next1
        
        
        cur = head
        while cur != None:
            next1 = cur.next.next
            copynode = cur.next
            copynode.random = cur.random.next if cur.random != None else None
            cur = next1
        
        new_head = head.next
        cur = head
        while cur != None:
            next1 = cur.next.next
            cur.next = next1
            copynode = cur.next
            copynode.next = next1.next if next1 != None else None
            cur = next1
        
        return new_head

'''







if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.rand = head.next.next.next.next.next # 1 -> 6
    head.next.rand = head.next.next.next.next.next # 2 -> 6
    head.next.next.rand = head.next.next.next.next # 3 -> 5
    head.next.next.next.rand = head.next.next # 4 -> 3
    head.next.next.next.next.rand = None # 5 -> null
    head.next.next.next.next.next.rand = head.next.next.next # 6 -> 4
    printRandLinkedlist(head)
    head1 = copyListwithRand1(head)
    printRandLinkedlist(head1)
    print("="*50)
    head2 = copyListwithRand2(head)
    printRandLinkedlist(head2)
    print("=================")
    head3 = fuzhi(head)
    printRandLinkedlist(head3)
    head33 = aaa(head)