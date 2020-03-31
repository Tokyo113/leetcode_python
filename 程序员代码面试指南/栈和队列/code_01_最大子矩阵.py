#coding:utf-8
'''
@Time: 2020/3/31 16:34
@author: Tokyo
@file: code_01_最大子矩阵.py
@desc:
给定一个整型矩阵 map，其中的值只有 0 和 1 两种，求其中全是 1 的所有矩形区域中，最大的矩形区域里 1 的数量。
输入描述:
第一行输入两个整数 n 和 m，代表 n*m 的矩阵
接下来输入一个 n*m 的矩阵
输出描述:
输出其中全是 1 的所有矩形区域中，最大的矩形区域里 1 的数量。
示例1
输入
复制
1 4
1 1 1 0
输出
复制
3
说明
最大的矩形区域有3个1，所以返回3



height 数组肯定有重复值的情况，其实不需要改为原始单调栈结构中的list结构
为啥呢？
比如2，4，5，6，4，7
第一个4能扩到的区域至少是第二个四，就按这个算就好了
算到第二个四的时候肯定能包含之前的结果，无需担心

'''


def maxSubMatrix(arr):
    if arr is None or arr == []:
        return 0
    height = [0 for i in range(len(arr[0]))]
    maxArea = 0
    for i in range(0, len(arr)):
        for j in range(len(arr[0])):
            height[j] =height[j]+1 if arr[i][j] == 1 else 0

        print(height)

        maxArea = max(maxArea, getMaxArea(height))
    return maxArea


def getMaxArea(arr):
    '''
    单调栈生成最大面积
    必然存在重复值的情况，需要改成list吗？
    不需要的
    :param arr:
    :return:
    '''
    if arr is None or arr == []:
        return 0
    maxArea = 0
    stack = []
    for i in range(len(arr)):
        while stack != [] and arr[i]<=arr[stack[-1]]:
            pp = stack.pop()
            left = -1 if stack == [] else stack[-1]
            curArea = (i-left-1)*arr[pp]
            maxArea = max(maxArea,curArea)
        stack.append(i)

    while stack != []:
        pp = stack.pop()
        left = -1 if stack == [] else stack[-1]
        curArea = (len(arr)-left-1)*arr[pp]
        maxArea = max(maxArea,curArea)
    return maxArea

def maxSub(arr):
    if arr is None or arr == []:
        return 0
    height = [0 for i in range(len(arr[0]))]
    maxArea = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            height[j] = height[j] + 1 if arr[i][j] == 1 else 0
        maxArea = max(maxArea, getMax(height))
    return maxArea

def getMax(height):
    stack = []
    maxArea = 0
    for i in range(len(height)):
        while stack != [] and height[i]<=height[stack[-1]]:
            pp = stack.pop()
            left = -1 if stack == [] else stack[-1]
            maxArea = max(maxArea, (i-left-1)*height[pp])
        stack.append(i)
    while stack != []:
        pp = stack.pop()
        left = -1 if stack == [] else stack[-1]
        maxArea = max(maxArea, (len(height)-left-1)*height[pp])
    return maxArea
if __name__ == '__main__':
    arr = [[1,0,1,1],[1,1,1,1],[1,1,1,0]]
    print(maxSubMatrix(arr))
    print(maxSub(arr))


