#coding:utf-8
'''
@Time: 2020/3/21 10:21
@author: Tokyo
@file: code_04_minSumofSubArr.py
@desc:
给定一个整数数组 A，找到 min(B) 的总和，其中 B 的范围为 A 的每个（连续）子数组。

由于答案可能很大，因此返回答案模 10^9 + 7。



示例：

输入：[3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。


'''


def sumSubarrayMins(A):
    '''
    暴力解法，超内存
    :param A:
    :return:
    '''
    if A is None or A == []:
        return

    res = []
    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            res.append(A[i:j])

    cnt = 0
    for i in res:
        if i != []:
            cnt += min(i)

    return cnt % (10 ** 9 + 7)

def sumSubarrayMins2(A):
    if A is None or A == []:
        return

    stack = []
    info = [[-1, len(A)] for i in range(len(A))]
    for i in range(len(A)):
        while stack != [] and A[i] < A[stack[-1]]:
            ele = stack.pop()
            info[ele][1] = i
            info[ele][0] = stack[-1] if stack != [] else -1
        stack.append(i)

    while stack != []:
        ele = stack.pop()
        info[ele][0] = stack[-1] if stack != [] else -1

    res = 0
    for i in range(len(info)):
        res += A[i] * (i - info[i][0]) * (info[i][1] - i)
    print(info)
    return res % ((10 ** 9) + 7)


if __name__ == '__main__':
    print(sumSubarrayMins([3,1,2,4]))
    print(sumSubarrayMins2([48,87,27]))