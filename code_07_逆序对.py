#coding:utf-8
'''
@Time: 2019/10/11 15:23
@author: Tokyo
@file: code_07_逆序对.py
@desc:
'''
'''
一个数组中，如果左边的数比右边的数大，则这两个数构成一个逆序对，请打印所有逆序对
例如：数组 <2,3,8,6,1> 的逆序对为：<2,1> <3,1> <8,1> <8,6> <6,1> 共5个逆序对。

'''

def method1(arr):
    """
    暴力求解
    :param arr:
    """
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                print((arr[i],arr[j]))

def method2(arr):
    """
    MergeSort method
    :param arr:
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) >> 1
    arr_l = method2(arr[:mid])
    arr_r = method2(arr[mid:])

    p1, p2 = 0, 0
    arr_new = []

    while (p1 < len(arr_l) and p2 < len(arr_r)):
        if (arr_l[p1] <= arr_r[p2]):
            arr_new.append(arr_l[p1])
            p1 += 1
        else:
            # 排序的意义所在：
            # 如果arr_l[p1] > arr_r[p2],由于arr_l是有序的，
            # 则arr_l右边剩余的元素肯定也比此时的arr_r[p2]大，即都为逆序对
            for k in arr_l[p1:]:
                print((k, arr_r[p2]))
            arr_new.append(arr_r[p2])
            p2 += 1
    arr_new += arr_l[p1:]
    arr_new += arr_r[p2:]

    for i in range(len(arr_new)):
        arr[i] = arr_new[i]
    return arr




if __name__ == '__main__':
    a = [2,3,8,6,1,7,4,12]
    method1(a)
    print("*"*50)
    print(method2(a))
