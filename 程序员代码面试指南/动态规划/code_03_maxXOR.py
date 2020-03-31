#coding:utf-8
'''
@Time: 2020/3/27 10:52
@author: Tokyo
@file: code_03_maxXOR.py
@desc:
给定一个整型数组arr，其中可能有正有负有零。你可以随意把整个数组切成若干个不相容的子数组，求异或和为0的子数组最多可能有多少个？整数异或和定义：把数组中所有的数异或起来得到的值。
输入描述:
输出包括两行，第一行一个整数，代表数组长度n(1 \leq n \leq 10^6)(1≤n≤10
6
 )。第二行有n个整数，代表数组arr\left(-1e9 \leq arr_i \leq 1e9 \right)(−1e9≤arr
i
​
 ≤1e9)。
输出描述:
输出一个整数，表示数组切割最多的子数组的个数。


单个数组问题就两个模型，从左往右，从右往左
这个题是从右往左
process(arr,n-1)
要求整个数组的最大异或和，看前一个数组
process(arr,i)----->process(arr,i-1)
1.最后一个子数组异或和不为0，比如arr[i]单独一个，看process(arr,i-1)
2.最后一个异或和为0，比如arr[k:i],dp[k-1]+1,
关键是k怎么求
'''


def maxXor1(arr):
    if arr is None or arr == []:
        return 0
    dp = [0 for i in range(len(arr))]
    dp[0] = 1 if arr[0] == 0 else 0

    xorMap = {}
    xorMap[0] = -1
    xorMap[arr[0]] = 0
    res = arr[0]
    for i in range(1,len(arr)):
        res = res^arr[i]
        k = xorMap.get(res)
        if k != None:
            dp[i] = 1 if k == -1 else dp[k]+1
        dp[i] = max(dp[i], dp[i-1])
        xorMap[res] = i
    print(xorMap)
    print(dp)
    return dp[len(arr)-1]


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
    # testTime = 50
    # maxSize = 10
    # maxValue = 10
    # succeed = True
    # for i in range(0, testTime):
    #     arr1 = generateRandomArray(maxSize, maxValue)
    #     arr2 = arr1.copy()
    #
    #     a = maxXor(arr1)
    #     b = maxXor1(arr2)
    #
    #     if (a != b):
    #         succeed = False
    #         print(arr1)
    #         print(a,b)
    #         break
    # print("Nice!" if succeed else "Fucking fucked")
    print(maxXor1([3,2,1,9,0,7,0,2,1,3]))



