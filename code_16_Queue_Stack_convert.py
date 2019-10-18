#coding:utf-8
'''
@Time: 2019/10/18 21:03
@author: Tokyo
@file: code_16_Queue_Stack_convert.py
@desc:
1.如何仅用队列结构实现栈结构----两个队列实现一个栈
2.如何仅用栈结构实现队列结构----两个栈实现一个队列
'''


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


class Stack(object):

    def __init__(self):
        self.__stack = []

    def push(self, num):
        """
        入栈
        :param num:
        """
        self.__stack.append(num)

    def pop(self):
        """
        出栈
        """
        return self.__stack.pop()
    def peek(self):
        if self.__stack == []:
            raise Exception("the stack is empty")
        return self.__stack[-1]
    def is_empty(self):
        return self.__stack == []
    def size(self):
        return len(self.__stack)


class twoQueue_Stack(object):
    def __init__(self):
        self.__data_queue = Queue()
        self.__helper = Queue()

    def push(self, num):
        self.__data_queue.push(num)

    def pop(self):
        """
        把data_queue中的元素pop到helper中，直至最后一个元素作为栈顶弹出
        data_queue和helper引用互换
        """
        if self.__data_queue.is_empty():
            raise Exception("the stack is empty")
        while(self.__data_queue.size()>1):
            ele = self.__data_queue.poll()
            self.__helper.push(ele)
        # 引用互换，互换后helper中的才是栈顶元素
        self.__data_queue, self.__helper = self.__helper, self.__data_queue
        return self.__helper.poll()

    def peek(self):
        if self.__data_queue.is_empty():
            raise Exception("the stack is empty")
        while(self.__data_queue.size() > 1):
            self.__helper.push(self.__data_queue.poll())
        res = self.__data_queue.poll()
        self.__helper.push(res)
        self.__data_queue, self.__helper = self.__helper, self.__data_queue
        return res

    def is_empty(self):
        return self.__data_queue.is_empty()

    def size(self):
        return self.__data_queue.size()

class twoStack_Queue(object):
    def __init__(self):
        self.__push_stack = Stack()
        self.__pop_stack = Stack()

    def push(self, num):
        self.__push_stack.push(num)
    def pop(self):
        """
        相当于把push_stack倒入pop_stack中，pop栈顶即是队列头部元素，
        下一次倒入需要等pop为空，新加入的元素都在push_stack中
        """
        if (self.__push_stack.is_empty() and self.__pop_stack.is_empty()):
            raise Exception("the queue is empty")
        elif self.__pop_stack.is_empty():
            while not self.__push_stack.is_empty():
                self.__pop_stack.push(self.__push_stack.pop())
        return self.__pop_stack.pop()
    def peek(self):
        if (self.__push_stack.is_empty() and self.__pop_stack.is_empty()):
            raise Exception("the queue is empty")
        elif self.__pop_stack.is_empty():
            while not self.__push_stack.is_empty():
                self.__pop_stack.push(self.__push_stack.pop())
        return self.__pop_stack.peek()







if __name__ == '__main__':
    # a = twoQueue_Stack()
    # a.push(1)
    # a.push(2)
    # a.push(4)
    # a.push(5)
    # print(a.peek())
    # a.pop()
    # print(a.peek())
    b = twoStack_Queue()
    b.push(2)
    b.push(4)
    b.push(3)
    b.push(9)
    b.pop()
    b.pop()
    print(b.peek())

