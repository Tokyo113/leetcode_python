#coding:utf-8
'''
@Time: 2019/10/29 16:06
@author: Tokyo
@file: code_01_PreInPosTraversal.py
@desc:二叉树先序中序后序遍历的递归和非递归实现
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
        self.left = None
        self.right = None
        self.ele = num



def preOrderRecur(node):
    if node is None:
        return
    print(node.ele, end=" ")
    preOrderRecur(node.left)
    preOrderRecur(node.right)

def inOrderRecur(node):
    if node is None:
        return
    inOrderRecur(node.left)
    print(node.ele, end=" ")
    inOrderRecur(node.right)

def posOrderRecur(node):
    if node is None:
        return
    posOrderRecur(node.left)
    posOrderRecur(node.right)
    print(node.ele, end=" ")

def preOrderUnRecur(node):
    """
    先序遍历非递归实现
    :param node:
    """
    if node is None:
        return
    stack = Stack()
    stack.push(node)
    while not stack.is_empty():
        head = stack.pop()
        print(head.ele, end=" ")
        if head.right != None:
            stack.push(head.right)
        if head.left != None:
            stack.push(head.left)

def posOrderUnrecur(node):
    if node is None:
        return
    s1 = Stack()
    s2 = Stack()
    s1.push(node)
    while not s1.is_empty():
        head = s1.pop()
        s2.push(head)
        if head.left != None:
            s1.push(head.left)
        if head.right != None:
            s1.push(head.right)
    while not s2.is_empty():
        node = s2.pop()
        print(node.ele, end=" ")


def inOrderUnRecur(node):
    if node is None:
        return
    s = Stack()
    while node is not None or not s.is_empty():
        if node != None:
            s.push(node)
            node = node.left
        else:
            node = s.pop()
            print(node.ele, end=" ")
            node = node.right

def posorder(head):
    if head is None:
        return None
    stack = Stack()
    s2 = Stack()
    stack.push(head)
    while not stack.is_empty():
        head = stack.pop()

        if head.left != None:
            stack.push(head.left)
        if head.right != None:
            stack.push(head.right)
        s2.push(head)

    while not s2.is_empty():
        print(s2.pop().ele, end=" ")

def inorder(head):
    if head is None:
        return None
    stack = Stack()
    while head != None or not stack.is_empty():
        if head != None:
            stack.push(head)
            head = head.left
        else:
            head = stack.pop()
            print(head.ele, end=" ")
            head = head.right



if __name__ == '__main__':
    head = Node(5)
    head.left = Node(3)
    head.right = Node(8)
    head.left.left = Node(2)
    head.left.right = Node(4)
    head.left.left.left = Node(1)
    head.right.left = Node(7)
    head.right.left.left = Node(6)
    head.right.right = Node(10)
    head.right.right.left = Node(9)
    head.right.right.right = Node(11)
    print("===================Recur======================")
    print("Pre-order :")
    preOrderRecur(head)
    print("")
    print("in-order: ")
    inOrderRecur(head)
    print("")
    print("pos_order:")
    posOrderRecur(head)
    print("")
    print("===================UnRecur======================")
    print("pre-order:")
    preOrderUnRecur(head)
    print("")
    print("in-order:")
    inOrderUnRecur(head)
    print("")
    print("pos-order:")
    posOrderUnrecur(head)
    print("")
    print("=======================")
    inorder(head)

