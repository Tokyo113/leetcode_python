#coding:utf-8
'''
@Time: 2019/10/31 19:15
@author: Tokyo
@file: code_05_isCBT.py
@desc: complete binary tree
判断一棵二叉树是否是完全二叉树
'''


class Node(object):
    def __init__(self, num):
        self.right = None
        self.left = None
        self.ele = num


class Queue(object):
    def __init__(self):
        self.__queue = []

    def push(self, num):
        self.__queue.append(num)

    def poll(self):
        if self.__queue == []:
            raise Exception("the queue is empty")
        return self.__queue.pop(0)

    def is_empty(self):
        return self.__queue == []

    def peek(self):
        """
        返回队列头的元素
        :return:
        """
        if self.__queue == []:
            raise Exception("the queue is empty")
        return self.__queue[0]

    def size(self):
        return len(self.__queue)

def isCBT(head):
    if head is None:
        return True

    queue = Queue()
    queue.push(head)
    leaf = False
    while not queue.is_empty():
        head = queue.poll()
        l = head.left
        r = head.right

        if (l is None and r != None) or (leaf and (l != None or r != None)):
            return False

        if l != None:
            queue.push(l)

        if r != None:
            queue.push(r)

        if l is None or r is None:
            leaf = True
    return True



def cbt(head):
    if head is None:
        return True
    queue = []
    queue.append(head)
    isleaf = False
    while queue != []:
        node = queue.pop(0)
        l = node.left
        r = node.right

        if (r != None and l == None) or (isleaf and (l!= None or r != None)):
            return False

        if node.left == None or node.right == None:
            isleaf = True


        if l != None:
            queue.append(l)
        if r != None:
            queue.append(r)

    return True

if __name__ == '__main__':
    head = Node(5)
    head.left = Node(3)
    head.right = Node(10)
    head.right.left = Node(7)
    head.left.left = Node(2)
    head.left.right = Node(4)
    head1 = None
    print(isCBT(head))

    print(cbt(head))