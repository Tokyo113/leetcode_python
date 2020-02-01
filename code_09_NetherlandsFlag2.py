#coding:utf-8
'''
@Time: 2019/10/11 18:35
@author: Tokyo
@file: code_09_NetherlandsFlag2.py
@desc:进阶版荷兰国旗问题
'''
'''
给定一个数组arr 和一个数num,请把小于等于num的数放在数组的左边，
等于num的数放在数组的中间，大于num的数放在数组的右边，
要求额外空间复杂度O(1), 时间复杂度O(N)
进阶：在数组的[L,R]范围内完成如上排序
'''

def netherlands(arr, num):
    """
    需要三个指针，分别表示小于区less，游标cur以及大于区more
    arr[i] = num : cur ++
    arr[i] < num : 和小于区的下一个元素交换，less ++, cur++
    arr[i] > num : 和大于区的前一个元素交换，more -- ，此时游标不移动，继续比较
    :param arr:
    :param num:
    """

    less = -1
    more = len(arr)
    cur = 0

    while (cur < more):
        if arr[cur] == num:
            cur += 1
        elif arr[cur] < num:
            arr[cur], arr[less+1] = arr[less+1], arr[cur]
            less += 1
            cur += 1
        else:
            arr[cur], arr[more-1] = arr[more-1], arr[cur]
            more -= 1


def netherlands_plus(arr, num, l, r):
    """
    进阶版，在给定区间完成如上排序
    :param arr:
    :param num:
    :param l: 左边界
    :param r: 右边界
    """
    if l >= r:
        return
    less, more = l-1, r+1
    cur = l

    while (cur < more):
        if arr[cur] == num:
            cur += 1
        elif arr[cur] < num:
            arr[cur], arr[less+1] = arr[less+1], arr[cur]
            cur += 1
            less += 1
        else:
            arr[cur], arr[more-1] = arr[more-1], arr[cur]
            more -= 1

def partition(arr, num, l, r):
    if l >= r:
        return
    small, big = l-1,r+1
    i = l
    while i < big:
        if arr[i] < num:
            arr[i], arr[small+1] = arr[small+1], arr[i]
            small += 1
            i += 1
        elif arr[i] == num:
            i += 1
        else:
            arr[i], arr[big-1] = arr[big-1], arr[i]
            big -= 1








if __name__ == '__main__':
    a = [5,7,3,-9,20,45,45,-78,2,4,6,4,-3]
    num = -1
    # netherlands_plus(a, num, 2, 7)
    partition(a, num, 1,7)
    print(a)
