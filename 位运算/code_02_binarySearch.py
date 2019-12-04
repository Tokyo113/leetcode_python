#coding:utf-8
'''
@Time: 2019/12/4 22:23
@author: Tokyo
@file: code_02_binarySearch.py
@desc:
'''


def binarySearch(arr, num):
    if arr is None or len(arr) == 0:
        return False

    L, R = 0, len(arr)-1
    while L < R:
        mid = L + ((R-L)>> 1)
        if arr[mid] == num:
            return True
        elif arr[mid] < num:
            L = mid + 1
        else:
            R = mid - 1
    return arr[L] == num



if __name__ == '__main__':
    a = [1]
    print(binarySearch(a, 0))