#coding:utf-8
'''
@Time: 2020/2/28 10:18
@author: Tokyo
@file: code_16_StringConvert.py
@desc:
给定两个字符串str1和str2，再给定三个整数ic、dc和rc，分别代表插入、删
除和替换一个字符的代价，返回将str1编辑成str2的最小代价。
【举例】
str1="abc"，str2="adc"，ic=5，dc=3，rc=2
从"abc"编辑成"adc"，把'b'替换成'd'是代价最小的，所以返回2
str1="abc"，str2="adc"，ic=5，dc=3，rc=100
从"abc"编辑成"adc"，先删除'b'，然后插入'd'是代价最小的，所以返回8
str1="abc"，str2="abc"，ic=5，dc=3，rc=2
不用编辑了，本来就是一样的字符串，所以返回0


重点题型，每年考！！！！！
'''

def convert(s1, s2, ic,dc,rc):
    if s1 is None or s2 is None:
        return
    if s1 == '':
        return len(s2)*ic
    if s2 == '':
        return len(s1)*dc
    return process(s1,s2,len(s1)-1, len(s2)-1, ic,dc,rc)


def process(s1, s2, i1, i2, ic,dc,rc):
    '''
    返回把s1[0:i1]编辑为s2[0:i2]的最小代价
    注意不包括i1和i2
    :param s1:
    :param s2:
    :param i1:
    :param i2:
    :return:
    '''
    if i2 == 0 and i1 == 0:
        return 0
    if i1 == 0:
        return i2*ic
    if i2 == 0:
        return i1*dc
    # 这个容易被忽略，相同的话不用操作
    if s1[i1] == s2[i2]:
        return process(s1,s2,i1-1,i2-1,ic,dc,rc)
    # s1删掉一个，剩下的变成s2
    p1 = process(s1,s2,i1-1, i2,ic,dc,rc)+dc
    # s1变成s2前n-1个，再加入最后一个
    p2 = process(s1,s2,i1,i2-1,ic,dc,rc)+ic
    # 直接替换
    p3 = process(s1,s2,i1-1,i2-1,ic,dc,rc)+rc
    return min(p1,p2,p3)

def convert1(s1, s2, ic,dc,rc):
    if s1 is None or s2 is None:
        return
    if s1 == '':
        return len(s2)*ic
    if s2 == '':
        return len(s1)*dc
    return process1(s1,s2, ic,dc,rc,len(s1),len(s2))
def process1(s1,s2,ic,dc,rc,i,j):
    if j == 0 and i == 0:
        return 0
    if i == 0:
        return ic*j
    if j == 0:
        return dc*i
    if s1[i-1] == s2[j-1]:
        return process1(s1,s2,ic,dc,rc,i-1,j-1)
    return min(process1(s1,s2,ic,dc,rc,i-1,j)+dc, process1(s1,s2,ic,dc,rc,i-1,j-1)+rc,process1(s1,s2,ic,dc,rc,i,j-1)+ic)



def convertDP(s1,s2,ic,dc,rc):
    if s1 is None or s2 is None:
        return
    if s2 == '':
        return len(s1)*dc
    if s1 =='':
        return len(s2)*ic
    dp = [[0 for i in range(len(s2))]for i in range(len(s1))]
    for i in range(len(s2)):
        dp[0][i] = i*ic
    for i in range(len(s1)):
        dp[i][0] = i*dc

    for i1 in range(1,len(s1)):
        for i2 in range(1, len(s2)):
            if s1[i1] == s2[i2]:
                dp[i1][i2] = dp[i1-1][i2-1]
            else:
                p1 = dp[i1-1][i2]+dc
                p2 = dp[i1][i2-1]+ic
                p3 = dp[i1-1][i2-1]+rc
                dp[i1][i2] = min(p1,p2,p3)
    return dp[len(s1)-1][len(s2)-1]


def editStr(s1, s2, ic, dc, rc):
    if s1 == s2:
        return 0
    if s2 == '':
        return len(s1) * dc
    if s1 == '':
        return len(s2) * ic
    n, m = len(s1), len(s2)
    dp = [0 for i in range(len(s2) + 1)]
    for j in range(1, m + 1):
        dp[j] = ic * j
    for i in range(1, n + 1):
        for j in range(0, m + 1):
            tmp = dp[j]
            if j == 0:
                dp[0] = dc*i
            else:
                tmp = dp[j]
                if s1[i - 1] == s2[j - 1]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j - 1] + ic, dp[j] + dc, pre+ rc)
            pre = tmp


    return dp[m]


if __name__ == '__main__':

    str1 = "adsdfsgsgc"
    str2 = "abaresafcwdsrgdfbhdfhethtfdsvsvrgrgrg"
    # print(convert(str1,str2,5,3,100))
    # print(convert1(str1,str2,5,3,100))
    print(convertDP(str1,str2,5,3,100))
    print(editStr(str1,str2,5,3,100))

    str1 = "abcdf"
    str2 = "ab12cd3"
    print(convert(str1,str2,3,2,4))
    print(convertDP(str1, str2, 3, 2, 4))

    str1 = ""
    str2 = "ab12cd3"
    print(convert(str1,str2,1,7,5))
    print(convertDP(str1, str2, 1, 7, 5))


    str1 = "abcdf"
    str2 = ""
    print(convert(str1,str2,2,9,8))
    print(convertDP(str1, str2, 2, 9, 8))
