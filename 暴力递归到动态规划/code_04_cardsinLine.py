#coding:utf-8
'''
@Time: 2019/11/17 10:18
@author: Tokyo
@file: code_04_cardsinLine.py
@desc:
给定一个整型数组arr，代表数值不同的纸牌排成一条线。玩家A和玩家B依次拿走每张纸
牌，规定玩家A先拿，玩家B后拿，但是每个玩家每次只能拿走最左或最右的纸牌，玩家A
和玩家B都绝顶聪明。请返回最后获胜者的分数。

'''


def win1(arr):
    if len(arr) == 0 or arr is None:
        return 0

    return max(f(arr, 0, len(arr)-1), s(arr, 0, len(arr)-1))


def f(arr, L, R):
    if L == R:
        return arr[L]

    return max(arr[L] + s(arr, L+1, R), arr[R] + s(arr, L, R-1))

def s(arr, L, R):
    if L == R:
        return 0

    return min(f(arr, L+1, R),  f(arr, L, R-1))



def winner(arr):
    return max(f1(arr, 0, len(arr)-1), g1(arr, 0, len(arr)-1))

def f1(arr, L, R):
    if L == R:
        return arr[L]

    return max(arr[L] + g1(arr, L+1, R), arr[R]+g1(arr, L, R-1))


def g1(arr, L, R):
    if L == R:
        return 0
    return min(f1(arr, L+1, R), f1(arr, L, R-1))





if __name__ == '__main__':
    a = [1,100,45,67,8,34,21,2,9]
    b = [1,9,1]
    print(win1(a))
    print(winner(b))


