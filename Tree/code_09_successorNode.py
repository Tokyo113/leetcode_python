#coding:utf-8
'''
@Time: 2019/11/5 10:58
@author: Tokyo
@file: code_09_successorNode.py
@desc:
给定一棵二叉树和其中一个节点，
如何找到中序遍历序列的下一个节点？
树中除了左右子节点的指针，还多了一个指向父节点的指针

思路：
根据中序遍历的特点分情况讨论：
1.没有右子树
2.有右子树：右子树的最左节点
'''


class Node(object):
    def __init__(self, num):
        self.left = None
        self.right = None
        self.parent = None
        self.ele = num



def successorNode(node):
    if node is None:
        return None

    if node.right != None:
        return mostLeft(node.right)
    else:
        parent = node.parent
        while parent != None and parent.left != node:
            node = node.parent
            parent = node.parent
        return parent


def mostLeft(node):
    if node is None:
        return node
    while node.left != None:
        node = node.left

    return node


def successorNode1(node):
    if  node is None:
        return None
    if node.right != None:
        return findleft(head,node.right)
    else:
        parent = node.parent
        while parent != None and parent.left != node:
            node = parent
            parent = parent.parent
        return parent

def findleft(node):
    if node is None:
        return None
    while node.left != None:
        node = node.left

    return node








if __name__ == '__main__':
    head = Node(6)
    head.parent = None
    head.left = Node(3)
    head.left.parent = head
    head.left.left = Node(1)
    head.left.left.parent = head.left
    head.left.left.right = Node(2)
    head.left.left.right.parent = head.left.left
    head.left.right = Node(4)
    head.left.right.parent = head.left
    head.left.right.right = Node(5)
    head.left.right.right.parent = head.left.right
    head.right = Node(9)
    head.right.parent = head
    head.right.left = Node(8)
    head.right.left.parent = head.right
    head.right.left.left = Node(7)
    head.right.left.left.parent = head.right.left
    head.right.right = Node(10)
    head.right.right.parent = head.right

    test = head.left.left
    print(test.ele, " next: " , successorNode(test).ele)
    print(test.ele, " next: ", findNext(head,test).ele)


    test = head.left.left.right
    print(test.ele , " next: " ,successorNode(test).ele)

    test = head.left
    print(test.ele , " next: " , successorNode(test).ele)

    test = head.left.right
    print(test.ele , " next: " , successorNode(test).ele)
    test = head.left.right.right
    print(test.ele ," next: " , successorNode(test).ele)
    test = head
    print(test.ele , " next: " , successorNode(test).ele)
    test = head.right.left.left
    print(test.ele , " next: ", successorNode(test).ele)
    test = head.right.left
    print(test.ele , " next: " , successorNode(test).ele)
    test = head.right
    print(test.ele , " next: ", successorNode(test).ele)
    test = head.right.right  # 10's next is null
    print(successorNode(test))

