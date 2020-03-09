#coding:utf-8
'''
@Time: 2020/3/8 17:18
@author: Tokyo
@file: code_18_ExpressionMatch.py
@desc:
判定一个由[a-z]字符构成的字符串和一个包含'?'和'*'通配符的字符串是否匹配。
通配符'?'匹配任意单一字符,'*'匹配任意多个字符包括0个字符。
字符串长度不会超过100，字符串不为空。
输入描述：
字符串 str 和包含通配符的字符串 pattern。1 <= 字符串长度 <= 100输出描述：
true 表示匹配，false 表示不匹配
'''
def match(s,p):
    if s is None or p is None:
        return False
    return process(s,p,0,0)


def process(s,p,i,j):
    if j == len(p):
        return True if i == len(s) else False
    # 不需要考虑j+1位置时的情况
    # 要么不存在j+1位置，要么j+1位置不是*
    if j+1==len(p) or p[j+1]!= '*':
        return i != len(s) and (s[i]==p[j] or p[j]=='.') \
               and process(s,p,i+1,j+1)
    # j+1位置是*
    else:
        while i !=len(s) and (s[i] == p[j] or p[j] == '.'):
            if process(s,p,i,j+2):
                return True
            i += 1
        return process(s,p,i,j+2)

if __name__ == '__main__':
    s = 'abcdeef'
    p = '.*cde*.'
    print(match(s,p))
