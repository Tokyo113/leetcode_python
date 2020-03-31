#coding:utf-8
'''
@Time: 2020/3/31 22:08
@author: Tokyo
@file: code_29_约瑟夫环问题.py
@desc:
据说著名犹太历史学家 Josephus 有过以下故事：在罗马人占领乔塔帕特后，
39 个犹太人与 Josephus 及他的朋友躲到一个洞中，
39 个犹太人决定宁愿死也不要被敌人抓到，于是决定了一种自杀方式，
41 个人排成一个圆圈，由第 1 个人开始报数，报数到 3 的人就自杀，
然后再由下一个人重新报 1，报数到 3 的人再自杀，这样依次下去，
直到剩下最后一个人时，那个人可以自由选择自己的命运。这就是著名的约瑟夫问题。
现在请用单向环形链表得出最终存活的人的编号。
'''

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

def yuesefu(head, m):
    if head is None or m<1:
        return None
    # 环形链表，先找到尾部
    last = head
    while last.next != head:
        last = last.next

    count = 0
    while head != last:
        count += 1
        if count == m:
            last.next = head.next
            count = 0
        else:
            last = last.next
        head = last.next
    return head.val

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = head
    print(yuesefu(head,3))