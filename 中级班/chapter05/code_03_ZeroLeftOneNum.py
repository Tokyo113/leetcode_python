#coding:utf-8
'''
@Time: 2020/2/19 16:05
@author: Tokyo
@file: code_03_ZeroLeftOneNum.py
@desc:
字符串只由'0'和'1'两种字符构成，
当字符串长度为1时，所有可能的字符串为"0"、"1"；
当字符串长度为2时，所有可能的字符串为"00"、"01"、"10"、"11"；
当字符串长度为3时，所有可能的字符串为"000"、"001"、"010"、"011"、"100"、
"101"、"110"、"111"
... 如果某一个字符串中，只要是出现'0'的位置，左边就靠着'1'，这样的字符串叫作达
标字符串。
给定一个正数N，返回所有长度为N的字符串中，达标字符串的数量。
比如，N=3，返回3，因为只有"101"、"110"、"111"达标。
1,2,3,5,......斐波那契数列
'''

def getNum(n):
    '''
    1.直接理解为斐波那契
    2.假设这个函数返回左边为1的情况下，长度为n的达标字符串的个数
    :param n:
    :return:
    '''
    if n == 1:
        return 1
    if n == 2:
        return 2
    return getNum(n-1)+getNum(n-2)


def getnum2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    arr = [[1,1,], [1,0]]
    pp = matrixPower(arr, n-2)
    return 2*pp[0][0]+pp[1][0]

def matrixPower(arr, n):
    res = [[0 for i in range(len(arr))] for i in range(len(arr))]
    for i in range(len(arr)):
        res[i][i] = 1
    t = arr
    while n !=0:
        if n&1 == 1:
            res = matrixMultiple(res, t)
        t = matrixMultiple(t,t)
        n = n >>1

    return res


def matrixMultiple(a, b):
    if len(a[0]) != len(b):
        print("Dimension error")
        return
    res = [[0 for i in range(len(b[0]))] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k]*b[k][j]

    return res


if __name__ == '__main__':
    print(getNum(14))
    print(getnum2(14))