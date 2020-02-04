#coding:utf-8
'''
@Time: 2020/2/4 16:00
@author: Tokyo
@file: code_04_ColorLeftRight.py
@desc:
牛牛有一些排成一行的正方形。每个正方形已经被染成红色或者绿色。牛牛现在可
以选择任意一个正方形然后用这两种颜色的任意一种进行染色,这个正方形的颜色将
会被覆盖。牛牛的目标是在完成染色之后,每个红色R都比每个绿色G距离最左侧近。
牛牛想知道他最少需要涂染几个正方形。
如样例所示: s = RGRGR
我们涂染之后变成RRRGG满足要求了,涂染的个数为2,没有比这个更好的涂染方案。
'''

def minPaint(str):
    '''
    暴力方法，O(N2)
    :param str:
    :return:
    '''
    if str is None or len(str)< 2:
        return 0
    minPaints = len(str)
    for i in range(len(str)+1):
        cnt = 0
        for left in str[:i]:
            if left != 'R':
                cnt += 1

        for right in str[i:]:
            if right != 'G':
                cnt += 1
        minPaints = min(minPaints, cnt)
    return minPaints


def minPaint2(str):
    '''
    申请辅助结构，分别统计左侧G和右侧R的个数
    :param str:
    :return:
    '''
    if len(str) < 2 or str is None:
        return 0
    # leftG  0~i上G的个数
    # rightR i~N-1上R的个数
    leftG = []
    cnt = 0
    for i in str:
        if i == "G":
            cnt += 1
            leftG.append(cnt)
        else:
            leftG.append(cnt)
    rightR = [0 for i in range(len(str))]
    rightR[len(str)-1] = 0 if str[-1] == "G" else 1
    for i in range(len(str)-2, -1, -1):
        rightR[i] = rightR[i+1]
        rightR[i] += 1 if str[i] == 'R' else 0
    mincolor = len(str)

    for i in range(len(str)+1):
        if i == 0:
            mincolor = min(mincolor, rightR[0])
        elif i == len(str):
            mincolor = min(mincolor, leftG[-1])
        else:
            mincolor = min(mincolor, leftG[i-1]+rightR[i])
    return mincolor





if __name__ == '__main__':
    str = "GRRGGGGR"
    print(minPaint2(str))
    print(minPaint(str))



