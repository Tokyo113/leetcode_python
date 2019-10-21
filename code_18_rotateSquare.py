#coding:utf-8
'''
@Time: 2019/10/20 20:29
@author: Tokyo
@file: code_18_rotateSquare.py
@desc:
'''

def rotateSquare(arr):
    """
    左上角（tr, tc） 右下角(dr,dc)
    :param arr: 
    """
    tr, tc = 0, 0
    dr, dc = len(arr)-1, len(arr[0])-1
    while(tr < dr):
        rotate90(arr, tr, tc, dr, dc)
        tr += 1
        tc += 1
        dr -= 1
        dc -= 1

def rotate90(arr, tr, tc, dr, dc):

    for i in range(0, dc-tc):
        tmp = arr[tr][tc+i]
        arr[tr][tc+i] = arr[dr-i][tc]
        arr[dr-i][tc] = arr[dr][dc-i]
        arr[dr][dc-i] = arr[tr+i][dc]
        arr[tr+i][dc] = tmp

def printMatrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end="\t")
        print("")


if __name__ == '__main__':
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13,14,15,16]]

    printMatrix(a)
    print("=================")
    rotateSquare(a)
    printMatrix(a)

    b = [[1, 2], [3,4]]
    rotateSquare(b)
    printMatrix(b)


