#coding:utf-8
'''
@Time: 2020/2/27 14:48
@author: Tokyo
@file: code_01_LongestSubString.py
@desc:
在一个字符串中找到没有重复字符子串中最长的长度。
例如：
abcabcbb没有重复字符的最长子串是abc，长度为3
bbbbb，答案是b，长度为1
pwwkew，答案是wke，长度是3
要求：答案必须是子串，"pwke" 是一个子字符序列但不是一个子字符串。
'''

def longestSubstring(str):
    if str is None or str == '':
        return 0
    strMap = [-1 for i in range(256)]
    pre = -1
    len1 = 1
    for i in range(len(str)):
        cur = max(strMap[ord(str[i])], pre)
        len1 = max(i-cur, len1)
        pre = cur
        strMap[ord(str[i])] = i
    return len1

if __name__ == '__main__':
    str = 'abbcdcaccd'
    str1 = 'aaa'
    print(longestSubstring(str1))






