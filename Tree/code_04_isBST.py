#coding:utf-8
'''
@Time: 2019/10/31 16:43
@author: Tokyo
@file: code_04_isBST.py
@desc: binary search tree
二叉搜索树的判断-----中序遍历是否是升序
'''
import sys

pre_value = sys.float_info.min
prevalue = sys.float_info.min


class Node(object):
    def __init__(self, num):
        self.right = None
        self.left = None
        self.ele = num


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


def inorderRecur(head, li):
    if head is None:
        return
    inorderRecur(head.left, li)
    li.append(head.ele)
    inorderRecur(head.right, li)


def isBST1(head):
    """
    最简单的思路
    :param head:
    :return:
    """
    tree_li = []
    inorderRecur(head, tree_li)
    for i in range(1, len(tree_li)):
        if tree_li[i] < tree_li[i-1]:
            return False

    return True


def isBST2(head):
    """
    动态比较，在中序遍历的过程中比较, 递归实现
    :param head:
    """
    global pre_value
    if head is None:
        return True
    left_BST = isBST2(head.left)
    print(pre_value)
    if not left_BST:
        return False
    else:
        if head.ele <= pre_value:
            return False
        else:
            pre_value = head.ele
    return isBST2(head.right)



def isBST3(head):
    if head is None:
        return True
    stack = Stack()
    global prevalue
    while not stack.is_empty() or head != None:
        if head != None:
            stack.push(head)
            head = head.left
        else:
            head = stack.pop()
            if head.ele <= prevalue:
                return False
            else:
                prevalue = head.ele
            head = head.right
    return True


def isBST4(head):
    """
    套路解法
    :param head:
    """
    return process(head)

def process(head):
    if head is None:
        return None

    min_ele, max_ele = head.ele, head.ele
    is_bst = True

    leftData = process(head.left)
    rightData = process(head.right)

    if leftData != None:
        min_ele = min(leftData[0], min_ele)
        max_ele = max(leftData[1], max_ele)
    if rightData != None:
        min_ele = min(min_ele, rightData[0])
        max_ele = max(max_ele, rightData[1])

    if leftData != None and (( not leftData[2]) or (leftData[1] >= head.ele)):
        is_bst = False

    if rightData != None and ((not rightData[2]) or (rightData[0] <= head.ele)):
        is_bst = False

    return min_ele, max_ele, is_bst











if __name__ == '__main__':
    head = Node(5)
    head.left = Node(3)
    head.right = Node(10)
    head.right.left = Node(6)
    head.left.left = Node(2)
    head.left.right = Node(4)
    # print(isBST1(head))
    print(isBST2(head))
    print(isBST3(head))
    print(isBST4(head))


