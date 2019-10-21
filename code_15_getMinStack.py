#coding:utf-8
'''
@Time: 2019/10/18 20:00
@author: Tokyo
@file: code_15_getMinStack.py
@desc:实现一个特殊的栈，在实现栈的基本功能的基础上，
再实现返回栈中最小元素的操作
要求：
1.pop, push, getMin操作的时间复杂度都是O(1)
2.设计的栈类型可以使用现成的栈结构
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


class MinStack(object):
    def __init__(self):
        self.__stack = Stack()
        self.__minstack = Stack()

    def push(self, num):
        """
        入栈
        dataStack 和minStack一起入栈，num和minStack栈顶元素比较，
        小于栈顶则入栈num,否则入栈原栈顶元素
        :param num:
        """
        self.__stack.push(num)
        if self.__minstack.is_empty():
            self.__minstack.push(num)
        elif num < self.__minstack.peek():
            self.__minstack.push(num)
        else:
            self.__minstack.push(self.__minstack.peek())

    def pop(self):
        if self.__stack.is_empty():
            raise Exception("the stack is empty")
        self.__stack.pop()
        self.__minstack.pop()


    def get_min(self):
        if self.__stack.is_empty():
            raise Exception("the stack is empty")
        return self.__minstack.peek()


class get_minStack(object):
    def __init__(self):
        self.__data_stack = Stack()
        self.__min_stack = Stack()

    def push(self, num):
        self.__data_stack.push(num)
        if self.__min_stack.is_empty():
            self.__min_stack.push(num)
        if self.__min_stack.peek() <= num:
            self.__min_stack.push(self.__min_stack.peek())
        else:
            self.__min_stack.push(num)

    def pop(self):
        if self.__data_stack.is_empty():
            raise Exception("the stack is empty")
        self.__data_stack.pop()
        self.__min_stack.pop()

    def peek(self):
        return self.__data_stack.peek()


    def get_min(self):
        return self.__min_stack.peek()


if __name__ == '__main__':
    a = get_minStack()
    a.push(-1)
    a.push(4)
    a.push(6)
    a.push(-7)
    a.push(3)
    print(a.peek())
    print(a.get_min())


