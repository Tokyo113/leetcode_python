#coding:utf-8
'''
@Time: 2019/12/9 22:09
@author: Tokyo
@file: code_08_RobotWalk.py
@desc:
【题目】
假设有排成一行的 N 个位置，记为 1~N，N 一定大于或等于 2。开始时机器人在其中的 M 位
置上(M 一定是 1~N 中的一个)，机器人可以往左走或者往右走，如果机器人来到 1 位置， 那
么下一步只能往右来到 2 位置;如果机器人来到 N 位置，那么下一步只能往左来到 N-1 位置。
规定机器人必须走 K 步，最终能来到 P 位置(P 也一定是 1~N 中的一个)的方法有多少种。给
定四个参数 N、M、K、P，返回方法数。
【举例】
N=5,M=2,K=3,P=3
上面的参数代表所有位置为 1 2 3 4 5。机器人最开始在 2 位置上，必须经过 3 步，最后到
达 3 位置。走的方法只有如下 3 种: 1)从2到1，从1到2，从2到3 2)从2到3，从3到2，从2到3
3)从2到3，从3到4，从4到3
所以返回方法数 3。 N=3,M=1,K=3,P=3
上面的参数代表所有位置为 1 2 3。机器人最开始在 1 位置上，必须经过 3 步，最后到达 3
位置。怎么走也不可能，所以返回方法数 0。

'''


def robot1(N, E, K, S):
    return f1(N, E, K, S)
def f1(N, E, rest, cur):
    '''
    暴力递归
    :param N: 固定参数，N个位置
    :param E: 固定参数，最终目标
    :param rest: 剩余的步数
    :param cur: 当前已经来到s位置
    :return:
    '''
    if rest == 0:
        return 1 if cur == E else 0

    if cur == 1:
        return f1(N, E, rest-1, 2)
    elif cur == N:
        return f1(N,E,rest-1,N-1)
    else:
        return f1(N, E, rest-1, cur-1) + f1(N, E, rest-1, cur+1)


def robot2(N,E, K,S):
    dp = [[-1 for i in range(N+1)]for i in range(K+1)]
    return f2(N, E, K, S, dp)

def f2(N, E, rest, cur, dp):
    if dp[rest][cur] != -1:
        return dp[rest][cur]
    if rest == 0:
        dp[rest][cur] = 1 if cur == E else 0
        return dp[rest][cur]
    if cur == 1:
        dp[rest][cur] = f2(N, E, rest-1, 2, dp)
    elif cur == N:
        dp[rest][cur] = f2(N, E, rest-1, N-1,dp)
    else:
        dp[rest][cur] = f2(N, E, rest-1, cur-1, dp) + f2(N, E, rest-1, cur+1, dp)

    return dp[rest][cur]

def robot3(N,E,K,S):
    '''

    :param N: N个位置
    :param E: 最后要到达的位置
    :param K: 给定步数
    :param S: 当前位置
    :return:
    '''
    dp = [[0 for i in range(N+1)] for i in range(K+1)]
    dp[0][E] = 1
    for rest in range(1,K+1):
        for cur in range(1,N+1):
            if cur == 1:
                dp[rest][cur] = dp[rest-1][2]
            elif cur == N:
                dp[rest][cur] = dp[rest-1][N-1]
            else:
                dp[rest][cur] = dp[rest-1][cur-1]+dp[rest-1][cur+1]

    return dp[K][S]



def robot(n,M,K,P):
    dp = [[0 for i in range(K+1)] for i in range(n+1)]
    dp[P][0] = 1
    for j in range(1,K+1):
        for i in range(1,n+1):
            if i == 1:
                dp[i][j] = dp[i+1][j-1]
            elif i == n:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i+1][k-1]+dp[i-1][k-1]
    return dp[M][K]%(10**9+7)








if __name__ == '__main__':
    print(robot1(9,4,5,3))
    print(robot2(9, 4, 5, 3))
    print(robot3(9,4,5,3))
    print(robot3(9,3,4,5))
    print(robot(9,4,5,3))



