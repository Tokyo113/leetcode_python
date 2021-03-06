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
    '''
    先序遍历序列的反序列化，使用队列
    每次从头部弹出
    :param preStr:
    :return:
    '''
    strs = preStr.split("!")
    return reconByPreOrder(strs)


def reconByPreOrder(strs):
    value = strs.pop(0)
    if value == "#":
        return None
    head = Node(int(value))
    head.left = reconByPreOrder(strs)
    head.right = reconByPreOrder(strs)
    return head




def serializeByLevel(head):
    if head is None:
        return '#_'
    queue = []
    queue.append(head)
    res = ''
    while queue != []:
        pp = queue.pop(0)
        if pp == '#_':
            res += pp
        else:
            res += str(pp.ele)+'_'

            if pp.left != None:
                queue.append(pp.left)
            else:
                queue.append('#_')
            if pp.right != None:
                queue.append(pp.right)
            else:
                queue.append('#_')
    return res


def reconstructByLevel(strs):
    '''
    按层遍历反序列化
    :param strs:
    :return:
    '''
    strs = strs.split('_')

    queue = []
    head = getNode(strs)
    queue.append(head)

    while queue != []:
        node = queue.pop(0)

        node.left = getNode(strs)
        node.right = getNode(strs)
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    return head


def getNode(strs):
    pp = strs.pop(0)
    if pp == '#':
        return None
    return Node(int(pp))

def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    if root is None:
        return '#!'
    res = ''
    queue = []
    queue.append(root)
    while queue:
        pp = queue.pop()
        if pp == '#!':
            res += pp
        else:
            res += str(pp.ele) + '!'

            if pp.left is None:
                queue.append('#!')
            else:
                queue.append(pp.left)
            if pp.right is None:
                queue.append('#!')
            else:
                queue.append(pp.right)
    return res

def deserialize( data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    if data == '':
        return
    queue = []
    strs = data.split('!')
    head = Node(strs.pop(0))
    queue.append(head)
    while queue:
        pp = queue.pop(0)
        left = strs.pop(0)
        right = strs.pop(0)
        if left == '#':
            pp.left = None
        else:
            pp.left = Node(int(left))
            queue.append(pp.left)
        if right == '#':
            pp.right = None
        else:
            pp.right = Node(int(right))
            queue.append(pp.right)
    return head


if __name__ == '__main__':
    head1 = None

    str1 = serialByPre(head1)
    print("pre_order:")
    print(str1)
    print(reconByPreString(str1))
    print("level_order:")





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

    print('按层遍历：')
    print(serializeByLevel(head))
    aa = serializeByLevel(head)
    # head_level = reconstructByLevel(aa)
    # print(serializeByLevel(head_level))
    print(serialize(head))

    print('='*40)
    a = [41, 37, 44, 24, 39, 42, 48, 1, 35, 38, 40 , 43, 46, 49, 0, 2, 30, 36,  45,
     47, 4, 29, 32 , 3, 9, 26,  31, 34,7, 11, 25, 27,  33, 6, 8, 10, 16, 28, 5,
     15, 19,    12, 18, 20,  13, 17,  22, 14, 21, 23]
    print(len(a),len(set(a)))

















