#coding:utf-8
'''
@Time: 2020/2/25 10:13
@author: Tokyo
@file: code_03_LongestSubArr.py
@desc:
求一个数组的最长递增子序列的长度
比如：
[3,2,4,5,1,7]
最长为[2,4,5,7],长度为4
'''


def maxLength(arr):
    '''
    O(N*N)
    :param arr:
    :return:
    '''
    if arr is None or arr == []:
        return 0
    dp = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        maxlen = 0
        for j in range(i):
            if arr[j] < arr[i]:
                maxlen = max(dp[j], maxlen)
        dp[i] = maxlen+1

    return max(dp)

def maxLength1(arr):
    '''
    O(NlogN)
    将第二层遍历转化为一个数组结构记录，不需要遍历
    N降为logN（二分）
    :param arr:
    :return:
    '''
    if arr is None or arr == []:
        return 0
    dp = [0 for i in range(len(arr))]
    ends = []

    for i in range(len(arr)):
        if findleft(ends,arr[i]) == -1:
            ends.append(arr[i])
            dp[i] = len(ends)

        else:
            index = findleft(ends,arr[i])
            ends[index] = arr[i]
            dp[i] = index+1
    return max(dp)


def findleft(arr, num):
    '''
    找到arr中大于num的最左侧的index
    :param arr:
    :param num:
    :return:
    '''
    if arr is None or arr == []:
        return -1
    L = 0
    R = len(arr)-1
    index = -1

    while L <= R:
        mid = (L+R)//2

        if arr[mid] >= num:
            R = mid-1
            index = mid
        else:
            L = mid+1

    return index


def findSub(arr):
    if arr is None or arr == []:
        return []
    dp = [1 for i in range(len(arr))]
    ends = []
    for i in range(len(arr)):
        index = findLeft2(ends,arr[i])
        if index == -1:
            ends.append(arr[i])
            dp[i] = len(ends)
        else:
            ends[index] = arr[i]
            dp[i] = index+1
    maxLen = max(dp)
    stack = []
    pre = float('inf')
    for i in range(len(arr)-1,-1,-1):
        if maxLen == 0:
            break
        if dp[i] == maxLen and arr[i]<pre:
            stack.append(arr[i])
            pre = arr[i]
            maxLen -= 1
    print(dp)
    return stack[::-1]


def findLeft2(arr,aim):
    if arr is None or arr ==[]:
        return -1
    L, R = 0, len(arr)-1
    pre = -1
    while L <=R:
        mid = (L+R)//2
        if arr[mid]>=aim:
            pre = mid
            R = mid-1
        else:
            L = mid+1
    return pre



def generateRandArr(maxValue, maxSize):
    import random
    return [int((maxValue+1)*random.random()-(maxValue+1)*random.random()) for i in range(int((maxSize+1)*random.random()))]


if __name__ == '__main__':
    arr = [1,1,4,7,9,8]
    print(maxLength(arr))
    print(maxLength1(arr))
    print(findSub(arr))


    # maxValue = 50
    # maxSize = 20
    # testTime = 100
    # for i in range(testTime):
    #     arr = generateRandArr(maxValue, maxSize)
    #     a = maxLength(arr)
    #     b = maxLength1(arr)
    #
    #     if a != b:
    #         print(arr)
    #         print(a, b)
    #         break


