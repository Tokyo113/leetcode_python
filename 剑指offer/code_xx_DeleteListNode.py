#coding:utf-8
'''
@Time: 2020/3/22 16:20
@author: Tokyo
@file: code_xx_DeleteListNode.py
@desc:
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplication(pHead):
    # write code here
    if pHead is None:
        return
    dum = ListNode(-1)
    dum.next = pHead
    cur = dum

    while cur != None:
        if cur.next is None:
            break
        L = cur.next
        R = L.next
        while R != None:
            if L.val == R.val:
                R = R.next
            else:
                break
        if R != L.next:
            cur.next = R
        else:
            cur = L
    return dum.next