#coding:utf-8
'''
@Time: 2020/2/25 11:24
@author: Tokyo
@file: code_04_DivideBy3.py
@desc:
小K得到一法个扩神展奇题的目数二列: 1, 12, 123,...12345678910,1234567891011...。
并且小Q对于能否被3整除这个性质很感兴趣。
小Q现在希望你能帮他计算一下从数列的第l个到第r个(包含端点)有多少个数可以被3整除。
输入描述：
输入包括两个整数l和r(1 <= l <= r <= 1e9), 表示要求解的区间两端。
输出描述：
输出一个整数, 表示区间内能被3整除的数字个数。
示例1:
输入
2 5
输出
3
'''


def divideBy3(l,r):
    if l <=0 or r<= 0 or l>r:
        return 0
    cnt = 0
    for i in range(l,r+1):
        tmp = (i*(i+1))/2


        if tmp % 3 == 0:
            cnt += 1
    return cnt


if __name__ == '__main__':
    print(divideBy3(2,5))