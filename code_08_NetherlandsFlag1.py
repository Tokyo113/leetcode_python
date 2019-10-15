#coding:utf-8
'''
@Time: 2019/10/11 16:32
@author: Tokyo
@file: code_08_NetherlandsFlag1.py
@desc:
'''

"""
给定一个数组arr 和一个数num,请把小于等于num的数放在数组的左边，
大于num的数放在数组的右边，要求额外空间复杂度O(1), 时间复杂度O(N)
"""

def method1(arr, num):
    """
    利用双指针，一次遍历完成
    与方法二相比，相当于定义了一个大于区域
    :param arr:
    :param num:
    """
    i = 0
    j = len(arr)-1
    # 两指针相遇，循环退出
    while (i < j):

            if arr[i] > num:
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
            else:
                i += 1
    return arr


def method2(arr, num):
    """
    定义x，[0,x]表示小于等于num的区域，起始x=-1,指针i遍历元素
    ele <= num, arr[i] 和x区域的下一个元素互换，x区域扩大一个， i++
    ele > num , i ++
    为什么要和x区域的下一个元素交换？
    下一个元素>num:
    下一个元素<num:相当于和自身交换，不变
    :param arr:
    :param num:
    """
    x = -1
    for i in range(0, len(arr)):
        if arr[i] < num:
            arr[x+1], arr[i] = arr[i], arr[x+1]
            x += 1



if __name__ == '__main__':
    a = [4,7,5,3,1,8,45,25,66,78,100]
    num = 20
    # method1(a, num)
    method2(a, num)
    print(a)