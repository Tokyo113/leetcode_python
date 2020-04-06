#coding:utf-8
'''
@Time: 2020/4/1 13:29
@author: Tokyo
@file: code_05_龙与地下城游戏.py
@desc:
给定一个二维数组map，含义是一张地图，例如，如下矩阵
-2，-3， 3
-5，-10，1
0， 30， -5
​

游戏的规则如下:
      1）骑士从左上角出发，每次只能向右或向下走，最后到达右下角见到公主。
      2）地图中每个位置的值代表骑士要遭遇的事情。如果是负数，说明此处有怪兽，要让骑士损失血量。如果是非负数，代表此处有血瓶，能让骑士回血。
      3）骑士从左上角到右下角的过程中，走到任何一个位置时，血量都不能少于1。为了保证骑土能见到公主，初始血量至少是多少?
根据map,输出初始血量。
'''


def dragon(arr):
    if arr is None or arr == []:
        return
    n,m = len(arr), len(arr[0])
    return process(arr,0,0)

def process(arr,i,j):
    '''
    返回安全通过i，j位置到达最后需要的最少血量
    状态转移：
    普遍位置a,b，
    当前需要的最少血量要看当前arr的值以及后面到达最后需要的血量
    :param arr:
    :param i:
    :param j:
    :return:
    '''
    if i == len(arr)-1 and j == len(arr[0])-1:
        return 1 if arr[i][j] >= 0 else 1-arr[i][j]
    if i == len(arr)-1:
        # max是总结了三种情况，
        # arr[i][j]>0且小于process（arr,i,j+1）
        # arr[i][j]>0且大于process（arr,i,j+1）
        # arr[i][j]<0
        return max(1,process(arr,i,j+1)-arr[i][j])

    if j == len(arr[0])-1:
        return max(1, process(arr, i+1, j) - arr[i][j])
    p1 = max(1,process(arr,i,j+1)-arr[i][j])
    p2 = max(1,process(arr,i+1,j)-arr[i][j])
    return min(p1,p2)

def dragonDP(arr):
    if arr is None or arr == []:
        return 0
    n,m = len(arr), len(arr[0])
    dp = [0 for i in range(m)]
    dp[m-1] = 1 if arr[n-1][m-1] >=0 else 1-arr[n-1][m-1]
    for j in range(m-2,-1,-1):
        dp[j] = max(1,dp[j+1]-arr[n-1][j])

    for i in range(n-2,-1,-1):
        for j in range(m-1,-1,-1):
            if j == m-1:
                dp[j] = max(1,dp[j]-arr[i][j])
            else:
                p1 = max(1,dp[j]-arr[i][j])
                p2 = max(1,dp[j+1]-arr[i][j])
                dp[j] = min(p1,p2)
    return dp[0]





if __name__ == '__main__':
    arr = [[-2,-3,3],[-5,-10,1],[0,30,-5]]
    print(dragon(arr))
    print(dragonDP(arr))