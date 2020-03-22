#coding:utf-8
'''
@Time: 2020/3/15 9:13
@author: Tokyo
@file: code_07_islandsII.py
@desc:
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def maxAreaOfIsland(grid):
    if grid is None or grid == []:
        return 0
    area = 0
    N = len(grid)
    M = len(grid[0])
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                area = max(infect(grid, N, M, i, j), area)
    return area


def infect(arr, N, M, i, j):
    if i < 0 or j < 0 or i == N or j == M or arr[i][j] != 1:
        return 0
    res = 1
    arr[i][j] = 2
    res += infect(arr, N, M, i + 1, j)
    res += infect(arr, N, M, i - 1, j)
    res += infect(arr, N, M, i, j - 1)
    res += infect(arr, N, M, i, j + 1)
    return res
