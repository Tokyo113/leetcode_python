#coding:utf-8
'''
@Time: 2020/2/14 10:21
@author: Tokyo
@file: code_07_SplitNBySM.py
@desc:
假设s和m初始化，s = "a"; m = s;
再定义两种操作，第一种操作：
m = s;
s = s + s;
第二种操作：
s = s + m;
求最小的操作步骤数，可以将s拼接到长度等于n

思路：
判断是否是质数
1.n是质数，只需要调用操作二n-1次
2.n不是质数，将n分解为质数因子相乘，最后答案是质数因子相加减去因子的个数
n=a*b*c*d, ans = a+b+c+d-4
'''
import math
def isPrim(n):
    '''
    判断是否是质数
    :param n:
    :return:
    '''
    if n < 2:
        return False
    v = math.sqrt(n)
    for i in range(2, int(v+1)):
        if n % i == 0:
            return False
    return True


def getPrimandSum(n):
    sum = 0
    cnt = 0
    for i in range(2, n+1):
        while n%i == 0:
            sum += i
            cnt += 1
            n /= i

    return sum, cnt




def splitNBySM(n):
    if n < 2:
        return 0
    if isPrim(n):
        return n-1
    ans = getPrimandSum(n)
    return ans[0]-ans[1]

if __name__ == '__main__':
    print(isPrim(4))
    print(splitNBySM(5555555))
