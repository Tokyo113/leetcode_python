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

    return process(x,y,z,start, end)


def process(x,y,z,cur, end):

    if cur == end:
        return 0
    if cur >= 2*end:
        return float('inf')

    if cur <= 0:
        return float('inf')
    else:
        return min(process(x,y,z,cur+2, end)+x, process(x,y,z,cur*2, end)+y, process(x,y,z,cur-2,end)+z)


if __name__ == '__main__':
    x,y,z = 6,5,1
    start, end = 10,30
    print(kiki(x,y,z,start,end))