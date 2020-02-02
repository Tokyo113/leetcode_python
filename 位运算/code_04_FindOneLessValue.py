#coding:utf-8
'''
@Time: 2019/12/4 22:56
@author: Tokyo
@file: code_04_FindOneLessValue.py
@desc:
找数组的局部最小值
给定一个无序的数组arr，任意两个相邻的数一定不相等
如下定义局部最小值：
若arr[i]<arr[i+1]且arr[i]<arr[i-1]，则i位置为局部最小值
头和尾只需要比较一个数即可
要求时间复杂度低于O(N)
'''


def findLessValue(arr):
    if arr is None or len(arr) <= 1:
        return -1

    if arr[0]< arr[1]:
        return 0

    if arr[-1]< arr[-2]:
        return len(arr)-1

    L = 1
    R = len(arr)-2

    while L < R:
        mid = L + ((R-L) >> 1)
        if arr[mid] < arr[mid+1] and arr[mid] < arr[mid-1]:
            return mid
        elif arr[mid] > arr[mid-1]:
            R = mid-1
        else:
            L = mid+1

    return L


def findsmall(arr):
    if arr is None or len(arr) <= 1 :
        return

    if arr[0] < arr[1]:
        return 0
    elif arr[-1] < arr[-2]:
        return len(arr)-1
    else:
        L, R = 1, len(arr)-2
        while L < R:
            mid = L + ((R-L) >> 1)
            if arr[mid] < arr[mid+1] and arr[mid] < arr[mid-1]:
                return mid
            elif arr[mid] > arr[mid-1]:
                R = mid - 1
            elif arr[mid] > arr[mid+1]:
                L = mid + 1
        # 最终必然存在局部极小值，返回L=R时的情况
        return R



if __name__ == '__main__':
    a = [1]
    findsmall(a)
    # print(a[findLessValue(a)])
    # print(a[findsmall(a)])
    b = [6, 5, 3, 9, 1, 7, 8 ]
    print(b[findLessValue(b)])
    print(b[findsmall(b)])

