#coding:utf-8
'''
@Time: 2020/3/5 12:10
@author: Tokyo
@file: code_06_FindRepeatNum.py
@desc:
在一个长度为 n+1 的数组 nums 里的所有数字都在 1～n 的范围内。
数组中至少有一个数字是重复的，请找出数组中任意一个重复的数字。
但不能修改输入的数组，空间复杂度O(1)

思路：和上题一样，但是不能改数组了
二分法，时间复杂度O(NlogN)
'''

def findNum(arr):
    if arr is None or arr == [] or len(arr) == 1:
        return
    n = len(arr)-1

    L, R = 1, n
    while L <= R:
        mid = (L+R)//2
        left = countNum(arr, L, mid)
        if L == R:
            return L if left >1 else -1
        if left > mid-L+1:
            R = mid
        else:
            L = mid+1



def countNum(arr, L, R):
    if L > R:
        return -1
    cnt = 0
    for i in arr:
        if i <= R and i >= L:
            cnt += 1
    return cnt


if __name__ == '__main__':
    arr = [2,3,5,4,3,2,6,7]
    print(findNum(arr))


