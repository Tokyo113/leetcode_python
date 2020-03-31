#coding:utf-8
'''
@Time: 2020/3/29 10:33
@author: Tokyo
@file: code_10_MapIslandAndSea.py
@desc:
你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。

我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。

如果我们的地图上只有陆地或者海洋，请返回 -1。

 

示例 1：



输入：[[1,0,1],[0,0,0],[1,0,1]]
输出：2
解释：
海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。
示例 2：



输入：[[1,0,0],[0,0,0],[0,0,0]]
输出：4
解释：
海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。
 


'''

def islandAndSea(arr):
    if arr is None or arr ==[]:
        return -1
    n, m = len(arr), len(arr[0])
    dist = [[float('inf') for i in range(m)] for i in range(n)]
    queue = []
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                dist[i][j] = 0
                arr[i][j] = -2
                cnt += 1
                queue.append([i, j])
    if cnt == m*n or cnt == 0:
        return -1
    ans = 0
    while queue != []:
        x,y = queue.pop(0)
        for i,j in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
            if 0<=i<n and 0<=j<m and arr[i][j] != -2:
                dist[i][j] = min(dist[i][j], dist[x][y]+1)
                ans = max(ans,dist[i][j])
                arr[i][j] = -2
                queue.append([i,j])
    return ans


if __name__ == '__main__':
    arr = [[1,0,0],[0,0,0],[0,0,0]]
    print(islandAndSea(arr))





