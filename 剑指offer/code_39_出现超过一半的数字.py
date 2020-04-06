#coding:utf-8
'''
@Time: 2020/4/3 21:43
@author: Tokyo
@file: code_39_出现超过一半的数字.py
@desc:
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

 

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
 

限制：

1 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


最优解：实现O(N)的解法
'''


def majorityElement(nums):
    if nums is None or nums == []:
        return

    def partition(arr, L, R):
        if arr is None or arr == []:
            return
        aim = arr[R]
        less, more = L - 1, R + 1
        cur = L
        while cur < more:
            if nums[cur] < aim:
                arr[cur], arr[less + 1] = arr[less + 1], arr[cur]
                less += 1
                cur += 1
            elif nums[cur] == aim:
                cur += 1
            else:
                arr[cur], arr[more - 1] = arr[more - 1], arr[cur]
                more -= 1
        return less + 1, more - 1

    L, R = 0, len(nums)-1
    p = partition(nums, L, R)
    while L <= R:
        print(nums)
        if p[0] <= len(nums) // 2 and len(nums) // 2 <= p[1]:
            return nums[p[0]]
        elif len(nums) // 2 > p[1]:
            L = p[1] + 1
        else:
            R = p[0] - 1
        p = partition(nums, L, R)


if __name__ == '__main__':
    arr = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(arr)
    print('---')
    print(majorityElement(arr))
