#coding:utf-8
'''
@Time: 2019/11/22 16:27
@author: Tokyo
@file: code_01_KMP.py
@desc:
KMP算法解决的问题
字符串str1和str2，str1是否包含str2，如果包含返回str2在str1中开始的位置。
如何做到时间复杂度O(N)完成？

cn值有两个含义
1.目前拿哪个位置的字符和i-1位置比较
2.cn也是i-1位置在next数组中的值
'''


def KMP(s,m):
    if s == None or m == None or len(m) < 1 or len(m) > len(s):
        return -1

    i1, i2 = 0, 0
    next = getNextArray(m)
    # 复杂度O(N)
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





def kmppp(a,b):
    if a is None or b is None or len(a)<len(b):
        return -1
    i1, i2 = 0, 0
    record = getNextarr(b)
    while i1 < len(a) and i2 < len(b):
        if a[i1] == b[i2]:
            i1 += 1
            i2 += 1
        else:
            if i2 == 0:
                i1 += 1
            else:
                i2 = record[i2]
    return  i1-i2 if i2 == len(b) else -1

def getNextarr(s):
    if len(s) == 1:
        return [-1]
    arr = [0 for i in range(len(s))]
    arr[0] = -1
    arr[1] = 0
    i = 2
    cn = 0
    while i < len(s):
        if s[i-1] == s[cn]:
            arr[i] = cn+1
            cn += 1
            i+= 1
        else:
            if cn > 0:
                cn = arr[cn]
            else:
                i += 1
    return arr

def manacher(s):
    if s is None or s == '':
        return 0
    strs = '1'+'1'.join(s)+'1'
    R = -1
    C = -1
    pArr = [0 for i in range(len(strs))]

    for i in range(len(pArr)):
        pArr[i] = min(R-i, pArr[2*C-i]) if i < R else 1

        while i+pArr[i] < len(strs) and i - pArr[i] >= 0:
            if strs[i+pArr[i]] ==strs[i-pArr[i]]:
                pArr[i] += 1
            else:
                break

        if i + pArr[i] >R:
            R = i+pArr[i]
            C = i
    return max(pArr)-1





if __name__ == '__main__':
    a = 'sdfjhweo1fwkdfndvmnve'
    b = '1fwkdfndv'
    c = '12343256787'
    index = KMP(a,b)
    print(index)
    print(kmppp(a,b))
    print(manacher(c))


