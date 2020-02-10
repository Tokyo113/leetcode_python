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
    '''
    宽度优先遍历，用队列
    :param head:
    :return:
    '''
    if head is None:
        return
    res = []
    queue = []
    queue.append(head)
    while queue != []:
        ele = queue.pop(0)
        res.append(ele.ele)
        if ele.left != None:
            queue.append(ele.left)
        if ele.right != None:
            queue.append(ele.right)
    return res



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

def getMaxWid(head):
    '''
    使用哈希表记录层数
    :param head:
    :return:
    '''
    if head is None:
        return 0
    queue = []
    levelMap = {}
    queue.append(head)
    levelMap[head] = 1
    cur_level = 1
    cur_num = 0
    max_num = 0
    while queue != []:
        node = queue.pop(0)
        if levelMap.get(node) == cur_level:
            cur_num += 1
            max_num = max(max_num, cur_num)
        else:
            cur_level += 1
            # 一层结束，结算，cur_num重置
            max_num = max(max_num, cur_num)
            cur_num = 1

        if node.left != None:
            levelMap[node.left] = levelMap.get(node)+1
            queue.append(node.left)
        if node.right != None:
            levelMap[node.right] = levelMap.get(node)+1
            queue.append(node.right)
    return max_num

def getMaxWid2(head):
    if head is None:
        return 0
    queue = []
    queue.append(head)
    cur_num = 1
    max_num = 0
    cur_end = head
    next_end = None

    while queue != []:
        node = queue.pop(0)
        if node.left != None:
            queue.append(node.left)
            next_end = node.left
        if node.right != None:
            queue.append(node.right)
            next_end = node.right
        if node == cur_end:
            max_num = max(max_num, cur_num)
            cur_end = next_end
            cur_num = 1
        else:
            cur_num += 1
            max_num = max(max_num, cur_num)
    return max_num




if __name__ == '__main__':
    head = Node(5)
    head.left = Node(3)
    head.right = Node(8)
    # head.left.left = Node(2)
    # head.left.right = Node(4)
    # head.left.left.left = Node(1)
    # head.left.left.right = Node(3)
    # head.right.left = Node(7)
    # head.right.left.left = Node(6)
    # head.right.right = Node(10)
    # head.right.right.left = Node(9)
    # head.right.right.right = Node(11)
    print(widthTravel(head))

    print(maxWidth(head))
    print(maxWidth2(head))
    print(getMaxWid(head))
    print(getMaxWid2(head))
