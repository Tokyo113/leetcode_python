#coding:utf-8
'''
@Time: 2020/3/14 21:54
@author: Tokyo
@file: code_03_findNthDigit.py
@desc:
和上一题类似哦
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

 

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
思路：

找规律：
0~9         10个,10位
10~99       90个，180位
100~999     900个，2700位
1000~9999   9000个

先判断是几位数，
'''


def f(n):
    '''
    返回n位数有多少个
    :param n:
    :return:
    '''
    if n == 1:
        return 10
    return 9*(10**(n-1))*n



def findNth(n):
    if n<0:
        return -1
    p = n
    i = 1
    while p>=0:
        p -= f(i)
        i += 1
    digit = i-1
    print(digit)
    num = p+f(digit)
    a = num//digit
    b = num%digit
    if digit == 1:
        return a
    res = str(10**(digit-1)+a)

    return int(res[b])






if __name__ == '__main__':
    print(findNth(10))