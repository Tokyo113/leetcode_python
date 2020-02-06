#coding:utf-8
'''
@Time: 2019/11/15 11:44
@author: Tokyo
@file: code_02_PrintAllSubsequence.py
@desc:
打印一个字符串的全部子序列，包括空字符串
ex：
'abc'
返回 ['abc', 'ab', 'ac', 'a', 'bc', 'b', 'c', '']
'''

def printAllSubsequence(strs):
    res = ''
    final = []


    def process(i, res):
        if i == len(strs):
            final.append(res)
            return
        # res是前面已经确定的数据
        keepStr = res[:]
        keepStr += strs[i]
        process(i + 1, keepStr)
        notkeep = res[:]
        process(i + 1, notkeep)


    process(0, res)

    return final




def quickAllSubsequence(strs):
    res = ['']
    for i in strs:
        res += [i+ strr for strr in res]

    return res






def findsub(str):
    strs = ''
    res = []

    def process(i, strs):
        if i == len(str):
            res.append(strs)
            return

        keepstr = strs+str[i]
        notkeepstr = strs
        process(i+1, keepstr)
        process(i+1, notkeepstr)

    process(0,strs)
    return res



if __name__ == '__main__':
    a = 'abcdef'
    b = printAllSubsequence(a)
    print(b)
    print(findsub(a))
    print(b == findsub(a))



