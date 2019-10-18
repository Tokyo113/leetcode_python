#coding:utf-8
'''
@Time: 2019/10/18 15:13
@author: Tokyo
@file: code_14_Arrayto_Stack_Queue.py
@desc: 使用固定长度数组实现栈和队列
'''


class Stack(object):

    def __init__(self, initsize):
        if initsize < 0:
            raise Exception("The init size is less than 0")
        self.__stack = [None for i in range(initsize)]
        self.index = 0


    def pop(self):
        """
        弹出栈顶元素
        """
        if self.index == 0:
            raise Exception("the stack is empty")
        self.index -= 1
        print(self.__stack[self.index])

    def peak(self):
        if self.index == 0:
            return
        return self.__stack[self.index-1]

    def push(self, num):
        if self.index == len(self.__stack):
            raise Exception("the stack is full")
        self.__stack[self.index] = num
        self.index += 1



class Queue(object):

    def __init__(self, initsize):
        if initsize < 0:
            raise Exception("The init size is less than 0")
        self.__queue = [None for i in range(initsize)]
        self.start = 0
        self.end = 0
        self.size = 0

    def push(self, num):
        """
        入队
        :param num:
        """
        if self.size == len(self.__queue):
            raise Exception("the queue is full")
        self.__queue[self.end] = num
        self.end = self.end + 1 if self.end < len(self.__queue)-1 else 0
        self.size += 1

    def poll(self):
        """
        出队
        """
        if self.size == 0:
            raise Exception("the queue is empty")
        print(self.__queue[self.start])
        self.start = self.start + 1 if self.start < len(self.__queue)-1 else 0
        self.size -= 1
    def peek(self):
        if self.size == 0:
            raise Exception("the queue is empty")
        return self.__queue[self.start]

if __name__ == '__main__':
    b=Queue(5)
    b.push(2)
    b.push(1)
    b.push(4)
    b.push(6)
    b.push(9)
    print(b.start)
    print(b.end)
    print(b.size)
    print(b.peek())
    print("===============")
    b.poll()
    b.poll()



