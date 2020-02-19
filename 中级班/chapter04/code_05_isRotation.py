#coding:utf-8
'''
@Time: 2020/2/16 15:17
@author: Tokyo
@file: code_05_isRotation.py
@desc:
如果一个字符串为str，把字符串str前面任意的部分挪到后面形成的字符串叫
作str的旋转词。比如str="12345"，str的旋转词有"12345"、"23451"、
"34512"、"45123"和"51234"。给定两个字符串a和b，请判断a和b是否互为旋转
词。
比如：
a="cdab"，b="abcd"，返回true。
a="1ab2"，b="ab12"，返回false。
a="2ab1"，b="ab12"，返回true。

总体思路：
判断b是否是a+a的子字符串即可
因为a+a包含了所有可能的旋转字符串
'''

def isRotation(str1, str2):
    '''
    奇技淫巧，python直接判断子串
    :param str1:
    :param str2:
    :return:
    '''
    if len(str1) != len(str2) or str1 is None or str2 is None:
        return False
    return True if str2 in str1+str1 else False


def isRotation1(a, b):
    '''
    使用KMP算法判断子串
    :param a:
    :param b:
    :return:
    '''
    if len(a) != len(b) or a is None or b is None:
        return False
    return True if KMP(a+a, b) != -1 else False


def KMP(a, b):
    '''
    判断b是否是a的子串，并返回子串在a中的起始index
    否则返回-1
    :param a:
    :param b:
    :return:
    '''
    if a is None or b is None or len(b)>len(a):
        return -1
    i1, i2 = 0, 0
    record = getNextArr(b)

    while i1 < len(a) and i2 < len(b):
        if a[i1] == b[i2]:
            i1 += 1
            i2 += 1
        else:
            if i2 == 0:
                i1 += 1
            else:
                i2 = record[i2]

    return i1-i2 if i2 == len(b) else -1

def getNextArr(str):
    if len(str) == 1:
        return [-1]
    res = [-1 for i in range(len(str))]
    res[1] = 0
    i = 2
    cn = 0
    while i < len(str):
        if str[i-1] == str[cn]:
            res[i] = cn+1
            cn += 1
            i += 1
        else:
            if cn > 0:
                cn = res[cn]
            else:
                res[i] = 0
                i += 1
    return res


if __name__ == '__main__':
    a = '12345'
    b = '51234'
    c = '23451'
    d = '42315'
    print(isRotation1(a, c))
