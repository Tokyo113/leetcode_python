#coding:utf-8
'''
@Time: 2020/2/7 17:03
@author: Tokyo
@file: code_08_NeedParenthese.py
@desc:
一个完整的括号字符串定义规则如下:
①空字符串是完整的。
②如果s是完整的字符串，那么(s)也是完整的。
③如果s和t是完整的字符串，将它们连接起来形成的st也是完整的。
例如，"(()())", ""和"(())()"是完整的括号字符串，"())(", "()(" 和 ")"
是不完整的括号字符串。
牛牛有一个括号字符串s,现在需要在其中任意位置尽量少地添加括号,将其转化
为一个完整的括号字符串。请问牛牛至少需要添加多少个括号。

'''


def needParenthese(str):
    if str is None or str == '':
        return 0

    count, ans = 0, 0
    for i in str:
        if i == '(':
            count += 1
        else:
            if count == 0:
                ans += 1
            else:
                count -= 1
    # 最后如果count == 0,直接返回ans，
    # 如果count=8, 说明多了8个左括号，返回8+ans
    return count + ans


if __name__ == '__main__':
    str = '()(()())'
    str1 = ')()(((())())'
    print(needParenthese(str))
    print(needParenthese(str1))