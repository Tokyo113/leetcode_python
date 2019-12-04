#coding:utf-8
'''
@Time: 2019/11/27 15:46
@author: Tokyo
@file: code_03_AllTimesMinToMax.py
@desc:
定义：数组中累积和与最小值的乘积，假设叫做指标A。
给定一个正数数组，请返回子数组中，指标A最大的值。
思考：
为什么对于重复元素也适用？
'''


def baoli(arr):
    maxA = 0

    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum = 0
            minNum = arr[i]
            for k in range(i,j+1):
                minNum = min(minNum, arr[k])
                sum += arr[k]

            maxA = max(maxA, sum*minNum)

    return maxA


def findMaxA(arr):
    '''
    单调栈的方法，每个元素轮流当最小值
    区间就是单调栈给出的离他最近的两个比他小的index
    :param arr:
    :return:
    '''
    if arr == []:
        return 0

    maxA = 0
    stack = []
    size = len(arr)
    sums = [0 for i in range(size)]
    sums[0] = arr[0]
    for i in range(1,size):
        sums[i] = sums[i-1] + arr[i]


    for i in range(len(arr)):
        while stack != [] and arr[i] <= arr[stack[-1]]:
            popIndex = stack.pop()
            maxA = max(maxA, (sums[i-1]-sums[stack[-1]])*arr[popIndex] if stack != [] else sums[i-1]*arr[popIndex])

        stack.append(i)

    while stack != []:
        popIndex = stack.pop()
        maxA = max(maxA, (sums[size-1]-sums[stack[-1]])*arr[popIndex] if stack != [] else (sums[size-1])*arr[popIndex])

    return maxA





def generateRandomArray(maxSize, maxValue):
    import random
    random_list = []
    for i in range(int((maxSize+1)*random.random())):
        random_list.append(int((maxValue+1)*random.random()))
    return random_list





if __name__ == '__main__':
    testTime = 5000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(0, testTime):
        arr1 = generateRandomArray(maxSize, maxValue)


        a = baoli(arr1)
        b =findMaxA(arr1)

        if (a != b):
            succeed = False
            print(arr1)
            print(a,b)
            break
    print("Nice!" if succeed else "Fucking fucked")



