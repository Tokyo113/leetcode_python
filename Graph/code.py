#coding:utf-8
'''
@Time: 2019/12/9 15:13
@author: Tokyo
@file: code.py
@desc:
'''


class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None



def convert(arr):
    if arr is None or arr == []:
        return None
    return process(arr)


def process(arr):
    if arr == []:
        return None
    if len(arr) == 1:
        return Node(arr[0])


    mid = len(arr)>>1
    head = Node(arr[mid])
    head.left = process(arr[:mid])
    head.right = process(arr[mid+1:])

    return head

def travel(head):
    if head is None:
        return

    travel(head.left)
    print(head.val, end=" ")
    travel(head.right)



class Node2(object):
    def __init__(self):
        self.nexts = {}
        self.feature = None


def ugly(s):
    if s is None or s == '' or len(s) == 1:
        return 0
    pre = s[0]
    cnt = 0

    return cnt


def countNum(n, k):
    bound = k * n - ((k + 1) * k) // 2
    cnt = 0
    print(bound)

    for i in range(1, bound // n+1):

        cnt += process1(n - 1, k, i * n)
        print(cnt)
    return cnt


def process1(end, k, aim):
    '''
    从0到end整数，选k个数组成aim的方法数
    '''
    if aim < 0:
        return 0
    if aim == 0:
        if k == 0 or k == 1:
            return 1
        else:
            return 0

    if end == 0:
        return 1 if aim == 0 and k == 1 else 0
    return process1(end - 1, k - 1, aim - end) + process1(end - 1, k, aim)

def minIncrementForUnique(A):
    if A is None or A == []:
        return 0
    A.sort()

    res = 0
    for i in range(1, len(A)):
        if A[i] == A[i - 1]:
            A[i] += 1
            res += 1
        elif A[i] < A[i - 1]:
            res += A[i - 1] - A[i] + 1
            A[i] += A[i - 1] - A[i] + 1

    print(A)
    return res



if __name__ == '__main__':
    # print(ugly('ABABA'))

    # print(countNum(7,2))
    print(minIncrementForUnique([3,2,1,2,1,7]))

