#coding:utf-8
'''
@Time: 2019/10/10 19:06
@author: Tokyo
@file: code_04_理解时间复杂度.py
@desc:
'''

'''
一个简单理解时间复杂度的例子
一个有序数组A， 另一个无序数组B，请打印B中所有不在A中的数，
A，B数组的长度分别为N， M
三种思路：
1：暴力求解：对于数组B中每一个数，在A中遍历
2.对于B中每一个数，在A中二分查找（利用了有序的条件）
3.先把B排序，然后用类似外排的方式打印不在A中的数
'''

from code_05_binarySearch import binary_search
def method1(arr1, arr2):
    """
    暴力求解 O(N^2)
    :param arr1:
    :param arr2:
    """
    for ele in arr2:
        flag = 0
        # if ele not in arr1:
        #     print(ele)
        for j in arr1:
            if ele == j:
                flag = 1
                break
        if not flag:
            print(ele)


def method2(arr1, arr2):
    """
    对于B中每一个元素，在A中二分查找  O(MlogN)
    :param arr1:
    :param arr2:
    """
    for ele in arr2:
        res = binary_search(arr1, ele)
        if res == -1:
            print(ele)
def method3(arr1, arr2):
    """
    先排序，再外排    O(MlogM)+ O(M+N)
    :param arr1:
    :param arr2:
    """
    arr2.sort()
    p1 = 0
    p2 = 0
    while (p1 < len(arr1) and p2 < len(arr2)):
        if (arr2[p2] < arr1[p1]):
            print(arr2[p2])
            p2 += 1
        elif (arr2[p2] == arr1[p1]):
            p2 += 1
        else:
            p1 += 1
    # 最后不管是哪个指针越界，直接打印p2后面元素即可
    # 因为如果p2越界，下面语句不会打印
    for ele in arr2[p2:]:
        print(ele)



if __name__ == '__main__':
    a = [1,2,3,4,5,20,30,40,100]
    b=[-1,2,63,4,-7,100,45,1,40]
    method3(a, b)
    print("="*50)
    method1(a, b)
    print("="*50)
    method2(a, b)


