#coding:utf-8
'''
@Time: 2019/10/20 21:25
@author: Tokyo
@file: code_19_zigzagMatrix.py
@desc: print Matrix as a zigzag style
'''

def zigzagMat(arr):
    """
    A (ar, ac)   B (br, bc)
    :param arr:
    """
    ar, ac = 0, 0
    br, bc = 0, 0
    endr, endc = len(arr)-1, len(arr[0])-1
    # 是否是从上往下打印
    direction = False
    while (ar != endr+1):
        printLevel(arr, ar, ac, br, bc, direction)
        # 注意这几句的顺序，ac到了endc时的第一次ar是不动的，下一次才加一
        ar = ar + 1 if ac == endc else ar
        ac = ac if ac == endc else ac+1
        bc = bc + 1 if br == endr else bc
        br = br if br == endr else br+1

        direction = ~direction


def printLevel(arr, a_r, a_c, b_r, b_c, direc):
    if direc:
        while a_r <= b_r:
            print(arr[a_r][a_c], end=" ")
            a_r += 1
            a_c -= 1
    else:
        while b_r >= a_r:
            print(arr[b_r][b_c], end=" ")
            b_r -= 1
            b_c += 1


if __name__ == '__main__':
    a = [[1, 2, 3,4],[5,6,7,8], [9,10,11,12]]
    zigzagMat(a)

