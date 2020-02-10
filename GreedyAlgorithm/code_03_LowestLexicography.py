#coding:utf-8
'''
@Time: 2019/11/11 14:39
@author: Tokyo
@file: code_03_LowestLexicography.py
@desc:
给定一个字符串类型的数组strs，找到一种拼接方式，使得把所有字符串拼起来之后形成的
字符串具有最小的字典序。
'''

import functools
def comparator(a, b):
    """
    自定义比较函数，升序排列a在前（a<b）就返回-1，b在前就返回1
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
    return ''.join(strs)

import itertools

def baoli(strs):
    str_sort = []
    # 字符串列表全排列
    for i in itertools.permutations(strs, len(strs)):
        # 连接字符串
        str_sort.append(''.join(i))
    str_sort.sort()
    return str_sort[0]

'''
全排列的思路：
[1,2,3,4,5]
外循环：
    第一个位置为1+剩余部分的全排列
    第一个位置为2+剩余部分的全排列
    。。。
    第一个位置为5+剩余部分的全排列
全排列函数返回一个大列表[[2,3,4,5], [2,3,5,4], [2,4,3,5], ...]
然后1与其中的每个小列表拼接就返回最后的结果

'''
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


def quanpailie(strs):
    # base case
    if len(strs) == 1:
        return [strs]
    res = []
    for i in range(len(strs)):
        others = strs[0:i] + strs[i+1:]
        p = quanpailie(others)
        for x in p:
            res.append(strs[i:i+1]+x)
    return res










if __name__ == '__main__':

    strs1 = ["jibw", "ji", "jp", "bw", "jibw"]
    print(lowestString(strs1))
    print(baoli(strs1))
    print('===')

    strs2 = ["ba", "b"]
    print(lowestString(strs2))
    print(baoli(strs1))
    print(method1(strs1))




