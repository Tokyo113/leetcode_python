#coding:utf-8
'''
@Time: 2019/10/10 15:26
@author: Tokyo
@file: code_03_MergeSort.py
@desc:
'''


def merge_sort(arr):
    """
    使用了切片操作
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    arr_l = merge_sort(arr[:mid])
    arr_r = merge_sort(arr[mid:])

    list_new = []
    p1 = 0
    p2 = 0
    while(p1 < len(arr_l) and p2 < len(arr_r)):

        if arr_l[p1] < arr_r[p2]:
            list_new.append(arr_l[p1])
            p1 += 1
        else:
            list_new.append(arr_r[p2])
            p2 += 1

    list_new += arr_r[p2:]
    list_new += arr_l[p1:]

    for i in range(0, len(list_new)):
        arr[i] = list_new[i]
    return arr


def mergeSort(arr):
    # 不能写成 ==1， 因为会有len（arr）== 0 的情形
    if len(arr) <= 1:
        return arr

    mid = len(arr) >> 1
    arr_left = mergeSort(arr[:mid])
    arr_right = mergeSort(arr[mid:])

    p_left, p_right = 0, 0
    arr_new = []
    while (p_left < len(arr_left) and p_right < len(arr_right)):
        if arr_left[p_left] < arr_right[p_right]:
            arr_new.append(arr_left[p_left])
            p_left += 1
        else:
            arr_new.append(arr_right[p_right])
            p_right += 1
    arr_new += arr_left[p_left:]
    arr_new += arr_right[p_right:]

    for i in range(len(arr_new)):
        arr[i] = arr_new[i]
    return arr












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
    testTime = 5000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(0, testTime):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()

        mergeSort2(arr1)
        comparator(arr2)

        if (arr1 != arr2):
            succeed = False
            print(arr2)
            print(arr1)
            break
    print("Nice!" if succeed else "Fucking fucked")

    a= [1,2,3,4,5,6]




