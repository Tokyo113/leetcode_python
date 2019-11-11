#coding:utf-8
'''
@Time: 2019/11/5 9:24
@author: Tokyo
@file: code_08_LowestCommonAncestor.py
@desc:
给定二叉树的两个节点node1和node2，
找到他们的最低公共祖先节点
'''


class Node(object):
    def __init__(self, num):
        self.right = None
        self.left = None
        self.ele = num


def LowestCommonAncestor(head, node1, node2):
    fathermap = {}
    # 哈希表存放父节点
    fathermap[head] = head
    process(head, fathermap)
    nodes_set = set()
    # 边界条件,
    if node1 == head and node2 == head:
        return head
    while node1 != fathermap[node1]:
        nodes_set.add(fathermap[node1])
        node1 = fathermap[node1]
    nodes_set.add(head)

    while node2 != fathermap[node2]:
        if fathermap[node2] in nodes_set:
            return fathermap[node2]
        node2 = fathermap[node2]
    return None


def process(head, map):
    if head is None:
        return
    if head.left != None:
        map[head.left] = head
    if head.right != None:
        map[head.right] = head
    process(head.left, map)
    process(head.right, map)



def LowestCommonAncestor1(head, o1, o2):
    if head is None or head == o1 or head == o2:
        return head

    left = LowestCommonAncestor1(head.left, o1, o2)
    right = LowestCommonAncestor1(head.right, o1, o2)
    if left != None and right != None:
        return head
    return left if left != None else right


def lowest(head, node1, node2):
    if head is None or head == node2 or head == node1:
        return head

    left = lowest(head.left, node1, node2)
    right = lowest(head.right, node1, node2)
    if left != None and right != None:
        return head

    return left if left != None else right







if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)
    head.right.right.left = Node(8)
    print("===============")
    o1 = head.right.right.left
    o2 = head.right.left
    print("o1 : ", o1.ele)
    print("o2 : ", o2.ele)
    print("ancestor : ", LowestCommonAncestor(head, o1, o2).ele)
    print("ancestor_plus : ", LowestCommonAncestor1(head, o1, o2).ele)
    print("ancestor : ", LowestCommonAncestor(head, head, o2).ele)
    print("ancestor_plus : ", LowestCommonAncestor1(head, head, o2).ele)
    print("===============")
    print(lowest(head, o1, o2).ele)



