#coding:utf-8
'''
@Time: 2020/2/21 16:24
@author: Tokyo
@file: code_02_SubArrayMaxSum.py
@desc:
为了保证招聘信息的质量问题，公司为每个职位设计了打分系统，打分可以为正数，也
可以为负数，正数表示用户认可帖子质量，负数表示用户不认可帖子质量．打分的分数
根据评价用户的等级大小不定，比如可以为 -1分，10分，30分，-10分等。假设数组A
记录了一条帖子所有打分记录，现在需要找出帖子曾经得到过最高的分数是多少，用于
后续根据最高分数来确认需要对发帖用户做相应的惩罚或奖励．其中，最高分的定义为：
用户所有打分记录中，连续打分数据之和的最大值即认为是帖子曾经获得的最高分。例
如：帖子10001010近期的打
分记录为[1,1,-1,-10,11,4,-6,9,20,-10,-2],那么该条帖子曾经到达过的最高分数为
11+4+(-6)+9+20=38。请实现一段代码，输入为帖子近期的打分记录，输出为当前帖子
得到的最高分数。
'''


def maxSum1(arr):
    '''
    暴力解法
    :param arr:
    :return:
    '''
    if arr is None or arr == []:
        return
    res = arr[0]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            res = max(res,sum(arr[i:j]))
    return res

def maxSum2(arr):
    '''
    时间复杂度O(N),空间O(1)
    :param arr:
    :return:
    '''
    if arr is None or arr == []:
        return
    cur = 0
    maxS = float('-inf')
    for i in range(len(arr)):
        cur += arr[i]
        maxS = max(maxS, cur)
        if cur < 0:
            cur = 0
    return maxS

def maxSubArray(nums):
    '''
    时间和空间都是O(N)
    :param nums:
    :return:
    '''
    if nums is None or nums == []:
        return
    res = [0 for i in range(len(nums))]
    res[0] = nums[0]
    for i in range(1, len(nums)):
        res[i] = max(res[i - 1] + nums[i], nums[i])
    return max(res)


if __name__ == '__main__':
    a = [1,1,-1,-10,11,4,-6,9,20,-10,-2]
    print(maxSum1(a))
    print(maxSum2(a))
    print(maxSubArray(a))

    arr1 = [-2, -3, -5, 40, -10, -10, 100, 1]
    print(maxSum1(arr1))
    print(maxSum2(arr1))
    print(maxSubArray(arr1))

    arr2 = [-2, -3, -5, 0, 1, 2, -1]
    print(maxSum1(arr2))
    print(maxSum2(arr2))

    arr3 = [-2, -3, -5, -1]
    print(maxSum1(arr3))
    print(maxSum2(arr3))
    print(maxSubArray(arr3))