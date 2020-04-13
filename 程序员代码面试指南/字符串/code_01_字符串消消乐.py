#coding:utf-8
'''
@Time: 2020/4/13 11:39
@author: Tokyo
@file: code_01_字符串消消乐.py
@desc:
消除连续重复次数大于2 的字符，消除后的字符串继续消除
返回最后的字符串

比如：
aabbbaddc
输出:  ddc
'''


def delete(strs):
    if strs is None or strs == '':
        return
    stack = []

    for i in strs:
        if  stack != [] and stack[-1][0] == i and stack[-1][1]>= 2:
            stack.pop()
            continue
        if stack == [] or stack[-1][0] != i:
            stack.append([i,1])
        else:
            stack[-1][1] += 1
    res = ''
    for i in stack:
        res += i[0]*i[1]

    return res

if __name__ == '__main__':
    strs = 'abbbccdddcaae'
    print(delete(strs))