#coding:utf-8
'''
@Time: 2019/12/4 22:41
@author: Tokyo
@file: code_03_BSNearLeft.py
@desc:
在一个有序数组中，找>=某个数最左侧的位置
'''

def nearestIndex(arr, num):
    if arr is None or len(arr)== 0:
        return

    L, R = 0, len(arr)-1
    index = -1
    while L <= R:
        mid = L + ((R-L) >> 1)
        if arr[mid] >= num:
            index = mid
            R = mid - 1
        else:
            L = mid + 1

    return index


if __name__ == '__main__':
    a = [1,1,1,2,2,2,3]
    print(nearestIndex(a, 1))
