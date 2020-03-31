#coding:utf-8
'''
@Time: 2020/3/29 18:50
@author: Tokyo
@file: code.py
@desc:
'''


def card(arr,m,brr):

    for i in range(len(arr)):
        arr[i] = [arr[i],brr[i]]

    arr.sort(key=lambda i:i[1])
    print(arr)

    res = 0
    for i in range(m):
        res += arr[-1][0]
        arr.pop()
        for i in range(len(arr)):
            arr[i] = [arr[i][0]-arr[i][1],arr[i][1]]
    return res


def baoli(arr,m,brr):
    for i in range(len(arr)):
        arr[i] = [arr[i],brr[i]]



# n = int(input())
# m = int(input())
# arr = [int(i) for i in input().split(' ')]
# brr = [int(i) for i in input().split(' ')]
# print(card(arr,m,brr))

if __name__ == '__main__':
    print(card([10,20,30,40,50],5,[4,5,6,20,8]))


