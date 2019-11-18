#coding:utf-8
'''
@Time: 2019/11/15 11:44
@author: Tokyo
@file: code_02_PrintAllSubsequence.py
@desc:
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



if __name__ == '__main__':
    a = 'abc'
    b = printAllSubsequence(a)
    print(b)
    print(quickAllSubsequence(a))
    print(ppppp(a))
