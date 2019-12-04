#coding:utf-8
'''
@Time: 2019/10/10 19:50
@author: Tokyo
@file: code_05_binarySearch.py
@desc: 二分查找
'''

def binary_search(arr, item):
    """
    递归实现二分查找
    :param arr:
    :param item:
    """
    if len(arr) >= 1:
        mid = len(arr) >> 1
        if (item > arr[mid]):
            # 注意一定要加return，否则返回mid后顺序往下执行，最终返回-1
            return binary_search(arr[mid+1:], item)
        elif(item < arr[mid]):
            return binary_search(arr[:mid], item)
        else:
            return mid
    return -1


if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    print(binary_search(a, 6))