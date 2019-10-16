#coding:utf-8
'''
@Time: 2019/10/16 14:46
@author: Tokyo
@file: code_12_sortSum.py
@desc:summary of 6 sort algorithms
'''
import random
def bubbleSort(arr):
    if len(arr)< 2:
        return
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selectSort(arr):
    if len(arr) < 2:
        return
    for i in range(len(arr)):
        min_index = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def insertSort(arr):
    if len(arr) < 2:
        return
    for i in range(1,len(arr)):
        for j in range(i,0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) >> 1
    arr_l = mergeSort(arr[:mid])
    arr_r = mergeSort(arr[mid:])

    p1, p2 = 0, 0
    arr_new = []

    while(p1 < len(arr_l) and p2 < len(arr_r)):
        if arr_l[p1] <= arr_r[p2]:
            arr_new.append(arr_l[p1])
            p1 += 1
        else:
            arr_new.append(arr_r[p2])
            p2 += 1
    arr_new += arr_l[p1:]
    arr_new += arr_r[p2:]

    for i in range(len(arr_new)):
        arr[i] = arr_new[i]
    return arr

def quickSort(arr, L, R):

    if L < R:
        rand = int((random.random()*(R-L+1)))
        arr[R], arr[L+rand] = arr[L+rand], arr[R]
        p = partition(arr, L, R)
        quickSort(arr, L, p[0]-1)
        quickSort(arr, p[1]+1, R)


def partition(arr, L, R):
    less, more = L-1, R+1
    cur = L
    num = arr[R]
    while(cur < more):
        if arr[cur] < num:
            arr[cur], arr[less+1] = arr[less+1], arr[cur]
            cur += 1
            less += 1
        elif arr[cur] > num:
            arr[cur], arr[more-1] = arr[more-1], arr[cur]
            more -= 1
        else:
            cur += 1
    return less+1, more-1


def heapSort(arr):
    if len(arr) < 2:
        return

    for i in range(len(arr)):
        heapInsert(arr, i)

    heapsize = len(arr)
    while (heapsize > 0):
        arr[0], arr[heapsize-1] = arr[heapsize-1], arr[0]
        heapsize -= 1
        heapify(arr, 0, heapsize)
    return

def heapInsert(arr, index):

    while arr[index] > arr[(index-1) >> 1] and ((index-1) >> 1) >= 0:
        arr[index], arr[(index-1)>>1] = arr[(index-1)>> 1], arr[index]
        index = (index-1) >> 1

def heapify(arr, i, size):

    left = 2*i + 1
    while(left< size):
        largest = left+1 if arr[left+1]> arr[left] and (left+1) < size else left
        largest = i if arr[i] > arr[largest] else largest
        if largest == i:
            break
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest
        left = 2*i+1




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
    testTime = 50
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(0, testTime):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()

        heapSort(arr1)
        comparator(arr2)

        if (arr1 != arr2):
            succeed = False
            break
    print("Nice!" if succeed else "Fucking fucked")

