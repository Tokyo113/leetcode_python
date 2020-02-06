#coding:utf-8
'''
@Time: 2019/11/15 15:11
@author: Tokyo
@file: code_03_PrintAllPermutation.py
打印一个字符串的全排列
打印一个字符串的全排列，并要求不出现重复的排列

leetcode46,47
思考为什么append后面不能直接加arr，需要重新给一个变量？
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


def allPermutation(str):
    '''
    所有全排列，带有重复值
    :param str:
    :return:
    '''

    res = []
    chs = list(str)


    def process(i):
        if i == len(str):
            print(chs)
            res.append(''.join(chs))
            return
        # 每个字符轮流当第一位，第二位。。。。
        for j in range(i,len(str)):
            chs[i], chs[j] = chs[j], chs[i]
            process(i+1)
            chs[i], chs[j] = chs[j], chs[i]
    process(0)

    return sorted(res)



def allPermutationNoRepeat(str):
    chs = list(str)
    res = []

    def process(i):
        if i == len(str):
            res.append(''.join(chs))
            return
        hasVisit = [False for i in range(26)]
        for j in range(i, len(str)):
            if not hasVisit[ord(chs[j])-ord('a')]:
                hasVisit[ord(chs[j])-ord('a')] = True
                chs[i], chs[j] = chs[j], chs[i]
                process(i+1)
                chs[i], chs[j] = chs[j], chs[i]

    process(0)

    return sorted(res)


def allPermutationArr(arr):
    '''
    数组的全排列
    :param arr:
    :return:
    '''
    if arr is None or arr == []:
        return []

    res = []

    def process(i):
        if i == len(arr):
            res.append(arr.copy())
            return

        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            process(i+1)
            arr[i], arr[j] = arr[j], arr[i]

    process(0)
    return res



if __name__ == '__main__':
    a = 'hello'
    c = 'ab'
    allPermutation(c)
    arr = [1,2,3]
    print(allPermutationArr(arr))





