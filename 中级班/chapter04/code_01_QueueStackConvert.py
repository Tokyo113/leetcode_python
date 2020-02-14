#coding:utf-8
'''
@Time: 2020/2/14 16:53
@author: Tokyo
@file: code_01_QueueStackConvert.py
@desc:
如何仅用队列结构实现栈结构?
如何仅用栈结构实现队列结构


面试套路：
图的深度优先遍历只能用队列完成，但面试官让你用栈实现图的深度优先遍历，
不要懵逼，先用两个栈实现队列，然后用队列做即可
'''

class twoStackQueue(object):
    '''
    两个栈实现队列
    '''
    def __init__(self):
        self.data = []
        self.helper = []

    def push(self, num):
        self.data.append(num)
        if self.helper == []:
            while self.data != []:
                self.helper.append(self.data.pop())

    def pop(self):
        if self.data == [] and self.helper == []:
            print('the queue is empty!')
            return
        res = self.helper.pop()
        if self.helper == []:
            while self.data != []:
                self.helper.append(self.data.pop())
        return res

    def peek(self):
        return self.helper[-1]



class twoQueueStack(object):
    '''
    两个队列实现栈
    '''
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, num):
        self.queue1.append(num)

    def pop(self):
        if self.queue1 == []:
            return
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        res = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return res



    def peek(self):
        if self.queue1 == []:
            return
        return self.queue1[-1]


if __name__ == '__main__':
    # a = twoStackQueue()
    a = twoQueueStack()
    a.push(1)
    a.push(3)
    a.push(5)
    a.push(6)
    a.push(7)
    print(a.pop())
    print(a.pop())
    print(a.peek())
