#coding:utf-8
'''
@Time: 2019/10/16 18:43
@author: Tokyo
@file: code_13_maxGap.py
@desc:
'''

'''
给定一个数组，求如果排序之后，相邻两数的最大差值，
要求时间复杂度O(N),且不能用非基于比较的排序
'''

def method1(arr):
    """
    方法一：暴力解法
    :param arr:
    """
    arr.sort()
    res = 0
    for i in range(len(arr)-1):
         res = arr[i+1]-arr[i] if (arr[i+1] - arr[i] > res) else res
    return res


def method2(arr):
    """
    基于分桶思想的方法
    :param arr:
    1.准备N+1个桶，数组的最小值放第一个桶，最大值放第二个桶
    2.将中间的值分别放入每个桶中，记录每个桶的min，max,hasnum
    3.从第一个桶开始遍历，前一个非空桶的最大值和后一个非空桶的最小值
    """

    n = len(arr)
    if n <= 1:
        return 0
    mins = [None for i in range(n+1)]
    maxs = [None for i in range(n+1)]
    hasnum = [None for i in range(n+1)]
    arr_min = min(arr)
    arr_max = max(arr)
    if arr_max == arr_min:
        return 0
    for i in range(n):
        # 每个元素放入桶中
        bid = bucket_num(arr[i], n, arr_min, arr_max)
        # 不能用数组元素判断，若该元素为0，则条件为真
        mins[bid] = arr[i] if not hasnum[bid] else min(mins[bid], arr[i])
        maxs[bid] = arr[i] if not hasnum[bid] else max(maxs[bid], arr[i])
        hasnum[bid] = True

    res = 0
    max_cur = maxs[0]
    for j in range(1, len(arr)+1):
        if hasnum[j]:
            res = res if mins[j] - max_cur <= res else mins[j] - max_cur
            max_cur = maxs[j]
    return res

def bucket_num(arr, n, min, max):
    return int(((arr-min)*n/(max-min)))






# Python对数器
def comparator(arr):
    arr.sort()


def generateRandomArray(maxSize, maxValue):
    import random
    random_list = []
    for i in range(int((maxSize+1)*random.random())):
        random_list.append(int((maxValue+1)*random.random())-int(maxValue*random.random()))
    return random_list

def copyArray(arr):
    if not arr:
        return
    res = []
    for i in arr:
        res.append(i)
    return res

if __name__ == '__main__':
    testTime = 500
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(0, testTime):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()

        res1 = method1(arr1)
        res2 = method2(arr2)

        if (res1 != res2):
            succeed = False
            print(arr1)
            print(res1, res2)
            break
    print("Nice!" if succeed else "Fucking fucked")


