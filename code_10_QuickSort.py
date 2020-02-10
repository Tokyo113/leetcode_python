#coding:utf-8
'''
@Time: 2019/10/14 18:43
@author: Tokyo
@file: code_10_QuickSort.py
@desc:基于荷兰国旗问题的快速排序
'''
import random
def quickSort(arr, L, R):
    """
    在指定区间上实现快速排序
    :param arr:
    :param L:
    :param R:
    """

    if L < R:
        # 随机快排,随机选择一个数与最后位置的数交换
        rand = int((random.random()*(R-L+1)))
        arr[L+rand], arr[R] = arr[R], arr[L+rand]

        p = partition(arr, L, R)
        quickSort(arr, L, p[0]-1)
        quickSort(arr, p[1]+1, R)

def partition(arr, L, R):
    """

    :param arr:
    :param L:
    :param R:
    :return:返回中间等于num的左右index
    """
    less = L-1
    more = R+1
    cur = L
    num = arr[R]
    while (cur < more):
        if arr[cur] < num:
            arr[less+1], arr[cur] = arr[cur], arr[less+1]
            less += 1
            cur +=1
        elif arr[cur] > num:
            arr[cur], arr[more-1] = arr[more-1], arr[cur]
            more -= 1
        else:
            cur += 1
    return less+1, more-1





def quickpai(arr, L, R):
    if L < R:
        rand = L+int(random.random()*(R-L+1))
        arr[rand], arr[R] = arr[R], arr[rand]
        p = partition1(arr, L, R)
        quickpai(arr, 0, p[0]-1)
        quickpai(arr, p[1]+1, R)

def partition1(arr, L, R):
    less, more = L-1, R+1
    num = arr[R]
    cur = L
    while cur < more:
        if arr[cur] < num:
            arr[cur], arr[less+1] = arr[less+1], arr[cur]
            cur += 1
            less += 1
        elif arr[cur] == num:
            cur += 1
        else:
            arr[cur], arr[more-1] = arr[more-1], arr[cur]
            more -= 1
    return less+1, more-1


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
    testTime = 500
    maxSize = 10
    maxValue = 10
    succeed = True
    for i in range(0, testTime):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1.copy()

        quickpai(arr1, 0, len(arr1)-1)
        comparator(arr2)

        if (arr1 != arr2):
            succeed = False
            break
    print("Nice!" if succeed else "Fucking fucked")


