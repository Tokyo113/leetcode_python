#coding:utf-8
'''
@Time: 2019/10/30 16:22
@author: Tokyo
@file: code_03_Maxwidth.py
@desc:
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



def widthTravel(head):
    if head is None:
        return
    queue = Queue()
    queue.push(head)

    while not queue.is_empty():
        head = queue.poll()
        print(head.ele, end=" ")
        if head.left != None:
            queue.push(head.left)
        if head.right != None:
            queue.push(head.right)


def maxWidth(head):
    if head is None:
        return
    queue = Queue()
    queue.push(head)
    levelmap = {}
    cur_level = 1
    cur_Nodenum = 0
    levelmap[head] = 1
    max_level = 0
    while not queue.is_empty():
        head = queue.poll()
        node_level = levelmap.get(head)
        if cur_level == node_level:
            cur_Nodenum += 1
            max_level = max(max_level, cur_Nodenum)
        else:
            # 已经进入下一层，结算最大值
            max_level = max(max_level, cur_Nodenum)
            cur_level += 1
            cur_Nodenum = 1

        if head.left != None:
            levelmap[head.left] = node_level + 1
            queue.push(head.left)
        if head.right != None:
            levelmap[head.right] = node_level + 1
            queue.push(head.right)

    return max_level



def maxWidth2(head):
    """
    不用哈希表
    :param head:
    """
    if head is None:
        return 0
    cur_end = head
    next_end = None
    cur_node = 0
    max_num = 0
    queue = Queue()
    queue.push(head)
    while not queue.is_empty():
        head = queue.poll()

        if head.left != None:
            queue.push(head.left)
            next_end = head.left
        if head.right != None:
            queue.push(head.right)
            next_end = head.right

        if head != cur_end:
            cur_node += 1
        else:
            cur_node += 1
            max_num = max(max_num, cur_node)
            # 进入下一层
            cur_end = next_end

            cur_node = 0


    return max_num





if __name__ == '__main__':
    head = Node(5)
    head.left = Node(3)
    head.right = Node(8)
    head.left.left = Node(2)
    head.left.right = Node(4)
    head.left.left.left = Node(1)
    head.left.left.right = Node(3)
    head.right.left = Node(7)
    head.right.left.left = Node(6)
    head.right.right = Node(10)
    # head.right.right.left = Node(9)
    # head.right.right.right = Node(11)
    widthTravel(head)
    print("")
    print(maxWidth(head))
    print(maxWidth2(head))
