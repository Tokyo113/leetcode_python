#coding:utf-8
'''
@Time: 2019/10/9 15:22
@author: Tokyo
@file: code_01_BubbleSort.py
@desc:
'''


def bubbleSort(arr):
    """
    冒泡排序
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return
    for i in range(len(arr)-1, 0, -1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selectionSort(arr):
    if len(arr) < 2:
        return
    for i in range(0, len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

import random
def quicksort(arr, L, R):



    if L < R:
        rand = L + int(random.random() * (R - L + 1))
        arr[R], arr[rand] = arr[rand], arr[R]

        p= partition(arr, L, R)
        quicksort(arr, L, p[0]-1)
        quicksort(arr, p[1]+1, R)

def partition(arr, L, R):

    num = arr[R]
    cur = L
    less, more = L-1, R + 1
    while cur < more:
        if arr[cur] < num:
            arr[cur], arr[less+1] = arr[less+1], arr[cur]
            less += 1
            cur += 1
        elif arr[cur] == num:
            cur += 1
        else:
            arr[cur], arr[more-1] = arr[more-1], arr[cur]
            more -= 1

    return less+1, more-1

def duipaixu(arr):
    if len(arr) < 2:
        return

    for i in range(len(arr)):
        heapinsert(arr, i)

    heapsize = len(arr)
    while heapsize > 0:
        arr[0], arr[heapsize-1] = arr[heapsize-1], arr[0]
        heapsize -= 1
        heapify(arr, 0, heapsize)

def heapinsert(arr, i):
    while arr[i] > arr[(i-1)>>1] and ((i-1)>>1) >=0:
        arr[i], arr[(i-1)>>1] = arr[(i-1)>>1], arr[i]
        i = (i-1)>>1

def heapify(arr, index, size):
    left = 2*index + 1
    while left < size:
        largest = left+1 if arr[left+1] > arr[left] and (left+1) < size else left
        largest = index if arr[index] > arr[largest] else largest

        if largest == index:
            break
        arr[largest], arr[index] = arr[index], arr[largest]
        index = largest
        left = 2*index +1

    return











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
    testTime = 509
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(0, testTime):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()

        duipaixu(arr1)
        comparator(arr2)

        if (arr1 != arr2):
            succeed = False
            print(arr1)
            break
    print("Nice!" if succeed else "Fucking fucked")