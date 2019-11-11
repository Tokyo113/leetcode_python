#coding:utf-8
'''
@Time: 2019/11/11 14:39
@author: Tokyo
@file: code_03_LowestLexicography.py
@desc:
'''

import functools
def comparator(a, b):
    """
    比较合并后的字典序
    :param a:
    :param b:
    :return:
    """
    if a+b > b+a:
        return 1
    elif a + b < b + a:
        return -1
    else:
        return 0

def lowestString(strs):
    if strs is None or len(strs) == 0:
        return ""
    # strs = sorted(strs, key=functools.cmp_to_key(comparator))
    strs.sort(key=functools.cmp_to_key(comparator))
    res = ""
    for i in range(len(strs)):
        res += strs[i]
    return res



import itertools
def baoli(strs):
    str_sort = []
    # 字符串列表全排列
    for i in itertools.permutations(strs, len(strs)):
        # 连接字符串
        str_sort.append(''.join(i))
    str_sort.sort()
    return str_sort[0]


def perm(strs):
    if(len(strs)<=1):
        return [strs]
    res = []
    for i in range(len(strs)):
        s = strs[:i] + strs[i + 1:]
        # 对剩余元素全排列
        p = perm(s)
        for x in p:
            res.append(strs[i:i + 1] + x)
    return res

def method1(strs):
    all_str = perm(strs)
    str = []
    for i in all_str:
        str.append(''.join(i))
    str.sort()
    return str[0]



if __name__ == '__main__':

    strs1 = ["jibw", "ji", "jp", "bw", "jibw"]
    print(lowestString(strs1))

    strs2 = ["ba", "b"]
    print(lowestString(strs2))
    print(baoli(strs1))
    print(method1(strs1))