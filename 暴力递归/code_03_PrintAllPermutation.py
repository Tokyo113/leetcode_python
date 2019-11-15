#coding:utf-8
'''
@Time: 2019/11/15 15:11
@author: Tokyo
@file: code_03_PrintAllPermutation.py
@desc:
'''

def printAllPermutation(strs):
    if len(strs) == 1:
        return [strs]

    res = []
    # 去重
    visit = [False for i in range(26)]
    for i in range(len(strs)):
        # 若已经当过头，就不考虑
        if not visit[ord(strs[i])-ord('a')]:
            visit[ord(strs[i]) - ord('a')] = True
            others = strs[:i]+strs[i+1:]
            new = strs[i:i+1]
            p = printAllPermutation(others)
            for ele in p:
                res.append(new+ele)
    return res










if __name__ == '__main__':
    a = 'hello'
    c = 'abcde'
    b = printAllPermutation(a)
    print(b)
    print(len(printAllPermutation(c)))



