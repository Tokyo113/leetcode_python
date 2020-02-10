#coding:utf-8
'''
@Time: 2020/2/9 17:30
@author: Tokyo
@file: code_09_ParentheseDeep.py
@desc:
一个合法的括号匹配序列有以下定义:
①空串""是一个合法的括号匹配序列
②如果"X"和"Y"都是合法的括号匹配序列,"XY"也是一个合法的括号匹配序列
③如果"X"是一个合法的括号匹配序列,那么"(X)"也是一个合法的括号匹配序列
④每个合法的括号序列都可以由以上规则生成。
例如: "","()","()()","((()))"都是合法的括号序列
对于一个合法的括号序列我们又有以下定义它的深度:
①空串""的深度是0
②如果字符串"X"的深度是x,字符串"Y"的深度是y,那么字符串"XY"的深度为
max(x,y) 3、如果"X"的深度是x,那么字符串"(X)"的深度是x+1
例如: "()()()"的深度是1,"((()))"的深度是3。牛牛现在给你一个合法的括号
序列,需要你计算出其深度。
'''


def deep(str):
    count = 0
    maxDeep = 0
    for i in str:
        if i == '(':
            count += 1
            maxDeep = max(maxDeep, count)
        else:
            count -= 1
    return maxDeep


if __name__ == '__main__':
    str = '((()))'
    print(deep(str))
