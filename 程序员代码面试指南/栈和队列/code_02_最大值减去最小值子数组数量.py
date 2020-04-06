#coding:utf-8
'''
@Time: 2020/4/2 21:03
@author: Tokyo
@file: code_02_最大值减去最小值子数组数量.py
@desc:
给定数组 arr 和整数 num，共返回有多少个子数组满足如下情况：
max(arr[i...j] - min(arr[i...j]) <= num
max(arr[i...j])表示子数组arr[i...j]中的最大值，min[arr[i...j])表示子数组arr[i...j]中的最小值。

输入描述:
第一行输入两个数 n 和 num，其中 n 表示数组 arr 的长度
第二行输入n个整数X_iX
i
​
 ，表示数组arr中的每个元素
输出描述:
输出给定数组中满足条件的子数组个数
'''


def findNum(arr, num):
    if arr is None or arr == []:
        return 0
    cnt = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)+1):
            pp = arr[i:j]
            if max(pp)-min(pp)<=num:
                cnt += 1


    return cnt

def findNum2(arr,num):
    '''
    最优解，时间复杂度和空间都是O(N)
    滑动窗口结构
    重要结论：
    如果一个子数组满足条件，那这个子数组的所有子数组一定也满足条件
    如果一个子数组不满足条件，那么包含这个子数组的数组一定不满足条件
    L和R都不回头，时间复杂度O(N)
    :param arr:
    :param num:
    :return:
    '''
    if arr is None or arr == []:
        return 0
    qmax = []
    qmin = []
    L,R = 0,0
    res = 0
    while L<len(arr):
        while R < len(arr):
            if qmin == [] or qmin[-1] != R:
                while qmax != [] and arr[R]>=arr[qmax[-1]]:
                    qmax.pop()
                qmax.append(R)

                while qmin != [] and arr[R]<=arr[qmin[-1]]:
                    qmin.pop()
                qmin.append(R)

            if qmax[0]-qmin[0]>num:
                break
            R += 1
        res += R-L
        if qmin[0] == L:
            qmin.pop(0)
        if qmax[0] == L:
            qmax.pop(0)
        L += 1
    return res















if __name__ == '__main__':
    arr = [1,2,3,4,5]
    print(findNum(arr,2))
    print(findNum2(arr,2))