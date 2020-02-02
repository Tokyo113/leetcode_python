#coding:utf-8
'''
@Time: 2019/11/26 11:13
@author: Tokyo
@file: code_01_SlidingWindow.py
@desc:
进阶：窗口的左右边界可以自由动，但保证L<R
'''

from collections import deque
def getMaxWindow(arr, w):
    if arr == None or w < 1 or len(arr) < w:
        return None

    qmax = deque()
    res = []
    for i in range(len(arr)):
        while len(qmax) != 0 and arr[qmax[-1]] <= arr[i]:
            qmax.pop()

        qmax.append(i)

        if qmax[0] == i-w:
            # 要过期的下标是双端队列的头部
            qmax.popleft()

        if i >= w-1:
            # 此时开始结算，加入res中
            res.append(arr[qmax[0]])

    return res


def getMinWindow(arr, w):
    '''
    维持窗口最小值
    :param arr:
    :param w:
    :return:
    '''
    if arr is None or len(arr) < w or w < 1:
        return

    qmin = deque()
    res = []
    for i in range(len(arr)):
        while len(qmin) > 0 and arr[qmin[-1]] >= arr[i]:
            qmin.pop()
        qmin.append(i)

        if i-w == qmin[0]:
            qmin.popleft()

        if i-w >= -1:
            res.append(arr[qmin[0]])

    return res


if __name__ == '__main__':
    arr = [4,3,5,4,3,3,6,7,2,1]
    w = 3
    print(getMaxWindow(arr, w))
    print(getMinWindow(arr, w))




