#coding:utf-8
'''
@Time: 2019/11/23 16:13
@author: Tokyo
@file: code_02_Manacher.py
@desc:
'''

def manacherString(s):
    res = ['' for i in range(2*len(s)+1)]
    index = 0
    for i in range(len(res)):
        if (i & 1) == 0:
            res[i] = '#'
        else:
            res[i] = s[index]
            index += 1


    return res



def maxLcpsLength(s):
    if s == None or len(s) == 0:
        return 0

    strs = manacherString(s)
    # 回文半径数组
    pArr = [1 for i in range(len(strs))]
    maxP = 0
    C = -1
    R = -1
    for i in range(len(strs)):
        pArr[i] = min(pArr[2*C-i], R-i) if R > i else 1

        while i+pArr[i] < len(strs) and i-pArr[i] > -1:
            if strs[i+pArr[i]] == strs[i-pArr[i]]:
                pArr[i] += 1
            else:
                break

        if (i+pArr[i]) > R:
            R = i + pArr[i]
            C = i

        maxP = max(maxP, pArr[i])

    return maxP-1


if __name__ == '__main__':
    a = 'abc1234321ab'
    print(manacherString(a))
    print(maxLcpsLength(a))
    b = 'avcta132tba'
    print(maxLcpsLength(b))