#coding:utf-8
'''
@Time: 2020/2/25 18:14
@author: Tokyo
@file: code_14_Kiki.py
@desc:
CC里面有一个土豪很喜欢一位女直播Kiki唱歌，平时就经常给她点赞、送礼、私聊。最近CC直播平台在举行
中秋之星主播唱歌比赛，假设一开始该女主播的初始人气值为start， 能够晋升下一轮人气需要刚好达到end，
土豪给主播增加人气的可以采取的方法有：
a. 点赞 花费x C币，人气 + 2
b. 送礼 花费y C币，人气 * 2
c. 私聊 花费z C币，人气 - 2
其中 end 远大于start且start，end都为偶数， 请写一个程序帮助土豪计算一下，最少花费多少C币就能帮助该主播
Kiki将人气刚好达到end，从而能够晋级下一轮？

注意这道题想说明的问题：
直接写出暴力递归是跑不完的，边界条件不够，根本跑不完
缺少basecase
什么时候不用继续分类了？
'''

def kiki(x,y,z,start, end):
    if start >= end:
        return
    coinLimit = ((end-start)/2)*x

    return process(x,y,z, coinLimit, end, start, 0)


def process(x,y,z,coinLimit, aim, cur, curCoins):

    if cur == aim:
        return curCoins
    if curCoins > coinLimit:
        return float('inf')
    if cur >= 2*aim:
        return float('inf')
    if cur <= 0:
        return float('inf')

    minCoin = float('inf')

    p1 = process(x,y,z,coinLimit, aim,cur+2, curCoins+x)
    if p1 != float('inf'):
        minCoin = p1
    p2 = process(x,y,z,coinLimit, aim, cur*2, curCoins+y)
    if p2 != float('inf'):
        minCoin = min(minCoin, p2)
    p3 = process(x,y,z,coinLimit, aim, cur-2, curCoins+z)
    if p3 != float('inf'):
        minCoin = min(minCoin, p3)
    return minCoin

def generateMatrix(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    res = [[0 for i in range(n)] for i in range(n)]
    lr, lc = 0, 0
    rr, rc =n-1, n-1
    start = 1
    while lr <= rr:
        # end = ppp(lr,lc,rr,rc, res, start)

        for i in range(lc, rc):
            print('aaa')
            res[lr][i] = start
            start += 1
        for i in range(lr, rr):
            print('bbb')
            res[i][rc] = start
            start += 1
        for i in range(rc, lc, -1):
            print('ccc')
            res[rr][i] = start
            start += 1
        for i in range(rr, lr, -1):
            print('ddd')
            res[i][lc] = start
            start += 1
        lr += 1
        lc += 1
        rr -= 1
        rc -= 1

    return res


if __name__ == '__main__':
    x,y,z = 6,5,1
    start, end = 10, 24
    # print(kiki(x,y,z,start,end))
    print(generateMatrix(2))