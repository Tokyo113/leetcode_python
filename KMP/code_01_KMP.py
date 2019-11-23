#coding:utf-8
'''
@Time: 2019/11/22 16:27
@author: Tokyo
@file: code_01_KMP.py
@desc:
KMP算法解决的问题
字符串str1和str2，str1是否包含str2，如果包含返回str2在str1中开始的位置。
如何做到时间复杂度O(N)完成？
'''


def KMP(s,m):
    if s == None or m == None or len(m) < 1 or len(m) > len(s):
        return -1

    i1, i2 = 0, 0
    next = getNextArray(m)

    while i1 < len(s) and i2 < len(m):
        if s[i1] == m[i2]:
            i1 += 1
            i2 += 1
        else:
            if next[i2] == -1:
                i1 += 1
            else:
                i2 = next[i2]

    return i1-i2 if i2 ==len(m) else -1


def getNextArray(m):
    if len(m) == 1:
        return [-1]

    next = [0 for i in range(len(m))]
    next[0] = -1
    next[1] = 0
    i = 2
    cn = 0   # 拿哪个位置字符和i-1比较，i = 2时用0位置和2的前一个比较
    while i < len(next):
        if m[i-1] == m[cn]:
            next[i] = cn + 1
            i += 1
            cn += 1
        else:
            if cn > 0:
                cn = next[cn]
            else:
                next[i] = 0
                i += 1
    return next








if __name__ == '__main__':
    a = 'sdfjhweofwkdfndvmnve'
    b = 'dfndvmnve'
    index = KMP(a,b)
    print(index)
