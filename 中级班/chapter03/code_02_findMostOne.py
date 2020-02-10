#coding:utf-8
'''
@Time: 2020/2/10 11:27
@author: Tokyo
@file: code_02_findMostOne.py
@desc:
给定一个二维数据arr，每一行由0和1组成，
但每一行0都在1的左边，也可以全为0或全为1，
请找到1数量最多的行，数量相同则可以返回多行
'''

def findMostOne(arr):
    if arr is None or arr == []:
        return []
    i, j = 0, len(arr[0])-1

    ans = 0
    maxNum = 0
    while i <len(arr) and j > -1:
        while j >= 0 and arr[i][j] == 1:
            j -= 1
            ans += 1
        maxNum = max(maxNum, ans)
        i += 1
    return maxNum

if __name__ == '__main__':
    arr = [[0,1,1,1,1],
           [0,0,0,0,0],
           [1,1,1,1,1],
           [0,0,0,1,1]]
    print(findMostOne(arr))
