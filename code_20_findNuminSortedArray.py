#coding:utf-8
'''
@Time: 2019/10/21 11:49
@author: Tokyo
@file: code_20_findNuminSortedArray.py
@desc:
给定一个有N*M的整型矩阵matrix和一个整数K，
矩阵的每一行和每一列都是排好序的，
实现一个函数，判断K是否在矩阵中，返回True or False
要求：
时间复杂度O(M+N), 额外空间复杂度O(1)
'''

def findNumIn_sortedArray(arr, k):
    row = 0
    col = len(arr[0])-1
    while (row < len(arr) and col >= 0):
        if k > arr[row][col]:
            row += 1
        elif k < arr[row][col]:
            col -= 1
        else:
            return True
    return False

if __name__ == '__main__':
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(findNumIn_sortedArray(a, 7))