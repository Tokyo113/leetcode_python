#coding:utf-8
'''
@Time: 2020/2/29 10:39
@author: Tokyo
@file: code_02_StringToKth.py
@desc:
在K数MP据算加法密扩和展数据题压目缩二中常需要对特殊的字符串进行编码。给定的字母表A由26个小写英文字母组成，即
A={a, b...z}。该字母表产生的长序字符串是指定字符串中字母从左到右出现的次序与字母在字母表中出现
的次序相同，且每个字符最多出现1次。例如，a，b，ab，bc，xyz等字符串是升序字符串。对字母表A产生
的所有长度不超过6的升序字符串按照字典排列编码如下：a(1)，b(2)，c(3)……，z(26)，ab(27)，
ac(28)……对于任意长度不超过16的升序字符串，迅速计算出它在上述字典中的编码。
输入描述：
第1行是一个正整数N，表示接下来共有N行，在接下来的N行中，每行给出一个字符串。输出描述：
输出N行，每行对应于一个字符串编码。
示例1:
输入
3
a
b
ab
输出
1
2
27

百度原题，难题
总体思路：一位一位往后看，统计出他前面的个数一点一点加上去
'''

def g(i, n):
    '''
    返回以第i号字符开头，总长度为n的子序列的个数
    :param i:
    :param n:
    :return:
    '''
    if n <= 0:
        return 0
    if n == 1:
        return 1
    res = 0
    for j in range(i+1, 27):
        res += g(j, n-1)
    return res






def f(n):
    '''
    返回总长度为n的子序列的个数
    :return:
    '''
    if n <= 0:
        return 0
    res = 0
    for i in range(1,27):
        res += g(i,n)
    return res


def findKth(str):
    if str is None or str == '':
        return -1
    if len(str) == 1:
        return ord(str)-ord('a')+1
    res = 0
    n = len(str)
    # 先统计长度为1,2,3,...,n-1的子序列的个数
    # 必然在str前面
    for i in range(1,n):
        res += f(i)
    pre = 0
    length = n
    # 再看长度为n的子序列，排在str[0]之前的
    for k in range(len(str)):
        index = ord(str[k])-ord('a')+1
        for i in range(pre+1,index):
            res += g(i, length)
        pre = index
        length -= 1
    # res统计的是在str前面的个数，最后还需要加一
    return res+1






if __name__ == '__main__':
    print(findKth('abc'))
    print(findWord('abc'))


