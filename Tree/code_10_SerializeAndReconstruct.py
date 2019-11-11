#coding:utf-8
'''
@Time: 2019/11/5 14:03
@author: Tokyo
@file: code_10_SerializeAndReconstruct.py
@desc:
二叉树的序列化和反序列化
就是内存里的一棵树如何变成字符串形式，又如何从字符串形式变成内存里的树
'''


class Node(object):
    def __init__(self, num):
        self.ele = num
        self.right = None
        self.left = None
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


def serialByPre(head):
    """
    先序遍历实现序列化
    :param head:
    """
    if head is None:
        return "#!"

    res = str(head.ele) + "!"
    res += serialByPre(head.left)
    res += serialByPre(head.right)
    return res


def reconByPreString(preStr):
    values = preStr.split("!")
    queue = Queue()
    for i in range(len(values)):
        queue.push(values[i])

    return reconByPreOrder(queue)


def reconByPreOrder(queue):
    value = queue.poll()
    if value == "#":
        return None
    head = Node(int(value))
    head.left = reconByPreOrder(queue)
    head.right = reconByPreOrder(queue)
    return head

def serial_in(head):
    if head is None:
        return "#_"

    res = serial_in(head.left)
    res += str(head.ele) + "_"
    res += serial_in(head.right)

    return res







if __name__ == '__main__':
    head1 = None
    str1 = serialByPre(head1)
    print("pre_order:")
    print(str1)
    print(reconByPreString(str1))
    print("in_order:")
    print(serial_in(head1))



    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.right.right = Node(5)
    str2 = serialByPre(head)
    print("pre_order:")
    print(str2)
    head_re = reconByPreString(str2)
    print(serialByPre(head_re))
    print("in_order:")
    str22 = serial_in(head)
    print(str22)












