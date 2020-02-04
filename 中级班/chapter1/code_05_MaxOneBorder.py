#coding:utf-8
'''
@Time: 2020/2/4 18:36
@author: Tokyo
@file: code_05_MaxOneBorder.py
@desc:
给定一个N*M的矩阵matrix，只有0和1两种值，返回边框全是1的最大正方形的边
长长度。
例如:
01111
01001
01001
01111
01011
其中边框全是1的最大正方形的大小为4*4，所以返回4

'''

def helperMatrix(m, N, M):
    right = [[0 for i in range(M)]for i in range(N)]
    down = [[0 for i in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M-1, -1, -1):
            if j == M-1:
                right[i][j] = 1 if m[i][j] == 1 else 0
            else:
                if m[i][j] == 0:
                    right[i][j] = 0
                else:
                    right[i][j] = 1 + right[i][j+1]

    for j in range(M):
        for i in range(N-1, -1, -1):
            if i == N-1:
                down[i][j] = 1 if m[i][j] == 1 else 0
            else:
                if m[i][j] == 0:
                    down[i][j] = 0
                else:
                    down[i][j] = 1+down[i+1][j]




    return right, down

def getMaxSize(m):
    N = len(m)
    M = len(m[0])
    maxSize = 0
    right, down = helperMatrix(m, N, M)
    for i in range(N):
        for j in range(M):
            for length in range(1,min(M-j, N-i)+1):
                if right[i][j] == length and down[i][j] == length and down[i][j+length-1] == length and right[i+length-1][j] == length:
                    maxSize = max(maxSize, length)


    return maxSize



if __name__ == '__main__':
    m = [[1,0,1,1,1],
         [0,0,1,0,1],
         [1,0,1,1,1]]
    r,d = helperMatrix(m, 3,5)
    print(r)
    print(d)
    print(getMaxSize(m))





