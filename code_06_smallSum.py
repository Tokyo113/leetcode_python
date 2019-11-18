#coding:utf-8
'''
@Time: 2019/10/10 20:59
@author: Tokyo
@file: code_06_smallSum.py
@desc: 归并排序的应用
'''
'''
小和问题  smallSum
在一个数组中， 每一个数左边比当前数小的数累加起来， 叫做这个数组的小和。 求一个数组
的小和。
例子：
[1,3,4,2,5]
1左边比1小的数， 没有；
3左边比3小的数， 1；
4左边比4小的数， 1、 3；
2左边比2小的数， 1；
5左边比5小的数， 1、 3、 4、 2；
所以小和为1+1+3+1+1+3+4+2=16
'''
def method1(arr):
    """
    暴力解法 O(N^2)
    :param arr:
    """
    sum = 0
    for i in range(1,len(arr)):
        for j in range(0, i):
            if arr[j] < arr[i]:
                sum += arr[j]
    return sum

def merge_method(arr):
    """
    基于归并排序的思想：
    代码和归并排序完全一样
    :param arr:
    """

    if len(arr) == 1:
        res = 0
        return arr, res

    mid = len(arr) >> 1
    arr_left, res_left = merge_method(arr[:mid])
    arr_right, res_right = merge_method(arr[mid:])
    res = res_left + res_right
    list = []
    p_left, p_right = 0, 0
    while (p_left < len(arr_left) and p_right < len(arr_right)):
        if arr_left[p_left] < arr_right[p_right]:
            list.append(arr_left[p_left])
            res += arr_left[p_left] * (len(arr_right) - p_right)
            p_left += 1
        else:
            list.append(arr_right[p_right])
            p_right += 1
    list += arr_left[p_left:]
    list += arr_right[p_right:]
    return list, res











if __name__ == '__main__':
    a = [1,3,-4,2,5, 7,10,-12,55, 45,9,100]
    print(method1(a))
    print(merge_method(a)[1])
    print(smallSum(a)[1])