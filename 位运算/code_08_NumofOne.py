#coding:utf-8
'''
@Time: 2020/3/7 16:20
@author: Tokyo
@file: code_08_NumofOne.py
@desc:
请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def method1(n):
    '''
    不断右移，这种方法面对负数会导致死循环
    易错点
    :param n:
    :return:
    '''
    res = 0
    while n != 0:
        if n & 1 == 1:
            res += 1
        n = n >> 1
    return res

def method2(n):
    '''

    :param n:
    :return:
    '''
    cnt = 0
    while n != 0:
        rightOne = n&(~n+1)
        cnt += 1
        n = n&(~rightOne)
    return cnt

def method3(n):
    cnt = 0
    while n:
        cnt += 1
        n= n&(n-1)
        print(cnt)
    return cnt
if __name__ == '__main__':
    print(method1(8))
    # print(method2(-8))
    print(method3(-8))