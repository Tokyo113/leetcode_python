#coding:utf-8
'''
@Time: 2019/11/13 20:35
@author: Tokyo
@file: code_07_NQueens.py
@desc:
Leetcode51
leetcode52
N皇后问题是指在N*N的棋盘上要摆N个皇后，要求任何两个皇后不同行、不同列，
也不在同一条斜线上。
给定一个整数n，返回n皇后的摆法有多少种。
n=1，返回1。
n=2或3，2皇后和3皇后问题无论怎么摆都不行，返回0。
n=8，返回92
'''
'''
record:
index表示行数
ele表示第几列有queen
record[1] = 1 表示第一行第一列有queen
'''
final = []
def nQueens(n):
    if n < 1:
        return 0

    record = [0 for i in range(n)]
    result = process(0,record, n)

    return result

def process(i, record,n):
    if i == n:
        convert(record)
        return 1
    res = 0
    for j in range(n):
        if isvalid(i, record, j):
            record[i] = j
            res += process(i+1, record, n)
    return res


def isvalid(i, record, j):

    for k in range(i):
        if j == record[k] or (abs(j-record[k]) == abs(i-k)):
            return False

    return True

def convert(record):
    global final
    li = []

    for j in range(len(record)):
        strs = ''
        for i in range(len(record)):
            if i == record[j]:
                strs += 'Q'
            else:
                strs += '.'
        li.append(strs)
    final.append(li)

class Solution():
    def nqueen(self,n):
        if n < 1:
            return 0

        record = [0 for i in range(n)]
        res = self.process(0, record, n)

        return res


    def process(self,i, record, n):
        if i == n:
            return 1
        res = 0
        for j in range(n):
            if self.isvalid(i,record, j):
                record[i] = j
                res += self.process(i+1, record,n)
        return res


    def isvalid(self,i, record, j):
        for k in range(i):
            if record[k] == j or abs(record[k]-j) == abs(i-k):
                return False
        return True



def nhuanghou(n):
    if n <= 0:
        return 0
    record = [0 for i in range(n)]


    def process1(i):
        if i == n:
            return 1
        res = 0
        for j in range(n):
            if canbe(record, i, j):
                record[i] = j
                res += process1(i+1)
        return res


    return process1(0)
def canbe(record, i, j):
    for k in range(i):
        if record[k] == j or abs(j-record[k]) == abs(i-k):
            return False
    return True





if __name__ == '__main__':
    print(nQueens(5))
    # print(final)
    # a = Solution()
    # print(a.nqueen(8))
    print(nhuanghou(5))
