#coding:utf-8
'''
@Time: 2020/2/27 10:49
@author: Tokyo
@file: code_15_ExpressionNum.py
@desc:
给定一个只由 0(假)、1(真)、&(逻辑与)、|(逻辑或)和^(异或)五种字符组成
的字符串express，再给定一个布尔值 desired。返回express能有多少种组合
方式，可以达到desired的结果。
【举例】
express="1^0|0|1"，desired=false
只有 1^((0|0)|1)和 1^(0|(0|1))的组合可以得到 false，返回 2。
express="1"，desired=false
无组合则可以得到false，返回0
'''


def numStr(exp, desired):
    if exp is None or exp == '':
        return 0
    if not isvalid(exp):
        return 0
    if desired != True and desired != False:
        return 0

    return process(exp, desired, 0, len(exp)-1)

def isvalid(str):
    if len(str)%2 == 0:
        return False
    for i in range(0, len(str), 2):
        if str[i] != '1' and str[i] != '0':
            return False

    for i in range(1, len(str), 2):
        if str[i] != '&' and str[i] != '^' and str[i] != '|':
            return False
    return True


def process(exp, desired, L, R):
    '''
    范围上尝试，返回在L~R范围上实现desired的方法数
    :param exp:
    :param desired:
    :param L:
    :param R:
    :return:
    '''
    if L == R:
        if exp[L] == '1':
            return 1 if desired else 0
        else:
            return 1 if not desired else 0

    res = 0
    for i in range(L+1, R, 2):
        if exp[i] == '&':
            if desired:
                res += process(exp, True, L, i-1)*process(exp,True, i+1, R)
            else:
                res += process(exp, False, L, i-1) * process(exp,False, i+1, R)
                res += process(exp, False, L, i - 1) * process(exp, True, i + 1, R)
                res += process(exp, True, L, i - 1) * process(exp, False, i + 1, R)

        elif exp[i] == '^':
            if desired:
                res += process(exp, False, L, i - 1) * process(exp, True, i + 1, R)
                res += process(exp, True, L, i - 1) * process(exp, False, i + 1, R)
            else:
                res += process(exp, False, L, i - 1) * process(exp, False, i + 1, R)
                res += process(exp, True, L, i - 1) * process(exp, True, i + 1, R)
        else:  # or
            if desired:
                res += process(exp, True, L, i - 1) * process(exp, True, i + 1, R)
                res += process(exp, True, L, i - 1) * process(exp, False, i + 1, R)
                res += process(exp, False, L, i - 1) * process(exp, True, i + 1, R)
            else:
                res += process(exp, False, L, i - 1) * process(exp, False, i + 1, R)
    return res

def numDP(exp, desired):
    if exp == '' or exp is None:
        return 0
    if not isvalid(exp):
        return 0
    n = len(exp)
    dpTrue = [[0 for i in range(n)] for i in range(n)]
    dpFalse = [[0 for i in range(n)] for i in range(n)]
    for i in range(0, n, 2):
        dpTrue[i][i] = 1 if str[i] == '1' else 0
        dpFalse[i][i] = 1 if str[i] == '0' else 0
    # i j 要保证是数字0和1的位置，所以步长是2
    for i in range(n-3, -1, -2):
        for j in range(i+2, n, 2):
            for k in range(i+1, j, 2):
                if str[k] == '&':
                    dpTrue[i][j] += dpTrue[i][k-1]+dpTrue[k+1][j]
                    dpFalse[i][j] += dpTrue[i][k-1]+dpFalse[k+1][j]
                    dpFalse[i][j] += dpFalse[i][k-1]+dpTrue[k+1][j]
                    dpFalse[i][j] += dpFalse[i][k-1]+dpFalse[k+1][j]

                elif str[k] == '^':
                    dpTrue[i][j] += dpTrue[i][k-1]+dpFalse[k+1][j]
                    dpTrue[i][j] += dpFalse[i][k - 1] + dpTrue[k + 1][j]
                    dpFalse[i][j] += dpTrue[i][k-1]+dpTrue[k+1][j]
                    dpFalse[i][j] += dpFalse[i][k - 1] + dpFalse[k + 1][j]

                else:
                    dpTrue[i][j] += dpTrue[i][k - 1] + dpTrue[k + 1][j]
                    dpTrue[i][j] += dpTrue[i][k - 1] + dpFalse[k + 1][j]
                    dpTrue[i][j] += dpFalse[i][k - 1] + dpTrue[k + 1][j]
                    dpFalse[i][j] += dpFalse[i][k - 1] + dpFalse[k + 1][j]

    return dpTrue[0][n-1] if desired else dpFalse[0][n-1]




if __name__ == '__main__':
    str =  "1^0&0|1&1^0&0^1|0|1&1"
    desired = True
    print(numStr(str, desired))
    print(numDP(str, desired))
