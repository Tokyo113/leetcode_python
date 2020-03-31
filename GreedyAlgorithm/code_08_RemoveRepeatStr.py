#coding:utf-8
'''
@Time: 2020/2/28 13:11
@author: Tokyo
@file: code_08_RemoveRepeatStr.py
@desc:
给定一个全是小写字母的字符串str，删除多余字符，使得每种字符只保留一个，并让
最终结果字符串的字典序最小
【举例】
str = "acbc"，删掉第一个'c'，得到"abc"，是所有结果字符串中字典序最小的。
str = "dbcacbca"，删掉第一个'b'、第一个'c'、第二个'c'、第二个'a'，得到"dabc"，
是所有结 果字符串中字典序最小的。
'''


def remove(str):
    if str is None or str == '':
        return ''
    wordMap = {}
    for i in str:
        if wordMap.get(i) == None:
            wordMap[i] = 1
        else:
            wordMap[i] += 1

    minAsciiIndex = 0
    for i in range(len(str)):
        wordMap[str[i]] -= 1
        minAsciiIndex = i if str[i] < str[minAsciiIndex] else minAsciiIndex
        if wordMap.get(str[i]) == 0:
            break

    new = str[minAsciiIndex+1:].replace(str[minAsciiIndex], '')

    return str[minAsciiIndex]+remove(new)


if __name__ == '__main__':

    print(remove('eebcbeb'))
    print(remove('dbcacbca'))
