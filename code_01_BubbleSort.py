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


def heapSort(arr):
    if len(arr) <= 1:
        return

    for i in range(len(arr)):
        heapInsert(arr, i)

    heapsize = len(arr)
    while (heapsize > 1):
        arr[heapsize-1], arr[0] = arr[0], arr[heapsize-1]
        heapsize -= 1
        heapify(arr, 0, heapsize)


def heapInsert(arr, i):
    while(arr[i] > arr[(i-1)>>1] and ((i-1) >> 1) >= 0 ):
        arr[i], arr[(i-1) >> 1] = arr[(i-1) >> 1], arr[i]
        i = (i-1)>> 1


def heapify(arr, index, size):
    left = 2*index + 1
    while(left < size):
        largest = left + 1 if arr[left+1] > arr[left] and left+1 < size else left
        largest = index if arr[index] > arr[largest] else largest
        if largest == index:
            break
        else:
            arr[largest], arr[index] = arr[index], arr[largest]
            index = largest
            left = 2*index+1

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