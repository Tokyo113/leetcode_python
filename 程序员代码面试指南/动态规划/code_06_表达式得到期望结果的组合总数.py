#coding:utf-8
'''
@Time: 2020/4/2 16:36
@author: Tokyo
@file: code_06_表达式得到期望结果的组合总数.py
@desc:
'''

def isvalid(strs):
    if len(strs)%2 == 0:
        return False
    for i in range(len(strs)):
        if i%2 ==0:
            if strs[i] != '1' and strs[i] != '0':
                return False
        else:
            if strs[i] !='&' and strs[i] !='^' and strs[i] !='|':
                return False
    return True

def expression(strs, aim):
    if strs is None or strs == '' or isvalid(strs)== False:
        return 0
    if len(strs) == 1:
        if strs == '1':
            return 1 if aim else 0
        else:
            return 1 if not aim else 0
    res = 0
    for i in range(1,len(strs), 2):
        if strs[i]=='&':
            if aim:
                res += expression(strs[:i], True)*expression(strs[i+1:],True)
            else:
                res += expression(strs[:i],True)*expression(strs[i+1:],False)
                res += expression(strs[:i],False)*expression(strs[i+1:],True)
                res += expression(strs[:i], False)*expression(strs[i+1:],False)
        elif strs[i] == '|':
            if aim:
                res += expression(strs[:i],True)*expression(strs[i+1:],False)
                res += expression(strs[:i], False) * expression(strs[i + 1:], True)
                res += expression(strs[:i], True) * expression(strs[i + 1:], True)
            else:
                res += expression(strs[:i], False) * expression(strs[i + 1:], False)
        else:
            if aim:
                res += expression(strs[:i], True) * expression(strs[i + 1:], False)
                res += expression(strs[:i], False) * expression(strs[i + 1:], True)
            else:
                res += expression(strs[:i], True) * expression(strs[i + 1:], True)
                res += expression(strs[:i], False) * expression(strs[i + 1:], False)
    return res



def expressionDP(strs,aim):
    if strs is None or strs == '' or isvalid(strs)== False:
        return 0
    if len(strs) == 1:
        if strs == '1':
            return 1 if aim else 0
        else:
            return 1 if not aim else 0
    n = len(strs)
    dpTrue = [[0 for i in range(n)] for i in range(n)]
    dpFalse = [[0 for i in range(n)] for i in range(n)]
    for i in range(0,n,2):

        dpTrue[i][i] = 1 if strs[i] == '1' else 0
        dpFalse[i][i] = 1 if strs[i] == '0' else 0
    # i 和j保证是0或者1的位置
    for i in range(n-3,-1,-2):
        for j in range(i+2,n,2):
            for k in range(i+1,j,2):
                if strs[k] == '&':
                    dpTrue[i][j] += dpTrue[i][k-1]*dpTrue[k+1][j]
                    dpFalse[i][j] += dpTrue[i][k-1]*dpFalse[k+1][j]
                    dpFalse[i][j] += dpFalse[i][k - 1] * dpTrue[k + 1][j]
                    dpFalse[i][j] += dpFalse[i][k - 1] * dpFalse[k + 1][j]
                elif strs[k] == '|':
                    dpTrue[i][j] += dpTrue[i][k - 1] * dpFalse[k + 1][j]
                    dpTrue[i][j] += dpFalse[i][k - 1] * dpTrue[k + 1][j]
                    dpTrue[i][j] += dpTrue[i][k - 1] * dpTrue[k + 1][j]
                    dpFalse[i][j] += dpFalse[i][k - 1] * dpFalse[k + 1][j]
                else:
                    dpFalse[i][j] += dpTrue[i][k - 1] * dpTrue[k + 1][j]
                    dpFalse[i][j] += dpFalse[i][k - 1] * dpFalse[k + 1][j]
                    dpTrue[i][j] += dpTrue[i][k - 1] * dpFalse[k + 1][j]
                    dpTrue[i][j] += dpFalse[i][k - 1] * dpTrue[k + 1][j]
    return dpTrue[0][n-1] if aim else dpFalse[0][n-1]










if __name__ == '__main__':
    strs = '^^0&0'
    # print(isvalid(strs))
    print(expression("1^0&0|1&1^0&0^1|0|1&1",False))
    print(expressionDP("1^0&0|1&1^0&0^1|0|1&1", False))
