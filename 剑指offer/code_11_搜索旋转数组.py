#coding:utf-8
'''
@Time: 2020/4/13 11:19
@author: Tokyo
@file: code_11_搜索旋转数组.py
@desc:  leetcode33
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


和原始问题类似，
先找到旋转点，再二分查找
'''


def search(nums, aim):
    if nums is None or nums == []:
        return -1
    L, R = 0, len(nums) - 1
    rotateIndex = L
    while L < R:
        mid = (L + R) // 2
        if R == L + 1:
            rotateIndex = R
            break
        if nums[mid] >= nums[L]:
            L = mid
        elif nums[mid] <= nums[R]:
            R = mid

    if len(nums) == 1 or nums[0] < nums[-1]:
        rotateIndex = 0
    print(rotateIndex)
    if aim == nums[rotateIndex]:
        return rotateIndex
    elif aim < nums[rotateIndex]:
        return -1

    def findAim(arr, aim):
        if arr is None or arr == []:
            return -1

        L, R = 0, len(arr) - 1
        while L < R:
            mid = (L + R) // 2
            if arr[mid] > aim:
                R = mid - 1
            elif arr[mid] < aim:
                L = mid + 1
            else:
                return mid
        return L if arr[L] == aim else -1

    i1 = findAim(nums[:rotateIndex], aim)
    i2 = findAim(nums[rotateIndex:], aim)
    print(i1,i2)
    return i1 if i1 != -1 else (rotateIndex+i2 if i2 != -1 else -1)


if __name__ == '__main__':
    arr = [4,5,6,7,0,1,2]
    print(search(arr,3))