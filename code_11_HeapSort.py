#coding:utf-8
'''
@Time: 2019/10/15 16:07
@author: Tokyo
@file: code_11_HeapSort.py
@desc:
'''

def heap_sort(arr):
    if len(arr) < 2:
        return

    # 1.将数组变为大根堆
    for i in range(len(arr)):
        heapInsert(arr, i)
    # 2.循环执行heapify过程
    heapSize = len(arr)
    arr[0], arr[heapSize-1] = arr[heapSize-1], arr[0]
    heapSize -= 1
    while(heapSize>0):
        heapify(arr, 0, heapSize)
        arr[0], arr[heapSize-1] = arr[heapSize-1], arr[0]
        heapSize -= 1
    return


def heapInsert(arr, index):
    # 注意在python中，-1//2 = -1
    while (arr[index] > arr[(index-1)//2] and (index-1)>>1 >= 0):
        arr[index], arr[(index-1)//2] = arr[(index-1)//2], arr[index]
        index = (index-1)//2
    return

def heapify(arr, index, size):


    left = 2*index + 1
    while(left<size):
        largest = left+1 if ((arr[left+1] >= arr[left]) and ((left+1) < size)) else left
        largest = index if arr[index] >= arr[largest] else largest
        if (largest == index):
            break

        arr[largest], arr[index] = arr[index], arr[largest]
        index = largest
        left = 2*index + 1



def HeapSort(arr):
    if len(arr) < 2:
        return

    for i in range(len(arr)):
        heap_insert(arr, i)

    heapsize = len(arr)
    while (heapsize > 0):
        arr[0], arr[heapsize-1] = arr[heapsize-1], arr[0]
        heapsize -= 1
        heapify(arr, 0, heapsize)
    return

def heap_insert(arr, i):
    while(arr[i] > arr[(i-1)>>1] and ((i-1)>>1) >= 0 ):
        arr[i], arr[(i-1) >>1] = arr[(i-1)>>1], arr[i]
        i = (i-1) >> 1

def Heapify(arr, i, size):
    left = 2*i+1
    while(left< size):
        largest = left+1 if arr[left+1] >= arr[left] and (left+1) < size else left
        largest = largest if arr[largest] >= arr[i] else i
        if (largest == i):
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
    testTime = 5000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(0, testTime):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()

        HeapSort(arr1)
        comparator(arr2)

        if (arr1 != arr2):
            succeed = False
            break
    print("Nice!" if succeed else "Fucking fucked")
    # a = [6,-4,-8,4,9, 3, 5]
    # for i in range(len(a)):
    #     heapInsert(a, i)
    # print(a)



