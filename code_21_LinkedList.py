#coding:utf-8
'''
@Time: 2019/10/21 19:14
@author: Tokyo
@file: code_21_LinkedList.py
@desc:
'''

class Node(object):
    def __init__(self, ele):
        self.ele = ele
        self.next = None


class Linkedlist(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):

        cur = self.__head
        count = 0
        while(cur != None):
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while (cur != None):
            print(cur.ele, end=" ")
            cur = cur.next
        print("")

    def add(self, num):
        node = Node(num)
        node.next = self.__head
        self.__head = node

    def append(self, num):
        node = Node(num)
        if self.__head is None:
            self.__head = node
        cur = self.__head
        while (cur.next != None):
            cur  = cur.next
        cur.next = node

    def insert(self, index, num):
        node = Node(num)
        if index <= 0:
            self.add(num)
        elif index > self.length()-1:
            self.append(num)
        else:
            count = 0
            cur = self.__head
            while(count < index-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node


    def remove(self, num):
        """
        删除所有num节点
        :param num:
        """
        cur = self.__head
        pre = None
        while (cur != None):
            if (cur.ele == num):
                if(cur == self.__head):
                    self.__head = cur.next
                else:
                    pre.next = cur.next
            pre = cur
            cur = cur.next



            pre = cur
            cur = cur.next


    def search(self, num):
        cur = self.__head
        while(cur != None):
            if cur.ele == num:
                return True
            else:
                cur = cur.next
        return False








if __name__ == '__main__':
    a = Linkedlist()
    print(a.is_empty())
    a.add(1)
    a.add(2)
    a.add(3)
    a.add(4)
    a.add(3)
    a.append(6)
    a.travel()
    a.remove(3)
    a.travel()
    print(a.search(4))