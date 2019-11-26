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

    # strs = manacherString(s)
    strs = '#'+'#'.join(s)+'#'
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
            # 有更大的回文子串，更新R和C
            R = i + pArr[i]
            C = i

        maxP = max(maxP, pArr[i])

    return maxP-1




def manaccc(s):
    """
    返回最长回文字符串  leetcode 5
    :param s:
    :return:
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

    示例 1：

    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。
    示例 2：

    输入: "cbbd"
    输出: "bb"

    """
    if s == None or len(s) == 0:
        return 0

    strs = '#'+"#".join(s)+'#'
    pArr = [1 for i in range(len(strs))]
    R = -1
    C = -1
    maxIndex = 0

    for i in range(len(strs)):
        pArr[i] = min(pArr[2*C-i], R-i) if i <= R else 1

        while i+pArr[i] < len(strs) and i - pArr[i] > -1:
            if strs[i + pArr[i]] == strs[i-pArr[i]]:
                pArr[i] += 1
            else:
                break

        if i + pArr[i] > R:
            R = i + pArr[i]
            C = i

    maxP = 0
    for i in range(len(strs)):
        if pArr[i] > maxP:
            maxIndex = i
            maxP = pArr[i]

    return "".join(strs[maxIndex-pArr[maxIndex]+1:maxIndex+pArr[maxIndex]].split("#"))


def manacher(s):
    if s == None or len(s)== 0:
        return 0

    new = '#'+"#".join(s)+"#"
    pArr = [1 for i in range(len(new))]
    R = -1
    C = -1
    maxP = 0

    for i in range(len(new)):

        pArr[i] = min(pArr[2*C-i], R-i) if i < R else 1

        while i + pArr[i] < len(new) and i - pArr[i] > -1:
            if new[i+pArr[i]] == new[i-pArr[i]]:
                pArr[i] += 1
            else:
                break

        if i + pArr[i] > R:
            R = i + pArr[i]
            C = i

        maxP = max(maxP, pArr[i])


    return maxP-1


if __name__ == '__main__':
    a = 'abc1234321cb'
    print(manacherString(a))
    print(maxLcpsLength(a))
    print(manacher(a))

    print(manaccc(a))
    b = 'babad'
    print(maxLcpsLength(b))
    print(manaccc(b))
    print(manacher(b))