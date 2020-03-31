#coding:utf-8
'''
@Time: 2020/3/25 13:09
@author: Tokyo
@file: code_07_Envelop.py
@desc:
给n个信封的长度和宽度。如果信封A的长和宽都小于信封B，那么信封A可以放到信封B里，请求出信封最多可以嵌套多少层。
输入描述:
输出包含多行，第一行包括一个整数，代表信封的个数n\left(1 \leq n\leq  10^{5}\right)(1≤n≤10
5
 )。接下来n行，每行两个整数l_il
i
​
 和w_iw
i
​
 ，代表信封的长度和宽度\left( -1e9\leq l_i,w_i \leq 1e9 \right)(−1e9≤l
i
​
 ,w
i
​
 ≤1e9)。
输出描述:
输出包括一行，代表信封最多嵌套多少层。
示例1
输入
复制
9
3 4
2 3
4 5
1 3
2 2
3 6
1 2
3 2
2 4
输出
复制
4
说明
从里到外分别是{1，2}，{2，3}，{3，4}，{4，5}。

要求时间复杂度O(logN)
和前面的最长递增子序列一样的问题
'''

import functools
def cmp(a,b):
    if a[0]<b[0] or (a[0]==b[0] and a[1]>b[1]):
        return -1
    elif a[0]==b[0] and a[1] == b[1]:
        return 0
    else:
        return 1




def envelop(arr):
    if arr is None or arr == []:
        return 0
    arr.sort(key = functools.cmp_to_key(cmp))
    dp = [1 for i in range(len(arr))]
    ends = []
    for i in range(len(arr)):
        index = findLeft(ends,arr[i][1])
        if index == -1:
            ends.append(arr[i][1])
            dp[i] = len(ends)
        else:
            ends[index] = arr[i][1]
            dp[i] = index+1

    return max(dp)

def findLeft(arr,aim):
    if arr is None or arr == []:
        return -1
    L,R = 0, len(arr)-1
    pre = -1
    while L <=R:
        mid = (L+R)//2
        if arr[mid]>=aim:
            pre = mid
            R = mid-1
        else:
            L = mid+1
    return pre


if __name__ == '__main__':
    arr = [[1,4],[4,1]]
    print(envelop(arr))

