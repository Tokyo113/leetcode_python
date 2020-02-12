#coding:utf-8
'''
@Time: 2019/11/5 15:34
@author: Tokyo
@file: code_11_paperfolding.py
@desc:
'''

class Node(object):
    def __init__(self, num):
        self.ele = num
        self.right = None
        self.left = None


def paperfolding(N):

    printProcess(1, N, True)

def printProcess(i, N, ao):
    if i > N:
        return
    printProcess(i+1, N, True)
    print("凹" if ao is True else "凸", end=" ")
    printProcess(i+1, N, False)


def zhezhi(n):
    return process(1,n,True)
def process(i, n, ou):
    if i > n:
        return
    process(i+1, n, True)
    print('凹' if ou else '凸', end=' ')
    process(i+1, n, False)






if __name__ == '__main__':
    paperfolding(3)
    print("")
    paperfolding(1)
    print("")
    paperfolding(2)
    print('')
    print(zhezhi(5))

