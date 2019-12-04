#coding:utf-8
'''
@Time: 2019/12/4 21:54
@author: Tokyo
@file: code_01_EvenTimesOddTimes.py
@desc:

1.一个数组中有一种数出现了奇数次，其他数都出现了偶数次，怎么找到这一个数
2.一个数组中有两种数出现了奇数次，其他数都出现了偶数次，怎么找到这两个数
'''

def findOddTimes1(arr):
    eor = 0
    for i in arr:
        eor = eor ^ i

    return eor


def findOddTimes2(arr):
    eor = 0
    for i in arr:
        eor = eor ^ i

    # eor = a ^ b
    # 取得eor最右侧的1，eor肯定不为0，存在一位为1
    # 这两个数肯定在这一位不一样，一个为1，一个为0
    rightone = eor & (~eor+1)
    eor1 = 0

    for i in arr:
        if (i&rightone) == 0:
            eor1 = eor1 ^ i
    return eor1, eor1^eor




if __name__ == '__main__':
    a = [1,2,3,2,1,2,4,4,3,2,3]
    print(findOddTimes1(a))
    b = [4, 3, 4, 2, 2, 2, 4, 1, 1, 1, 3, 3, 1, 1, 1, 4, 2, 2]
    print(findOddTimes2(b))