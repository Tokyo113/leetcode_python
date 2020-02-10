#coding:utf-8
'''
@Time: 2020/2/10 10:59
@author: Tokyo
@file: code_01_findNuminArray.py
@desc:
给定一个元素为非负整数的二维数组matrix，每行和每列都是从小到大有序的。
再给定一个非负整数aim，请判断aim是否在matrix中
'''

def findNum(arr, num):
    '''
    从右上角或者左下角开始找都可以，比遍历简单
    O(N+M)，遍历的话是O(MN)
    :param arr:
    :return:
    '''
    if arr is None or arr == []:
        return False
    n = len(arr)
    m = len(arr[0])
    i, j = 0, m-1
    while i < n and j >= 0:
        if num < arr[i][j]:
            j -= 1
        elif num > arr[i][j]:
            i += 1
        else:
            return True
    return False


if __name__ == '__main__':
    arr = [[0, 1, 2, 3, 4, 5, 6],
    [10, 12, 13, 15, 16, 17, 18],
    [23, 24, 25, 26, 27, 28, 29],
    [44, 45, 46, 47, 48, 49, 50],
    [65, 66, 67, 68, 69, 70, 71],
    [96, 97, 98, 99, 100, 111, 122],
    [166, 176, 186, 187, 190, 195, 200],
    [233, 243, 321, 341, 356, 370, 380]]
    print(findNum(arr, -233))