#coding:utf-8
'''
@Time: 2019/11/13 20:35
@author: Tokyo
@file: code_07_NQueens.py
@desc:
Leetcode51
leetcode52

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



if __name__ == '__main__':
    print(nQueens(5))
    print(final)
