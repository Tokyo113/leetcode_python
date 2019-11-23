#coding:utf-8
'''
@Time: 2019/11/20 22:42
@author: Tokyo
@file: code_04_islands.py
@desc:
'''


def islands(arr):

    N = len(arr)
    M = len(arr[0])
    res = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                res += 1

                infect(arr, i, j, N, M)
    return res




def infect(arr, i, j,N, M):
    if i == N or j == M or j < 0 or i< 0 or arr[i][j] != 1:
        return
    arr[i][j] = 2
    infect(arr, i-1, j, N,M)
    infect(arr, i+1, j, N, M)
    infect(arr, i, j+1, N, M)
    infect(arr, i, j-1, N, M)


if __name__ == '__main__':
    m1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(islands(m1))
