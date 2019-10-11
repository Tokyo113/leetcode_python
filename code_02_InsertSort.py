#coding:utf-8
'''
@Time: 2019/10/10 14:53
@author: Tokyo
@file: code_02_InsertSort.py
@desc:插入排序最优时间复杂度可达到O(N)
'''

'''
分为有序区和无序区，每次从无序区中取一个插入到有序区的正确位置

'''
def insert_sort(arr):
    if len(arr) < 2:
        return
    # 外层循环从无序区中选一个
    for i in range(1,len(arr)):
        j = i
        while(j > 0):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
            else:
                break

def insertSort(arr):

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]




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

        insertSort(arr1)
        comparator(arr2)

        if (arr1 != arr2):
            succeed = False
            break
    print("Nice!" if succeed else "Fucking fucked")


