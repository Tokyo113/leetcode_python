#coding:utf-8
'''
@Time: 2020/2/25 17:35
@author: Tokyo
@file: code_05_NumNotInArr.py
@desc:
给定一个整数数组A，长度为n，有 1 <= A[i] <= n，且对于[1,n]的整数，其
中部分整数会重复出现而部分不会出现。
实现算法找到[1,n]中所有未出现在A中的整数。
提示：尝试实现O(n)的时间复杂度和O(1)的空间复杂度（返回值不计入空间复
杂度）。
'''

def findNums(arr):
    if arr is None or arr == []:
        return []
    for i in range(len(arr)):
        while arr[i] != i+1:
            tmp = arr[i]
            if arr[tmp-1] == tmp:
                break
            else:
                arr[i], arr[tmp-1] = arr[tmp-1], arr[i]

    res = []
    for i in range(len(arr)):
        if arr[i] != i+1:
            res.append(i+1)
    return res

if __name__ == '__main__':
    arr = [1,1,1,1,4]
    print(findNums(arr))