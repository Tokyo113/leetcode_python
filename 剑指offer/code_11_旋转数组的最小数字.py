#coding:utf-8
'''
@Time: 2020/4/13 10:10
@author: Tokyo
@file: code_11_旋转数组的最小数字.py
@desc:
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
注意可能有相同值

变式题：
1：leetcode33
'''


def rotateArr(arr):
    if arr is None or arr == []:
        return
    # 注意各种情况，若没有发生旋转
    if len(arr) == 1:
        return arr[0]
    if arr[0]<arr[-1]:
        return arr[0]
    # 保证L指针永远在左半区域，
    # R永远在右半区域
    L,R = 0, len(arr)-1
    midIndex = L
    while L<R:
        mid = (L+R)//2
        # 当两者相差一时，说明R来到了右半区的最左位置
        if R == L+1:
            midIndex = R
            break
        if arr[mid] == arr[L] and arr[mid] == arr[R]:
            return min(arr[L:R+1])
        if arr[mid]>=arr[L]:
            L = mid
        elif arr[mid]<=arr[R]:
            R = mid


    return arr[midIndex]


if __name__ == '__main__':
    arr = [1,1,1,0,1]
    print(rotateArr(arr))


