#coding:utf-8
'''
@Time: 2019/10/23 11:47
@author: Tokyo
@file: leetcode_0001_twoSum.py
@desc:
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''

def twoSum1(arr, target):
    """
    暴力解法
    :param arr:
    :param target:
    """
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return list((i, j))



def twoSum2(arr, target):
    """
    遍历两遍字典
    :param arr:
    :param target:
    """
    map = {}
    for i in range(len(arr)):
        map[arr[i]] = i
    print(map.items())
    for i in range(len(arr)):
        index2 = map.get(target-arr[i])
        if i != index2 and index2 != None:
            return [i, index2]

def twoSum3(arr, target):
    """
    遍历一遍字典
    :param arr:
    :param target:
    """
    map = {}
    for i in range(len(arr)):

        j = map.get(target-arr[i])
        if j != i and j != None:
            return [j, i]
        map[arr[i]] = i


if __name__ == '__main__':
    nums = [2,7,11,15]
    print(twoSum1(nums, 9))
    print(twoSum2(nums, 9))
    arr = [3,3]
    print(twoSum2(arr, 6))
    print(twoSum3(arr, 6))
