#coding:utf-8
'''
@Time: 2020/2/16 9:04
@author: Tokyo
@file: code_03_waterProblem.py
@desc:
给定一个数组arr，已知其中所有的值都是非负的，将这个数组看作一个容器，
请返回容器能装多少水
比如，arr = {3，1，2，5，2，4}，根据值画出的直方图就是容器形状，该容
器可以装下5格水
再比如，arr = {4，5，1，3，2}，该容器可以装下2格水
'''

def waterProblem(arr):
    '''
    每次遍历i位置前后两部分找最大值
    :param arr:
    :return:
    '''
    if len(arr) <= 2:
        return 0
    res = 0
    for i in range(1,len(arr)-1):
        res += max(min(max(arr[:i]), max(arr[i+1:]))-arr[i],0)

    return res


def waterProblem2(arr):
    '''
    使用辅助数组记录最大值
    :param arr:
    :return:
    '''
    if arr is None or arr == []:
        return 0
    leftMax = [max(arr[:i+1]) for i in range(len(arr))]
    rightMax = [max(arr[i+2:]) for i in range(len(arr)-2)]
    res = 0
    for i in range(1,len(arr)-1):
        res += max(min(leftMax[i-1],rightMax[i-1])-arr[i],0)
    return res

def waterProblem1(arr):
    if len(arr) <= 2:
        return 0
    leftMax = arr[0]
    rightMax = arr[-1]
    l, r = 1, len(arr)-2
    res = 0
    while l <= r:
        # 哪边的最大值小，哪边就是瓶颈，就从哪边开始结算
        if leftMax <= rightMax:
            res += max(leftMax-arr[l], 0)
            leftMax = max(leftMax, arr[l])
            l += 1
        else:
            res += max(rightMax-arr[r], 0)
            rightMax = max(rightMax, arr[r])
            r -= 1
    return res
import random
def generateRandomArray(maxValue, maxSize):
    return [int(random.random()*(maxValue+1)) for i in range(int((maxSize+1)*random.random()))]

if __name__ == '__main__':
    # testtime = 100
    # maxValue = 50
    # maxSize = 20
    # succeed = True
    # for i in range(testtime):
    #     arr = generateRandomArray(maxValue, maxSize)
    #     a = waterProblem(arr)
    #     b = waterProblem1(arr)
    #     if a != b:
    #         print(a, b)
    #         print('fucking fucked!!!')
    #         succeed = False
    #         break
    # print('nice!!' if succeed else 'fuck')
    arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(waterProblem(arr))
    print(waterProblem2(arr))