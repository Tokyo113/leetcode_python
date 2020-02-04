#coding:utf-8
'''
@Time: 2020/2/2 14:42
@author: Tokyo
@file: code_01_CordCoverMaxPoints.py
@desc:
给定一个有序数组arr，代表数轴上从左到右有n个点arr[0]、arr[1]...arr[n－1]，
给定一个正数L，代表一根长度为L的绳子，求绳子最多能覆盖其中的几个点。
'''


def method1(arr, L):
    '''
    方法1：二分法，O(NlogN)
    :param arr:
    :param L:
    :return:
    '''
    if arr is None or len(arr) < 1:
        return 0
    max_points = 0
    for i in range(len(arr)):
        value = arr[i]-L
        left = findNearLeft(arr, i, value)
        max_points = max(max_points, i-left+1)

    return max_points

def findNearLeft(arr, R, value):
    '''
    找到arr中大于等于value的最左侧的数的下标
    :param arr:
    :param R:
    :param value:
    :return:
    '''
    L = 0
    index = -1
    while L <= R:
        mid = L+((R-L)>>1)
        if arr[mid] >= value:
            index = mid
            R = mid-1
        else:
            L = mid + 1
    return index

def method2(arr, length):
    '''
    类似滑动窗口法，复杂度进一步降低O(N)
    分别将绳子左端放在arr中每一个点
    双指针问题
    窗口中维持的是什么？
    维持的始终是覆盖最多的点的个数，只增不减
    :param arr:
    :param length:
    :return:
    '''
    if arr is None or length <= 0 or arr == []:
        return 0
    # 只要绳长>0，至少能覆盖1个点
    max_points = 1
    R = 1
    L = 0
    while L < len(arr):
        while R < len(arr) and arr[R] - arr[L] <= length:
            # 计算答案时L不动，R往右动
            R += 1
            max_points += 1
        # 维持窗口不变，L和R都要动，同时增加一个
        L += 1
        R += 1

    print((L,R))
    return max_points











if __name__ == '__main__':
    arr = []
    l = 8
    print(method1(arr, l))
    print(method2(arr, l))
    print(eee(arr,l))
